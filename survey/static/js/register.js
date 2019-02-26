var display = false;

// red orange green blue
function passwordC() {
    "use strict";
    var username = $('#firstname').val() + $('#lastname').val();
    var password = $("#password").val();
    var PWDlength = password.length;
    // password === username
    if (username) {
        if (password.toLowerCase().equals(username.toLowerCase())) {
            score = 0;
        }
        var user = new RegExp(username.toLowerCase());
        if (password.toLowerCase().match(user)) {
            score = 0;
        }
    }

    var score = 50;

    if (PWDlength < 7) {
        if (!display) {
            $("#strength").html("Add " + (7 - PWDlength).toString() + " characters");
        }
        display = true;
    }

    if (PWDlength > 8 && PWDlength < 13) {
        score += 50 - ((13 - PWDlength) * 10);
    }

    if (score > 100 || PWDlength >= 13) {
        score = 100;
    }

    // password has at least 1 sybols
    if (!password.match(/[-!$%^&*()_+|~=`{}\[\]:";'<>?,.\/]/)) {
        if (!display) {
            $("#strength").html("Add Some Symbols to make it stronger");
        }
        display = true;
        score -= 10;
    }

    // password has Upper and Lower chars
    if (!password.match(/([a-z])/)) {
        if (!display) {
            $("#strength").html("Add some Lower case characters to make it stronger");
        }
        display = true;
        score -= 10;
    }

    if (!password.match(/([A-Z])/)) {
        if (!display) {
            $("#strength").html("Add some Upper case characters to make it stronger");
        }
         display = true;
        score -= 15;
    }

    // password has number
    if (!password.match(/([0-9])/)) {
        if (!display) {
            $("#strength").html("Add Some Numbers to make it stronger");
        }
        display = true;
        score -= 15;
    }

    if (score < 0 || PWDlength === 0) {
        score = 0;
    }
    //color chosen
    if (score >= 25 && score <= 50) {
        $("#submit").prop("disabled",true);
        $("#strength").css("background-color", "orange");
    }else if(score > 50 && score <= 75){
        $("#submit").prop("disabled",false);
        $("#strength").css("background-color", "green");
    }else if (score > 75){
        $("#submit").prop("disabled",false);
        $("#strength").css("background-color", "blue");
    }else{
        $("#submit").prop("disabled",true);
        $("#strength").css("background-color", "red");
    }

    // change the width of the progress
    var percent = score.toString() + "%";
    $("#strength").css("width", percent);
    display = false;
}

jQuery((document)).ready(function () {
    "use strict";
    $("#submit").prop("disabled",true);
    $("#password").keydown(function () {
        passwordC();
    });
});
