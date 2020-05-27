import os
import csv

csvpath = "/Users/specky3512/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

Voter_ID = []
County = []
Candidate = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #defining header of csv
    csv_header = next(csvreader)
    
    for row in csvreader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    
print('text')
print('Election Results')
print('-' * 50)
print('Total Votes: ' + str(len(Voter_ID)))
print('-' * 50)

dict((x,Candidate.count(x))for x in set(Candidate))

# [[x, l.count(x)] for x in set(l)]
# [['a', 1], ['b', 2]]
# >> > dict((x, l.count(x)) for x in set(l))
# {'a': 1, 'b': 2}
print(dict((x, Candidate.count(x))for x in set(Candidate)))
