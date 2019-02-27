function build_table(){
    var table = document.getElementById("account_table");
    var row_size = 0;
    var row, cell0, cell1, cell2, cell3;
    while(0){
        row = table.insertRow(0);
        cell0 = row.insertCell(0);
        cell1 = row.insertCell(1);
        cell2 = row.insertCell(2);
        cell3 = row.insertCell(3);
        cell1.innerHTML = "cell0 Data";
        cell1.innerHTML = "cell1 Data";
        cell1.innerHTML = "cell2 Data";
        cell1.innerHTML = "cell3 Data";
    }
}

jQuery((document)).ready(function () {
    $('#polls_tab').on('click', function (e) {
        alert("this is an expernment");
    });
});
