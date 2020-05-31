# Matplotlib

Matplotlib Homework - The Power of Plots
By Raúl Flores / @raulfloresp

## Observations and Insights
Relevant observations from these challenge
* Duplicated mouse [g989] need to be excluded from the analysis to maintain consistency around the data. I decided to drop this record to enable consistency on the analysis. Number of mice to be analyzed moved to 248 mice.
* Standard Deviation and Standard Deviation Error of Mean (SEM), provide me an excellenr approach to identify the drug treamments with a greater efficiency.
* Bar plots were not quite useful to get relevant insights, however I can the insight of more extended drugs regimens: Capolumin, and Ramicane
* From the analysis of Pie representation, the sex factor is not so relevant. The difference between Male and Female are almost inexistent, and the trend goes to 50/50.
* From the Box Plot analysis, we can identify that the more effective treatments agains Tumor Volume are Capolumin and Ramicane.
* The analysis of the Line plot for Capolumin demonstrates that the treatments around Tumor volume is efficient over the time points.
* The Correlation Coefficient of 0.84 between Weight and Average Tumor Volume shows a strong relation between weith and the effectiveness of treatment.


## Summary of analysis steps executed
* Check the data for duplicate mice and remove any data associated with that mouse ID.
* Generate a summary statistics table consisting of the mean, median, variance, standard deviation, and SEM of the tumor volume for each drug regimen.
* Generate a bar plot using both Pandas’s DataFrame.plot() and Matplotlib’s pyplot that shows the number of mice per time point for each treatment regimen throughout the course of the study.
* Generate a pie plot using both Pandas’s DataFrame.plot() and Matplotlib’s pyplot that shows the distribution of female or male mice in the study.
* Calculate the final tumor volume of each mouse across four of the most promising treatment regimens: Capomulin, Ramicane, Infubinol, and Ceftamin. Calculate the quartiles and IQR and quantitatively determine if there are any potential outliers across all four treatment regimens.
* Using Matplotlib, generate a box and whisker plot of the final tumor volume for all four treatment regimens and highlight any potential outliers in the plot by changing their color and style.
* Generate a line plot of time point versus tumor volume for a single mouse treated with Capomulin.
* Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin treatment regimen.
* Calculate the correlation coefficient and linear regression model between mouse weight and average tumor volume for the Capomulin treatment. Plot the linear regression model on top of the previous scatter plot.
* Look across all previously generated figures and tables and write at least three observations or inferences that can be made from the data. Include these observations at the top of notebook.


## Built With

* [Pandas](https://www.python.org/) - The development language used
* [Python](https://pandas.pydata.org/) - Oopen source data analysis and manipulation tool
* [GitHub](https://github.com/) - The version control software and repo

## Authors

* **Raúl Flores Palacios** - *Initial work* - [raulfloresp](https://github.com/raulfloresp/databootcamp)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
