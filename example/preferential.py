"""
    CITS1401 project 2 2017
    Name(s): Cunjun Yin
    Student Number(s): 22249435
    Date:  30/10/2017   date-of-submission
"""

def get_candidates(file_name):
    """
    Args:
        file_name (str): the file name that contain candidates
    returns:
        candidates (list): always return [], no matter what unexpected error occure
    Except:
        FileNotFoundError: if file is not find
    """
    candidates = []
    try:
        dict = open(file_name,mode = 'r')
    except FileNotFoundError as e:
        print("cannot open {0},I/O error({1}): {2}".format(f,e.errno,e.strerror))
    else:
        with dict:
            for line in dict:
                line = line.strip()
                if(line): #check the line in empty after strip
                    candidates.append(line)
    finally:
        return candidates
    
#---------------------------------------------------------------------------------
def parse_vote(string_vote,num_candidates):
    """
    Args:
        string_vote (str) : a char string
        num_candidates (int) : how many candidates in this election
    returns:
        string_vote to int, otherwise(not digit, too big, to small) return 0
    example:
        num_candidates = 5
        ' 1 ' -> 1
        '1 5' -> 0
        '-1' -> 0
        '15' -> 0
    """
    
    string_vote = string_vote.strip() # remove white space
    if string_vote: #check not empty after strip
        if string_vote.isdigit(): # check the input is digit
            string_vote = int(string_vote)
            #check condictions
            if string_vote > 0:
                return string_vote
    return 0

def votes_range(votes):
    """
    Args:
        votes (list): a list of votes
    returns:
        True if successful, False otherwise.
    example:
        votes = [1,2,3,4,5] -> True
        votes = [1,2,4,5,6] -> False
    """

    if votes:
        max_votes = max(votes)+1
        # 1 -> max in votes
        for i in range(1,max_votes):
            if i not in votes: #
                return False
                break # Informal Votes, No Need To Check
    return True

def parse_paper(votes,num_candidates,optional):
    """
    Args:
        votes (str): votes in string ,separate by ','
        num_candidates (int): number of candidates in this election
        optional (bool): optional preferential allowed = True, otherwise False
    returns:
        result(list) is successful, None otherwise.
    example:
        optional = False  votes = "1,2,3,4,5" num_candidates = 5 ->[1,2,3,4,5]
        optional = False  votes = ",2,3,4,5" num_candidates = 5 ->None
        optional = True  votes = ",2,3,4,5" num_candidates = 5 ->[0,2,3,4,5]
        optional = True/False  votes = "2,3,4,5" num_candidates = 5 ->None
        optional = True/False  votes = "1,2,3,4,6" num_candidates = 5 ->None
    """
    result = None
    votes = votes.split(",") #split string by delimiter ,
    if len(votes)==num_candidates: # check number of votes if too less or too more,so we dont have to consider
        result = [] # make result point to a list
        for vote in votes: # iterate through votes list
            vote = parse_vote(vote,num_candidates) # string change to int
            if vote > num_candidates: #no vote too big it in any situation
                return None
                break
            
            if result.count(vote)==0 or vote == 0: # no duplicate in any situation
                result.append(vote)
            else:
                print(result)
                return None
                break
        if not votes_range(result): # not in order 1 -> max votes,no need consider
            result = None
        elif (0 in result) and (not optional):# as zero repoesent informal,optional not allowed so result -> None
            result = None
        elif all(v == 0 for v in result): # empty ballot or unecpected result
            result = None
    return result

def getPapers(file_name,num_candidates,optional):
    """
    Args:
        file_name (str): the file name contain ballot papers
        num_candidates (int): number of candidates in this election
        optional (bool)
    return:
        ballot_papers (list): always return a list, no matter what unexpected error occure
    except:
        FileNotFoundError : cannot file the file or directory
    """
    count = 0
    ballot_papers = []
    try:
        ballot_papers_f = open(file_name,mode = 'r')
    except FileNotFoundError as e:
        print("cannot open {0},I/O error({1}): {2}".format(f,e.errno,e.strerror))
    else:
        with ballot_papers_f:
            for line in ballot_papers_f:
                line = line.strip()
                ballot = parse_paper(line,num_candidates,optional)
                if(ballot != None):
                    ballot_papers.append(ballot)
                else:
                    count +=1
    finally:
        return ballot_papers,count
#--------------------------------------------------------------------------
    
def get_first_pref(ballot_papers,candidates,num_candidates):
    """
    Args:
        ballot_papers (list): 2d list contain ballots
        candidates (list): list contain candidates
        num_candidates (int): number of candidates in this election
    return:
        list tuple: each tuple with diferent candidates and number of their 1s pref in first count
        dict: a dictionary contain candidates with they 1st pref in ballot_papers
    """
    first_pref = [0]*num_candidates #creat a 1d list with zeros
    ballot_index_at = [[] for i in range(num_candidates)] #creat a 2d list with zeros
    i = 0
    for votes in ballot_papers:
        if 1 not in  votes: #check it contain first preference 
            continue # if no skip
        firstPrefIndex = votes.index(1) #file which candidate get this frist pref
        first_pref[firstPrefIndex] = first_pref[firstPrefIndex] + 1 # this candidate  get one more suppoter
        ballot_index_at[firstPrefIndex].append(i) # remember who vote for this candidate
        i = i + 1
    first_pref_candidates_Tuple = [tuple([i,j]) for i,j in zip(first_pref,candidates)]
    return first_pref_candidates_Tuple,dict(zip(candidates,ballot_index_at))
#--------------------------------------------------------------------------

def sortTuple(list_tuple):
    """
    Args:
        list_tuple (list): a list of tuples
    return:
        list_tuple sorted in desc order
    """
    return sorted(list_tuple,key=lambda tup: tup[0],reverse = True) 

def print_tuple(list_tuple,count):
    """
    Args:
        list_tuple (list): list of tuples 
        count (int) :
    """
    print("count {}".format(count))
    list_tuple = sortTuple(list_tuple)
    for vote, candidate in list_tuple:
        print(vote,"\t",candidate)

def fifty_plus1(perfer_tuple,num_ballots):
    """
    Args:
        perfer_tuple (list): list of tuples(2 elements), (int,String) 
        num_ballots (int): minimum 50% of the elegible votes, plus 1)
    return:
        bool: True if successful, False otherwise.
    """
    maxVote = max(perfer_tuple,key=lambda perfer_tuple:perfer_tuple[0]) #wow find max in tuple[0]
    is_elected = (maxVote[0] >= num_ballots)
    if is_elected or len(perfer_tuple) <=2: #check one got max or 2 candidates left chose one
        print("\nCandidate {} is elected".format(maxVote[1]))
        return True
    return is_elected

#--------------------------------------------------------------------------

def del_votes(BallotPapers,index):
    """
    Args:
        BallotPapers (list) : list of ballots votes
        index (int) : which index in ballot vote get remove
    return:
        BallotPapers[i++].pop(index)
    example:
        index = 1
        [[1,2,3,4,5],[1,2,3,4,5]] -> [[1,3,4,5],[1,3,4,5]]
    """
    for i in BallotPapers:
        del i[index]
    return BallotPapers

def candidate_MiniVotes(first_pref):
    """
        args:
            first_pref (list): list of tuples(2 elements),(int,string)
        return:
            candidate (string): candidate[1]
            (int) : candidate current index sat in first_pref
    """
    candidate = min(first_pref,key=lambda first_pref:first_pref[0])
    return [candidate[1],[i[1] for i in first_pref].index(candidate[1])]

def append_value(index_in_ballot,index,value):
    """
        this function us designed to append value in dict, the value have to be list else error pop
        args:
            index_in_ballot (dict): dictionary of candidate and their 1st pref indec set in ballots_paper
            index (int): which candidate get the value in dict
            value (int): value get append in the index_in_ballot's value
    """
    cans = list(index_in_ballot)
    can = cans[index]
    index_in_ballot.get(can).append(value) # this candidate get the ballot(value)

def resort_count(ballotPapers,fristPrefAt,index_in_ballot,num_candidates,const_num_candidates):
    """
        this function is used to found which candidate will get which vote from remove candidate
        args:
            ballotPapers (list): list of ballot
            fristPrefAt (list): list of index in ballotPapers
            index_in_ballot (dict): dictionary of candidate and their 1st pref indec set in ballots_paper
            num_candidates (int): how many candidates in this election
            const_num_candidates (int): how many candidates in this election(guaranteed not change)
        return:
            result: which candidates get more votes
            index_in_ballot: new index_in_ballot 
    """
    result = [0]*num_candidates #set how many space required
    for i in fristPrefAt: #range(index in ballot papers)
        for ii in range(2,const_num_candidates+1): # ii = 2 -> num_candidates "THE BEGINING NUMBER"
            if ii in ballotPapers[i]:  # oh, this ballot contain it do some thing and break it
                indexOfvote = ballotPapers[i].index(ii) # find which candidate will get this ballot by index
                result[indexOfvote] = result[indexOfvote] +1 # +1 for him
                append_value(index_in_ballot,indexOfvote,i) # he got this vote
                break
    return result,index_in_ballot

def get_index_in_ballot(index_in_ballot,candidate):
    """
        this function is unsed to get the value form candidate -> his index in ballor_papers
        args:
            index_in_ballot (dict): dictionary of candidate and their 1st pref indec set in ballots_paper
            candidate (stirng): candiddate with samallest votes
        return:
            list : the value get form index_in_ballot
    """
    return index_in_ballot.get(candidate) # get this candidate's index in ballot papers

def resort(firstPref,addPref): 
    """
        this function is used to update candidate's vote  after some one get removed
        args:
            firstPref (list):list of tuples(2 elements),(vote,candidate)
            addPred (list): list of votes in candidate order
        return:
            firstPref (list)
    """
    i = 0
    for vote,candidate in firstPref:
        if addPref[i] != 0: # don't have consider zero,
            vote = vote + addPref[i];
            firstPref[i] = (vote,candidate) # undate this candidate's vote
        i = i+1
    return firstPref

#---------------------------------------------------------------------------------
def exclusion(firstPref,this_candidate):
    """
        args:
            firstPref (list):list of tuples(2 elements)->(vote,candidate)
            this_candidate (string): candidate get remove
        return:
            firstPref (list): new list of tuples(2 elements),(vote,candidate) with this_candidate get exclude
    """
    i = 0
    for vote,candidate in firstPref:
        if candidate == this_candidate: # in the candidate in tuple is wanted TODO
            del firstPref[i] # remove this candidate
            break #no need to loop anymore 
        i = i + 1
    print("\nCandidate {} has the smallest number of votes and is eliminated from the count\n".format(candidate))
    return firstPref
#---------------------------------------------------------------------------------

def Election(firstPref,ballotPapers,index_in_ballot,num_candidates,num_ballot):
    """
        args:
            firstPref (list): list of tuples(2 elements),(vote,candidate)
            ballotPapers (list): list of ballot
            index_in_ballot (dict): dictionary of candidate and their 1st pref indec set in ballots_paper
            num_candidates (int): how many candidates in this election
            num_ballot (int): 50% +1
    """
    
    count = 1;
    const_num_candidates = num_candidates
    while True:
        print_tuple(firstPref,count)
        
        if fifty_plus1(firstPref,num_ballot): # as some one gto elected no need to loop through anymore
            break
        
        del_candidate = candidate_MiniVotes(firstPref) # get the candidate gets removed and his index 
        ballotPapers = del_votes(ballotPapers,del_candidate[1]) #ballot votes - 1
        fristPrefAt = get_index_in_ballot(index_in_ballot,del_candidate[0])# list of index in ballot papers
        del index_in_ballot[del_candidate[0]] #remove this candidate in dictionary
        firstPref = exclusion(firstPref,del_candidate[0]) # remove this candidate
        num_candidates -= 1 #number of candidates - 1 as we deleted one
        resort_count_result = resort_count(ballotPapers,fristPrefAt,index_in_ballot,num_candidates,const_num_candidates) # add,new index_in_ballot
        add,index_in_ballot = resort_count_result[0],resort_count_result[1]
        firstPref = resort(firstPref,add) # add number in list to tuple parallely
        count += 1

def main(candidates_file_name, ballots_file_name, optional=False):
    """
        args:
            candidates_file_name (String): the file name that contain candidates
            ballots_file_name (String): the file name that contain ballots
            optional (bool)
    """
    candidates = get_candidates(candidates_file_name) # get candidate
    Num_candidates = len(candidates) # get number of candidate at the start
    getPapers_result=getPapers(ballots_file_name,Num_candidates,optional) # get papers
    ballot_papers,informal = getPapers_result[0],getPapers_result[1]
    num_ballot = int(len(ballot_papers)/2)+1 # used in 50 + 1
    get_first_pref_result = get_first_pref(ballot_papers,candidates,Num_candidates) # get num of first pref for each candidate
    Election(get_first_pref_result[0],ballot_papers,get_first_pref_result[1],Num_candidates,num_ballot) # election step
    print("{} papers excluded as informal".format(informal))
    
##import time
##def run():
##    start_time = time.time()
##    main("candidates.txt","ballot1.txt",optional=False)
##    print("--- %s sec ---" % (time.time() - start_time))