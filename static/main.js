//Displaying the selected month to the user

function printCalendar() {

    //Taking input month from the select month drop down menu by creating a variable

    var selectedMonth = document.getElementById("choose-month").value;

    // Displaying the selected month as a pop up
    
    alert("Selected month: " + selectedMonth);
}