(function() {
  var backButton = document.getElementById('js-history-back')
  backButton.onclick = function() {
    history.go(-1)
  }
}());
