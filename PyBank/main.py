import os
import csv

csvpath = "/Users/specky3512/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv"

Months_list = []
Profit_Loss_list = []
Monthly_difference =[]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:
        Months_list.append(row[0])
        Profit_Loss_list.append(int(row[1]))
        total = sum(Profit_Loss_list)
        Monthly_difference.append = (Profit_Loss_list)
       
        
    for i < len(int(Profit_Loss_list)):
        Monthly_difference.append = (Profit_Loss_list[i] - Profit_Loss_list[i -1]


maxVal = max(Profit_Loss_list)
minVal = min(Profit_Loss_list)

        

    # print(Months_list)
    #print(Profit_Loss_list)
    #Delta_Profit = sum(Profit_Loss_list)
   
    
print(f'Total Months: ' + str(len(Months_list)))
print(f'Total: $' + str(total))
#print((Delta_Profit))
print(minVal)
print(maxVal)




