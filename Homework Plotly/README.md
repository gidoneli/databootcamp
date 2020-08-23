# Plot.ly Homework - Belly Button Biodiversity
## Date: Agosto 2020
### By Raúl Flores Palacios

## INTRODUCTION 
Interactive dashboard to explore the Belly Button Biodiversity dataset, which catalogs the microbes that colonize human navels.
The dataset reveals that a small handful of microbial species (also called operational taxonomic units, or OTUs, in the study) were present in more than 70% of people, while the rest were relatively rare.


## Step 1: Plotly Bar Chart and Bubble Chart
* Use the D3 library to read in samples.json.
* Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
* Use sample_values as the values for the bar chart.
* Use otu_ids as the labels for the bar chart.
* Use otu_labels as the hovertext for the chart.


## Step 1: Plotly Bubble Chart
* Create a bubble chart that displays each sample.
* Use otu_ids for the x values.
* Use sample_values for the y values.
* Use sample_values for the marker size.
* Use otu_ids for the marker colors.
* Use otu_labels for the text values.
* Display the sample metadata, i.e., an individual’s demographic information.
* Display each key-value pair from the metadata JSON object somewhere on the page.
* Update all of the plots any time that a new sample is selected.


## Advanced Challenge Assignment (Optional)
* Adapt the Gauge Chart from https://plot.ly/javascript/gauge-charts/ to plot the weekly washing frequency of the individual.
* You will need to modify the example gauge code to account for values ranging from 0 through 9.
* Update the chart whenever a new sample is selected.



## Final Result
* The link to the page is located here:

https://github.com/raulfloresp/databootcamp/tree/master/javascript-challenge/UFO-level-2


The final webpage look is illustrated here:

![alt text](https://github.com/raulfloresp/databootcamp/blob/master/Homework%20Plotly/images/index.jpg?raw=true)



## Built With

* [Plotly](https://plotly.com/) - Chart Library
* [Visual Studio Code](https://code.visualstudio.com/) - Source Code Editor
* [GitHub](https://github.com/) - The version control software and repo
* [Bootstrap](https://getbootstrap.com/) - Javascript Framework



## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
