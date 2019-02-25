var prama = {
    containsUsername: "ops, seems like this passwork contain the username",
    shortPWD: "The password is too short",
    weekPWD: "Too week; combination of letters & numbers, plz",
    mediumPWD: "OkOk; try some symbols to make it harder",
    strongPWD: "Strong Passwork",
    onlyChar: "add some Numbers & Symbols",
    onlyNumber: "add some Charters & Symbols",
    onlySymbols: "add some Charters & Numbers",
    username: false,
    minimumLength: 8,
    pass: true
};

var displayed = false;

// red orange green blue
function passwordC() {
    "use strict";
    var username = $('#firstname').val() + $('#lastname').val();
    var password = $("#password").val();
    var PWDlength = password.length;
    // password === username
    if (username) {
        if (password.toLowerCase().equals(username.toLowerCase())) {
            return 0;
        }
        var user = new RegExp(username.toLowerCase());
        if (password.toLowerCase().match(user)) {
            return 0;
        }
    }

    var score;

    if (PWDlength < 8){
        score = 50;
    }else{
        score = 100;
    }

    if (PWDlength > 8 && PWDlength <= 13) {
        score +=(13-PWDlength)*10;
    }

    if (score > 100) {
        score = 100;
    }

    // password has at least 1 sybols
    var symbols = '.*[!,@,#,$,%,^,&,*,?,_,~]';
    symbols = new RegExp('(' + symbols + ')');
    if (!password.match(symbols)) {
        score -= 10;
    }

    // password has Upper and Lower chars
    if (!password.match(/([a-z])/)) {
        score -= 10;
    }

    if (!password.match(/([A-Z])/)) {
        score -= 15;
    }

    // password has number
    if (!password.match(/([0-9])/)) {
        score -= 15;
    }

    if (score < 0 || PWDlength === 0) {
        score = 0;
    }

    var percent = score.toString() + "%";
    $("#strength").css("width", percent);
}

jQuery((document)).ready(function () {
    "use strict";
    $("#password").keydown(function () {
        passwordC();
    });
});
