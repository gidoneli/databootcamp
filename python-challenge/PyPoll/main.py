#PyPoll Analysys

#Import relevant modules
import os
import csv

#os.path.join() method in Python join one or more path components intelligently.
csvpath = os.path.join("Resources", "election_data.csv")

#Create an empty dictionary. Dictionary will be used for candidate name and vote count.
#Initialize variable of Total Votes for counting
poll_dictionary = {}
Total_Votes = 0

#Create additional lists for candidates, number of votes, percentage of votes, and winners
#list for candidates names
candidates = []
#list for number of votes
number_of_votes = []
#list for percentage of votes
percentage_votes = []
#list for candidate results
candidates_results = []

#We opened the file in read mode and then passed the file object to csv.reader() function.
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #Return the next item from the iteration, and skiping the header line
    #Default value to return if the iteration has reached to its end = "None"
    next(csvreader, None)

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    #Reference (https://www.tutorialspoint.com/python/python_dictionary.htm)
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        #Iteration in dictionary keys
        #Counting votes for each candidate and add values to the dictionary keys
        if row[2] in poll_dictionary.keys():
            poll_dictionary[row[2]] = poll_dictionary[row[2]] + 1
        else:
            poll_dictionary[row[2]] = 1
 
# Use function dictionary.items to return a list of dictionary (key, value) tuple pairs
# Adds values to candidates and number_of_votes to lists created above
for key, value in poll_dictionary.items():
    candidates.append(key)
    number_of_votes.append(value)

#Using a loop in the number of votes list to update
#Using a loop we execute an addition (append) to the percentage of votes list, one for each item in the list.
#Calculate the percentage value and rounding the value
for j in number_of_votes:
    percentage_votes.append(round(j/Total_Votes*100, 1))

#Create a list object for the summarized data coming from a container zipped with summarized data.
#Reference: (https://www.journaldev.com/15891/python-zip-function)
#Reference: (https://www.w3schools.com/python/ref_func_list.asp)
#Zips summirized data number_of_votes, percentage_votes into tuples
summarized_values = list(zip(candidates, number_of_votes, percentage_votes))

for candidate_name in summarized_values:
    if max(number_of_votes) == candidate_name[1]:
        candidates_results.append(candidate_name[0])

#Obtain the first value of the list of candidate results in order to get the winner.
winner_candidate = candidates_results[0]

#Use Len funcion. The len() function returns the number of items in an object.
#only runs if there is a tie and puts additional winners into a string separated by commas
if len(candidates_results) > 1:
    for k in range(1, len(candidates_results)):
        winner_candidate = winner_candidate + ", " + candidates_results[k]

#Calculate individual percentages and format numbers using str.format() method
#Reference(https://kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python)
percentage_one = "{:.3%}".format((summarized_values[0][2])/100)
percentage_two = "{:.3%}".format((summarized_values[1][2])/100)
percentage_three = "{:.3%}".format((summarized_values[2][2])/100)
percentage_four = "{:.3%}".format((summarized_values[3][2])/100)

#Script prints the analysis to the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: "+ str(Total_Votes))
print("------------------------")
print(summarized_values[0][0] + ": " + percentage_one + " (" + str(summarized_values[0][1]) + ")" )
print(summarized_values[1][0] + ": " + percentage_two + " (" + str(summarized_values[1][1]) + ")" )
print(summarized_values[2][0] + ": " + percentage_three + " (" + str(summarized_values[2][1]) + ")" )
print(summarized_values[3][0] + ": " + percentage_four + " (" + str(summarized_values[3][1]) + ")" )
print("------------------------")
print("Winner: " + winner_candidate)
print("------------------------")

#Script writes the analysis to an output text file
output_file = os.path.join("Analysis", "output_file.txt")
with open(output_file,"w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Votes: "+ str(Total_Votes))
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(summarized_values[0][0] + ": " + percentage_one + " (" + str(summarized_values[0][1]) + ")" )
    text_file.write("\n")
    text_file.write(summarized_values[1][0] + ": " + percentage_two + " (" + str(summarized_values[1][1]) + ")" )
    text_file.write("\n")
    text_file.write(summarized_values[2][0] + ": " + percentage_three + " (" + str(summarized_values[2][1]) + ")" )
    text_file.write("\n")
    text_file.write(summarized_values[3][0] + ": " + percentage_four + " (" + str(summarized_values[3][1]) + ")" )
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + winner_candidate)
    text_file.write("\n")
    text_file.write("------------------------")

#End of coding