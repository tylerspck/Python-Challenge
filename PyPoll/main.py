import sys
import os
import csv

#CSV location
csvpath = "/Users/specky3512/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

#Defining new lists
Voter_ID = []
Candidate = []

#Looping through the CSV file
with open(csvpath) as csvfile:

    #reading CSV and specifing where to break data
    csvreader = csv.reader(csvfile, delimiter=",")
    #defining header of csv
    csv_header = next(csvreader)
    
    #Creating new seperate lists
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
    
#Defining and Creating dictionary for number of votes each Candidate received
Canidate_Count = dict((x,Candidate.count(x))for x in set(Candidate))

#Total number of votes
total_votes = len(Voter_ID)
#looking up max value in the dict and deslaying the key
Winner = max(Canidate_Count,key=Canidate_Count.get)

#Displaying results in Terminal 
print('text')
print('Election Results')
print('-' * 50)
print('Total Votes: ' + str(len(Voter_ID)))
print('-' * 50)
#Looping through the dictionary and displaying each dict Key, calculating the percent vs total votes, and displaying the corrisponding value
for key in Canidate_Count:
    print(key + ': ' + str("{0:.3%}".format(Canidate_Count[key]/total_votes)) + '(' + str(Canidate_Count[key]) + ')')
print('-' * 50)
print('Winner: ' + Winner)
print('-' * 50)

#Writing txt file
output_path = os.path.join(
    "/Users/specky3512/GitHub/Python-Challenge/PyPoll/analysis", 'Election_Results.txt')
file = open(output_path, 'w')
sys.stdout = file

print('text')
print('Election Results')
print('-' * 50)
print('Total Votes: ' + str(len(Voter_ID)))
print('-' * 50)
for key in Canidate_Count:
    print(key + ': ' + str("{0:.3%}".format(Canidate_Count[key]/total_votes)) + '(' + str(Canidate_Count[key]) + ')')
print('-' * 50)
print('Winner: ' + Winner)
print('-' * 50)

file.close()