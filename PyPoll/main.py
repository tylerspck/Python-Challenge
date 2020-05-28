import os
import csv

csvpath = "/Users/specky3512/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

Voter_ID = []
Candidate = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #defining header of csv
    csv_header = next(csvreader)
    
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
    
Canidate_Count = dict((x,Candidate.count(x))for x in set(Candidate))
Khan_Votes = f'{Canidate_Count["Khan"]}'
Correy_Votes = f'{Canidate_Count["Correy"]}'
Li_Votes = f'{Canidate_Count["Li"]}'
Tooley_Votes = f'{Canidate_Count["O'Tooley"]}'
# total_votes = len(Voter_ID)
# print('text')
# print('Election Results')
# print('-' * 50)
# print('Total Votes: ' + str(len(Voter_ID)))
# print('-' * 50)
# print('Khan: ' + str("{0:.3%}".format(int(Khan_Votes)/int(total_votes))) + ' (' + Khan_Votes + ')')
# print('Correy: ' + str("{0:.3%}".format(int(Correy_Votes)/int(total_votes))) + ' (' + Correy_Votes + ')')
# print('Li: ' + str("{0:.3%}".format(int(Li_Votes)/int(total_votes))) + ' (' + Li_Votes + ')')
# # print("O'Tooley: " + str("{0:.2%}".format(int(Tooley_Votes)/int(total_votes))) + ' (' + Tooley_Votes + ')')
# print('-' * 50)
print(f'{Canidate_Count["O'Tooley"]}')
# print('-' * 50)

# maxVal = max(Canidate_Count[])
print(maxVal)
