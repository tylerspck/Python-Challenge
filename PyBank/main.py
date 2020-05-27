import os
import csv

# Set path for csv file
csvpath = "/Users/specky3512/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv"

#defining names of lists to create from csv
Months_list = []
Profit_Loss_list = []

#Looping through CSV
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #defining header of csv
    csv_header = next(csvreader)

    #Loop for appending values to new lists
    for row in csvreader:
        Months_list.append(row[0])
        Profit_Loss_list.append(int(row[1]))
        total = sum(Profit_Loss_list)

    #calculation of profit/loss from month to month
    res = [(Profit_Loss_list[i] - Profit_Loss_list[i-1]) for i in range(len(Profit_Loss_list))]

#find max value from calulation
maxVal = max(res)
minVal = min(res)
maxIndex = res.index(maxVal)
minIndex = res.index(minVal)

print('text')
print('Financial Analysis')
print(f'-'*50)
print(f'Total Months: ' + str(len(Months_list)))
print(f'Total: $' + str(total))
print('Average Change: $' +
      '{: .2f}'.format(int(sum(res) - res[0])/(len(Months_list)-1)))
print('Greatest Decrease in Profits: ' +
      str(Months_list[int(minIndex)]) + ' $' + str(minVal))
print('Greatest Increase in Profits: ' +
      str(Months_list[int(maxIndex)]) + ' $' + str(maxVal))

import sys
output_path = os.path.join(
    "/Users/specky3512/GitHub/Python-Challenge/PyBank/analysis", 'Financial_Analysis.txt')
file = open(output_path, 'a')
sys.stdout = file

#Print out of found values
print('text')
print('Financial Analysis')
print(f'-'*50)
print(f'Total Months: ' + str(len(Months_list)))
print(f'Total: $' + str(total))
print('Average Change: $' + '{: .2f}'.format(int(sum(res) - res[0])/(len(Months_list)-1)))
print('Greatest Decrease in Profits: ' + str(Months_list[int(minIndex)]) + ' $' + str(minVal))
print('Greatest Increase in Profits: ' + str(Months_list[int(maxIndex)]) + ' $' + str(maxVal))

file.close()


