// Initializes the page with a default plot
function init() {
    // Select the dropdown element from the dataset
    var dropdown = d3.select("#selDataset");

    //Dropdown data from subject ID's on the JSON dataset
    d3.json("static/data/samples.json").then((data) => {
        //select the names value and assign them to the IDs
        console.log(data);
        var IDs = data.names;
        IDs.forEach((id) => {
            dropdown
                .append("option") //add an option to the HTML menu
                .text(id)
                //Populate to the value option
                .property("value", id);
        });
        console.log(IDs);
        // Initial plotting
        const defaultPlot = IDs[0];
        console.log(IDs[0]);
        updatePlots(defaultPlot);
        refreshMetadata(defaultPlot);
    });
}


function refreshMetadata(sample) {
    //read the json data file
    d3.json("static/data/samples.json").then((data) => {
        var metadata = data.metadata;
        console.log(metadata); //print metadata
        var demographicInfo = metadata.filter(sampleItem => sampleItem.id == sample);
        console.log(demographicInfo); //print demographic info of the item in the table
        var result = demographicInfo[0];
        var sampleMetadata = d3.select("#sample-metadata");
        sampleMetadata.html("");
        Object.entries(result).forEach(([key, value]) => {
            sampleMetadata.append("h5").text(`${key.toUpperCase()}: ${value}`)
        })
        console.log(sampleMetadata); //print the values of sample metadata

        var trace3 = [{
            domain: { x: [0, 1], y: [0, 1] },
            type: "indicator",
            mode: "gauge+number",
            value: result.wfreq,
            title: { text: "Belly Button Washes Frequency" },
            gauge: {
                axis: { range: [0, 9], tickwidth: 0.5, tickcolor: "black" },
                bar: { color: "#669999" },
                bgcolor: "white",
                borderwidth: 2,
                bordercolor: "transparent",
                steps: [
                    { range: [0, 1], color: "#dff3f9" },
                    { range: [1, 2], color: "#caecf5" },
                    { range: [2, 3], color: "#b6e5f2" },
                    { range: [3, 4], color: "#a1ddee" },
                    { range: [4, 5], color: "#8cd6ea" },
                    { range: [5, 6], color: "#70cce5" },
                    { range: [6, 7], color: "#32b5da" },
                    { range: [7, 8], color: "#229fc2" },
                    { range: [8, 9], color: "#1d88a6" }

                ],
            }
        }];

        gaugeData = trace3;
        console.log(result.wfreq);

        var layout = {
            width: 450,
            height: 400,
            margin: { t: 25, r: 25, l: 25, b: 25 },
            paper_bgcolor: "lavender",
            font: { color: "darkblue", family: "Arial" }
        };

        Plotly.newPlot("gauge", gaugeData, layout);
    });
}

function updatePlots(sample) {
    d3.json("static/data/samples.json").then((data) => {
        var samples = data.samples;
        var demographicInfo = samples.filter(sampleItem => sampleItem.id == sample);
        var result = demographicInfo[0];
        var sample_values = result.sample_values;
        var otu_ids = result.otu_ids;
        console.log(otu_ids);
        var otu_labels = result.otu_labels;
        console.log(otu_labels);

        // Bubble Chart
        var trace1 = {
            x: otu_ids,
            y: sample_values,
            text: otu_labels,
            mode: 'markers',
            marker: {
                size: sample_values,
                color: otu_ids,
                colorscale: "Pastel" //Color scale https://plotly.com/python/discrete-color/
            }
        };
        var data = [trace1];
        var layout = {
            title: 'Sample of Bacteria Elements',
            showlegend: false,
            hovermode: 'closest',
            xaxis: { title: "Operational Taxonomic Units - OTU ID " + sample },
            margin: { t: 30 }
        };
        Plotly.newPlot('bubble', data, layout);

        // Bar Chart
        var trace1 = {
            x: sample_values.slice(0, 10).reverse(),
            y: otu_ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
            text: otu_labels.slice(0, 10).reverse(),
            name: "",
            type: "bar",
            orientation: "h",
            marker: {
                color: 'rgb(142,124,195)'
            }
        };
        var data = [trace1];

        var layout = {
            title: "Top 10 OTUs found in individual: " + sample,
            margin: {
                l: 75,
                r: 75,
                t: 75,
                b: 50
            },
            font: {
                family: 'Raleway, sans-serif'
            },
            showlegend: false,
            xaxis: {
                tickangle: -45
            },
            yaxis: {
                zeroline: false,
                gridwidth: 2
            },
            bargap: 0.05
        };

        Plotly.newPlot("bar", data, layout);
    });
}


function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    updatePlots(newSample);
    console.log(newSample);
    refreshMetadata(newSample);
    console.log(newSample);
}

// Initialize the dashboard
init();