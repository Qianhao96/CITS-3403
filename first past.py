"""
   CITS1401 Project 1 2017
   Name(cunjun yin):
   Student number(22249435):
   Date:10/9/2017             date-of-submission 22/9/2017
"""

"""
@param f: this represent the file to input
@retrun list_candidates: return all the name in the file, were add in the list(list_candidates)
@raise keyError: raises a exception if file not found
"""
def getCandidates(f):
    list_candidates = []
    try: 
        candidates_file = open(f,mode = 'r')
    except FileNotFoundError as e:
        print("cannot open {0},I/O error({1}): {2}".format(f,e.errno,e.strerror))
    else:
        with candidates_file:
            for line in candidates_file:
                line = line.strip()
                if(len(line) > 0 ):
                    list_candidates.append(line)
    return list_candidates

"""
@param s: s represent the to input of length = 1 Stirng
@return s: -1(not a number or less than 0) or positive number 
"""
def parseVote(s):
    s = s.strip()
    if (len(s) == 0):
        s = 0
    else:
        if s.isdigit():
            s = int(s)
            if s < 0:
                s = -1
        else:
            s = -1
    return s

"""
@param s: take a String TODO
@param n: the number of elements in the String array[]
@param result: an array[] to store Intergers
@param number.: boolean variable initialized to true to check is a number 
@return ([], 'non-digits'): if one or more elements in the Interger array(result) is not String Interger
@return ([], 'too long'): if length of Interger array(result) is greater than n(paramater)
@return ([], "blank"): if length of interger array(result) is zero or all number in result is zero
@return result: array with correct number of elements and type
"""
def parsePaper(s, n):
    votes = s.split(',') # list with one long String seperated words by "," 
    result = []
    number = True
    for vote in votes:
        vote = parseVote(vote)
        if vote >=0: 
            result.append(vote)
        else:
            number = False
            break #as one elements in array[] is not number, do have to check others
            
    if (number == False):
        return([], 'non-digits')
    elif len(result) > n:
        return([], 'too long')
    elif (len(result) == 0) or all(num == 0 for num in result) :
        return([], "blank")
    else:
        return(result,'')
    
"""
@param f: an input, this represent the file to input, should contain lines of numbers,
          and used to moderfied by other functions
@param n: an input, the number of elements in the list []
@retrun ballotPapers: is a list containing the result moderfied by parsePaper(s, n):
@raise keyError: raises a exception if file not found
"""
def getPapers(f,n):
    ballotPapers = []
    try:
        candidates_file = open(f,mode = 'r')
    except FileNotFoundError as e:
        print("cannot open {0},I/O error({1}): {2}".format(f,e.errno,e.strerror))
    else:
        with candidates_file:
            for line in candidates_file:
                line = line.strip()
                ballotPapers.append(parsePaper(line, n))
    return ballotPapers

"""
@param p: input a list [] of numbers  
@param n:number of candidates(should be as the number of elements in the list [])
@param theSumOfVote: sum the all number in the list
@return result[]: an list contain normlised input list e.g num/total-(percentage)
"""
def normalisePaper(p, n):
    result = []
    theSumOfVote = 0
    if isinstance(p[0], list): 
        p = p[0]# use p[0] as getpapers will return a length of 2 array {[array], String}
    if len(p) < n: #put [0]'s into p array if the len of p is lesser than n 
        p += [0]*(n-len(p))
    theSumOfVote = sum(p)
    if (theSumOfVote == 0):#avoid division by (0)
        theSumOfVote = 1
    for vote in p:
        result.append(vote/theSumOfVote)
    return result #return array wilh result of elements divided by theSumOfVote

"""
@param ps: a 2D list with numbers
@param n: number of caididates or how many elements you expected in the lists[]'s list[]
@return result[]: a 2D list with normlized data(ps) by the function normalisePaper(p, n)
"""
def normalisePapers(ps,n):
    result = []
    for paper in ps:
        result.append(normalisePaper(paper, n))
    return result 

"""
@param cs: represent the candidates list 
@param ps; the return result by normalisePapers(ps,n)
@return [cs]:[NormaliseedData,Candidates]
"""
def countVotes(cs, ps):
    tempPs =(sum(p) for p in zip(*ps))
    cs =[[i,j] for i,j in zip(tempPs,cs)] 
    cs.sort(reverse = True)#order the data in desc order
    return cs

"""
@param normalised_ballot_Paper_lis: type(list), result from normalisePapers(ps,n)
@print paramater informal and formal
"""
def in_formalvotes(normalised_ballot_Paper_list):
    informal,formal=0,0 #
    for normalised_ballot_Paper in normalised_ballot_Paper_list:
        if sum(normalised_ballot_Paper)==0: # as dont contain anything or all zeros 
            informal +=1 
        else:
            formal +=1
    print("There were {} informal votes".format(informal))
    print("There were {} formal votes\n".format(formal))
            
"""
@param c: this param is take the result value from the function countVotes(cs, ps)
@Print c[0],c[1]
"""
def printCount(c):
    for candidates_votes in c:
        print("%.2f"%candidates_votes[0]," ",candidates_votes[1])

"""
this is the function that the program run from start to end,
"""
def main():
    print("this is the election program\n")
    the_candidates_file = str(input("Enter the file name that used to store candidates: "))
    candidates_list = getCandidates(the_candidates_file) #getCandidates(f)
    if  len(candidates_list)!=0:
        number_of_candidates = len(candidates_list)
        ballot_papers_file= str(input("Enter the file name that contain the ballot: "))
        ballot_papers_list = getPapers(ballot_papers_file,number_of_candidates)#getPapers(f,n)
        normalised_ballot_Papers_list = normalisePapers(ballot_papers_list, number_of_candidates)#normalisePapers
        if len(normalised_ballot_Papers_list)!=0:
            percentage_Votes_Of_Each_Candidates = countVotes(candidates_list,normalised_ballot_Papers_list)
            print("Nerdvanian election 2017\n")
            in_formalvotes(normalised_ballot_Papers_list)
            printCount(percentage_Votes_Of_Each_Candidates)#printCount(c)
        else:
            print("PROGRAM TERMINATED UNSUCCESSFUL")
    else:
        print("PROGRAM TERMINATED UNSUCCESSFUL")
        
#if __name__ == "__main__" :
  #main()
