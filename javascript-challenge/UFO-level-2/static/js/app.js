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
    var dateValueText = d3.select("#datetime");
    var cityValueText = d3.select("#city");
    var stateValueText = d3.select("#state");
    var countryValueText = d3.select("#country");
    var shapeValueText = d3.select("#shape");


    var selectedData = tableData.filter(UFOSightings => {
        return (UFOSightings.datetime === dateValueText.property("value") || !dateValueText.property("value")) &&
            (UFOSightings.city === cityValueText.property("value") || !cityValueText.property("value")) &&
            (UFOSightings.state === stateValueText.property("value") || !stateValueText.property("value")) &&
            (UFOSightings.country === countryValueText.property("value") || !countryValueText.property("value")) &&
            (UFOSightings.shape === shapeValueText.property("value") || !shapeValueText.property("value"))
    })

    displayTable(selectedData);
    console.log("Display filtered table");
    console.log(dateValueText.property("value"));

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