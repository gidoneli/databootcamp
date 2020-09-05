// The code for the chart is wrapped inside a function that
// automatically resizes the chart
function makeResponsive() {

    // if the SVG area isn't empty when the browser loads,
    // remove it and replace it with a resized version of the chart
    var svgArea = d3.select("#scatter").select("svg");

    if (!svgArea.empty()) {
        svgArea.remove();
    }

    //SVG WRAPPER
    // SVG wrapper dimensions are determined by the current width and
    // height of the browser window.
    var svgWidth = window.innerWidth;
    var svgHeight = window.innerHeight;

    //Set margins
    var margin = {
        top: 30,
        bottom: 200,
        left: 30,
        right: 300
    };

    //Scatter height and width linked to window height and width from svgWidth/svgHeight linked to window width/height.
    var scatterHeight = svgHeight - margin.top - margin.bottom;
    var scatterWidth = svgWidth - margin.left - margin.right;


    //APPEND SVG ELEMENT
    //Refer to into index.html: id="scatter" and height/width based on the window height/width.
    var svg = d3
        .select("#scatter")
        .append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth);

    //Append group element "g" to the svg element
    //Transform to place "g" element in the svg canvas.
    var chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    //READ CSV AND EXTRACT DATA
    d3.csv("assets/data/data.csv").then(function(UsaCensusData) {
        console.log(UsaCensusData);

        //PARSE DATA
        //Extract from Data file variables
        UsaCensusData.forEach(function(data) {
            data.poverty = +data.poverty;
            data.povertyMoe = +data.povertyMoe;
            data.age = +data.age;
            data.ageMoe = +data.ageMoe;
            data.income = +data.income;
            data.incomeMoe = +data.incomeMoe;
            data.healthcare = +data.healthcare;
            data.healthcareLow = +data.healthcareLow;
            data.healthcareHigh = +data.healthcareHigh;
            data.obesity = +data.obesity;
            data.obesityLow = +data.obesityLow;
            data.obesityHigh = +data.obesityHigh;
            data.smokes = +data.smokes;
            data.smokesLow = +data.smokesLow;
            data.smokesHigh = +data.smokesHigh;
        });

        //CREATE SCALES FUNCTIONS: age as independent variable "X" axis, and smokes as dependent variable "Y" axis
        //age scale on X axis
        var xLinearScale = d3.scaleLinear()
            .domain([d3.min(UsaCensusData, d => d.age) - 1, d3.max(UsaCensusData, d => d.age) + 1])
            .range([0, scatterWidth]);

        //smokes scale on Y axis
        var yLinearScale = d3.scaleLinear()
            .domain([d3.min(UsaCensusData, d => d.smokes) - 1, d3.max(UsaCensusData, d => d.smokes) + 1])
            .range([scatterHeight, 0]);


        //CREATE AXES
        var xAxis = d3.axisBottom(xLinearScale);
        var yAxis = d3.axisLeft(yLinearScale);

        //APPEND AXES
        chartGroup.append("g")
            .attr("transform", `translate(0, ${scatterHeight})`)
            .call(xAxis);

        chartGroup.append("g")
            .call(yAxis);

        //Establish a color scale for plotting poverty data by color on the graph.
        var colorScale = d3.scaleLinear()
            .domain([d3.min(UsaCensusData, d => d.poverty), d3.mean(UsaCensusData, d => d.poverty), d3.max(UsaCensusData, d => d.poverty)])
            .range(["yellow", "orange", "blue"]);

        //CREATE TOOLTIP
        //I have used this tips tool: https://github.com/VACLab/d3-tip
        //Initializes the tooltip
        var tool_tip = d3.tip()
            .attr("class", "d3-tip")
            .offset([0, 50])
            .html(function(d) { return `${d.state}<hr>Income: $${d.income}<hr>Obesity: ${d.obesity}, Age: ${d.age}` });

        //Calls tooltip
        svg.call(tool_tip);


        //CREATE CIRCLES FOR PLOTTING
        //Create "mouseover" event listener to display tooltip
        var circleGroup = chartGroup.selectAll("circle")
            .data(UsaCensusData)
            .enter()

        circleGroup
            .append("circle")
            .attr("class", "circle")
            .attr("cx", d => xLinearScale(d.age))
            .attr("cy", d => yLinearScale(d.smokes))
            .attr("r", d => ((d.healthcare * d.healthcare) / 11))
            .attr("fill", function(d) { return colorScale(d.poverty); })
            .attr("opacity", "0.8")
            .style("stroke", "white")

        //CREATE LABELS USING ABBREVIATIONS
        circleGroup
            .append("text")
            .text(function(d) {
                return d.abbr;
            })
            .attr("x", d => xLinearScale(d.age) - 10)
            .attr("y", d => yLinearScale(d.smokes) + 10)

        .on("click", tool_tip.show)
            .on("mouseout", tool_tip.hide)

        //Create Axes Labels
        //Y axis label
        chartGroup.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left + 10)
            .attr("x", 0 - (scatterHeight / 2))
            .attr("class", "axisText")
            .text("smokers index");

        //X axis label
        chartGroup.append("text")
            .attr("y", scatterHeight + margin.top + 5)
            .attr("x", scatterWidth / 2)
            .attr("class", "axisText")
            .text("age index");


    });

};

//call makeResponsive when page loads
makeResponsive();

//call makeResponsive when page is resized
d3.select(window).on("resize", makeResponsive);