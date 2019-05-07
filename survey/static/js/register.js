var display = false;
var PWDlength;
var password;
var score;
var emailRegx = /^([0-9A-Za-z]{3,})(\.[a-zA-Z0-9_-]{1,})*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
var passed = false;

function validiateEmail(){
	var email = $("#email").val();
	return emailRegx.test(email);
}

// red orange green blue
function passwordC() {
    password = $("#password").val();
    PWDlength = password.length;

    score = 50;
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

	var passwordPassed = false;
    //color chosen
    if (score >= 25 && score <= 50) {
        $("#strength").css("background-color", "orange");
    } else if (score > 50 && score <= 75) {
		passwordPassed = true;
        $("#strength").css("background-color", "green");
    } else if (score > 75) {
		passwordPassed = true;
        $("#strength").css("background-color", "blue");
    } else {
        $("#strength").css("background-color", "red");
    }

    $("#strength").css("width", score.toString() + "%");

	var FName_L = $("#firstname").val().length;
	if(FName_L>0 && FName_L<21){
		var LName_L = $("#firstname").val().length;
		if(LName_L > 0 && LName_L<21){
			if ($("input[name='gender']:checked").val()) {
				if(PWDlength<61){
					if(validiateEmail()){
						if(passwordPassed){
							if(password === $("#confirm_password").val()) passed =true;
							else passed = false;
						}else passed = false;
					}else passed = false;
				}else passed = false;
			}else passed = false;
		}else passed = false;
	}else passed = false;

	// chose display or not
	if(passed){
		$("#submit").prop("disabled", false);
	}else{
		$("#submit").prop("disabled", true);
	}
    display = false;
}

jQuery((document)).ready(function () {
	setInterval(function() {
  		passwordC()
	}, 300);
});
