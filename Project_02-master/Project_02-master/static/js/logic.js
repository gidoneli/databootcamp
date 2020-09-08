// Creating map object

var dropDownList1 = d3.select("#selDataset1");
var dropDownList2 = d3.select("#selDataset2");
var dropDownList3 = d3.select("#selDataset3");
var dropDownList4 = d3.select("#selDataset4");


var myMap = L.map('map').setView([37.8, -96], 4);

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/outdoors-v11",
    accessToken: API_KEY
}).addTo(myMap);


var geo_url = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json";

function graph(url, country) {
    var geojson;
    d3.json(geo_url, function(geoData) {
        d3.json(url, function(error, stateInfo) {

            var toCycle = geoData.features
            var stateInfo2 = stateInfo.data

            toCycle.forEach(function(data) {
                var stateGeo = data.properties;
                var stateGeoName = stateGeo.name;

                for (var i = 0; i < stateInfo2.length; i++) {
                    var stateI = stateInfo2[i]
                    var stateName = stateI.state
                    var keysInfo = Object.keys(stateI)

                    if (stateName == stateGeoName) {
                        for (var j = 0; j < keysInfo.length; j++) {
                            var label = keysInfo[j]
                            stateGeo[label] = stateI[label]
                        }
                    }
                }

            });

            var data = geoData;

            geojson = L.choropleth(data, {

                valueProperty: function(feature) {
                    return feature.properties.variable
                },
                scale: ["#ffffb2", "#b10026"],
                steps: 7,
                mode: 'e',
                style: {
                    // Border color
                    color: "#fff",
                    weight: 1,
                    fillOpacity: 0.8
                },

                onEachFeature: function(feature, layer) {
                    layer.bindPopup(`State: ${feature.properties.name}<br>
                    ${country.toUpperCase()} Population: ${parseFloat(feature.properties.variable / 1000)}k<br>
                    Foreign Population:<br>Age:${parseFloat(feature.properties.age * 100).toFixed(2)}%<br>
                    Income:${parseFloat(feature.properties.income *100).toFixed(2)}%<br>
                    Citizen:${parseFloat(feature.properties.status * 100).toFixed(2)}%<br>
                    Male:${parseFloat(feature.properties.sex * 100).toFixed(2)}%<br>
                    Education:${parseFloat(feature.properties.education * 100).toFixed(2)}%`);

                }
            }).addTo(myMap)



            var legend = L.control({ position: "bottomright" });
            legend.onAdd = function() {
                d3.select(".legend").remove();
                var div = L.DomUtil.create("div", "info legend");
                var limits = geojson.options.limits;
                var colors = geojson.options.colors;
                console.log(colors)
                var labels = [];

                // // Add min & max
                var legendInfo = `<h5>Population of <br>${country.toUpperCase()} </h5>`
                div.innerHTML = legendInfo;
                for (var i = 0; i < limits.length; i++) {
                    div.innerHTML +=
                        '<i style="background:' + colors[i] + '"></i> ' + parseFloat(limits[i] / 1000).toFixed(0) + 'k<br>'
                };
                return div;
            };

            // Adding legend to the map
            legend.addTo(myMap);
        });
    });

};

function init() {
    var age = "+25";
    var country = "mexico";
    var income = "+50000";
    var education = "highschool";

    url = "http://127.0.0.1:5000/map/" + country + "/" + age + "/" + education + "/" + income;

    var countries = ['Caribbean', 'Bahamas', 'Barbados', 'Cuba', 'Dominica', 'Dominican Republic', 'Grenada',
        'Haiti', 'Jamaica', 'St Vincent and the Grenadines', 'Trinidad and Tobago', 'West Indies',
        'Other Caribbean', 'Central America', 'Mexico', 'Belize', 'Costa Rica', 'El Salvador',
        'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Other Central America', 'South America', 'Argentina', 'Bolivia',
        'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Peru', 'Uruguay', 'Venezuela', 'Other South America'
    ];

    var edad = ['<5', '<18', '<25', '<35', '<45', '<55', '<60', '<65', '<75', '+75'];

    var incomes = ['<10000', '<15000', '<25000', '<35000', '<50000', '<65000',
        '<75000', '+75000'
    ];

    var educations = ['School', 'High School', 'College', 'Bachelor', 'Graduate'];

    var options = dropDownList1.selectAll("option")
        .data(countries)
        .enter()
        .append("option")
        .text(function(d) { return d })
        .attr("value", function(d) { return d });

    var options2 = dropDownList2.selectAll("option")
        .data(edad)
        .enter()
        .append("option")
        .text(function(d) { return d })
        .attr("value", function(d) { return d });

    var options3 = dropDownList3.selectAll("option")
        .data(educations)
        .enter()
        .append("option")
        .text(function(d) { return d })
        .attr("value", function(d) { return d });

    var options4 = dropDownList4.selectAll("option")
        .data(incomes)
        .enter()
        .append("option")
        .text(function(d) { return d })
        .attr("value", function(d) { return d });


    graph(url, country)
};

d3.selectAll("#selDataset1").on("change", updateMap)
d3.selectAll("#selDataset2").on("change", updateMap)
d3.selectAll("#selDataset3").on("change", updateMap)
d3.selectAll("#selDataset4").on("change", updateMap)

function updateMap() {
    var dropDownList1 = d3.select("#selDataset1");
    var dropDownList2 = d3.select("#selDataset2");
    var dropDownList3 = d3.select("#selDataset3");
    var dropDownList4 = d3.select("#selDataset4");

    country = dropDownList1.property("value");
    age = dropDownList2.property("value");
    education = dropDownList3.property("value");
    income = dropDownList4.property("value");

    url = "http://127.0.0.1:5000/map/" + country + "/" + age + "/" + education + "/" + income;

    graph(url, country)
};

init()