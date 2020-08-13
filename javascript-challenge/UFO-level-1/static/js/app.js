// from data.js
var tableData = data;

// select tbody 
var tbody = d3.select("tbody");
console.log("tbody selected");

// Build table to display data
function displayTable(data) {
    tbody.text("")
    console.log("Build table");
    data.forEach(function(UFOSightings) {
        new_tr = tbody.append("tr")
        Object.entries(UFOSightings).forEach(function([key, value]) {
            new_td = new_tr.append("td").text(value)
        })
    })
}

// display table and send to console
displayTable(tableData);
console.log("Table displayed");


//Collect date selection
var button = d3.select("#filter-btn");

// Function to filter data
button.on("click", function() {
    // prevent the form from refreshing the page
    d3.event.preventDefault();

    //Collect date selection
    var dateInputText = d3.select("#datetime");
    console.log(dateInputText.property("value"));

    var selectedData = tableData.filter(UFOSightings => {
        return (UFOSightings.datetime === dateInputText.property("value") || !dateInputText.property("value"))

    })

    displayTable(selectedData);
    console.log("Display filtered table");

});


// clear the table for new data
function deleteTbody() {
    d3.select("tbody")
        .selectAll("tr").remove()
        .selectAll("td").remove();
};


// d3.selectAll("#filter-btn").on("click", submitClick);
d3.selectAll("#clear").on("click", deleteTbody);
// console.log("Table re-displayed");