var prama = {
    containsUsername: "ops, seems like this passwork contain the username",
    shortPWD: "The password is too short",
    weekPWD: "Toooo week; combination of letters & numbers, plz",
    mediumPWD: "OkOk; try some symbols to make it harder",
    strongPWD: "Strong Passwork",
    onlyChar: "add some Numbers & Symbols",
    onlyNumber: "add some Charters & Symbols",
    onlySymbols: "add some Charters & Numbers",
    username: false,
    minimumLength: 8,
    pass: true
};

function strength(strength) {
    switch (strength) {
        // contain user name
        case 0:
            break;
            // too short
        case 10:
            break;
            // only char
        case 20:
            break;
            // only number
        case 30:
            break;
            // only symbols
        case 40:
            break;
            //1 uper case, char, number
        case 50:
            return 0;
    }
}

function password(PWD, username) {
    // password === username
    if (PWD.toLowerCase().equals(username.toLowerCase())) {
        return 0;
    }
    var user = new RegExp(username.toLowerCase());
    if (password.toLowerCase().match(user)) {
        return 0;
    }

    //test password requirement
    PWDlength = PWD.length;
    if (PWDlength < 8) return 10;

    if (PWD.match(/^\w+$/)) {
        return 20;
    }
    if (PWD.match(/^\d+$/)) {
        return 30;
    }
    if (PWD.match()) {
        return 40;
    }

    // pass test initialize score to 0
    score = 0;
    //normalization
    if (PWD.match(/([a-z])/) && PWD.match(/([0-9])/) && PWD.match(/([A-Z])/)) {
        if(PWDlength>13) PWDlength=13;
        score = (100-(13-PWDlength))*10;
    }
    return score;
}

function init(){

}
