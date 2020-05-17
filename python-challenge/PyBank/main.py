#PyBank Analysis

#Import relevant modules
import os
import csv

#os.path.join() method in Python join one or more path components intelligently.
csvpath = os.path.join("Resources", "budget_data.csv")

#We opened the file in read mode and then passed the file object to csv.reader() function.
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    #Create empty lists. An empty list is assigned to a variable, then add the csv values to the list
    number_of_months = []
    profit = []
    Profit_Variation = []

    #For every row in the CSV, get the values and add them to the created lists above.
    #We use the append() method in python to add a single item to the existing list.
    #Reference: (https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737)
    for row in csvreader:
        number_of_months.append(row[0])
        profit.append(int(row[1]))
    
    #For every rwo in Profit List, and using the Range function to perform an action for a specific number of times
    #Use Len funcion. The len() function returns the number of items in an object.
    #Reference: https://docs.python.org/3.4/library/csv.html?highlight=csv
    #Reference: https://www.w3schools.com/python/ref_func_len.asp
    for i in range(len(profit)-1):
        Profit_Variation.append(profit[i+1]-profit[i])
                      
# Get the minimum and maximum values on the List Profit_Variation, using Min and Max functions
# Max function: This function is used to compute the maximum of the values passed in its argument
# Min function: This function is used to compute the minimum of the values passed in its argument
profit_increase = max(Profit_Variation)
profit_decrease = min(Profit_Variation)

#using the index() method to search an element in the list and to return its index.
month_profit_increase = Profit_Variation.index(max(Profit_Variation))+1
month_profit_decrease = Profit_Variation.index(min(Profit_Variation))+1

#Script prints the analysis to the terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(number_of_months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(Profit_Variation)/len(Profit_Variation),2)}")
print(f"Greatest Increase in Profits: {number_of_months[month_profit_increase]} (${(str(profit_increase))})")
print(f"Greatest Decrease in Profits: {number_of_months[month_profit_decrease]} (${(str(profit_decrease))})")      

#Script writes the analysis to an output text file
output_file = os.path.join("Analysis", "output_file.txt")
with open(output_file,"w") as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Months:{len(number_of_months)}")
    text_file.write("\n")
    text_file.write(f"Total: ${sum(profit)}")
    text_file.write("\n")
    text_file.write(f"Average Change: ${round(sum(Profit_Variation)/len(Profit_Variation),2)}")
    text_file.write("\n")
    text_file.write(f"Greatest Increase in Profits: {number_of_months[month_profit_increase]} (${(str(profit_increase))})")
    text_file.write("\n")
    text_file.write(f"Greatest Decrease in Profits: {number_of_months[month_profit_decrease]} (${(str(profit_decrease))})")

#End of coding