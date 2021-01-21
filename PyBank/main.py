import os
import csv

# path to collect data from resources folder
bank_csv = os.path.join(r'C:\Users\kyucz\Desktop\UPenn Data & Visualization\Python-Challenge\PyBank\Resources\budget_data.csv')

# determine variables
total_months = 0
net_total = 0
m = 0
greatest_increase = 0
greatest_decrease = 0
best_month = ''
worst_month = ''

# variable lists
date = []
profit = []
monthly_changes = []

# open and read csv
with open(bank_csv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # skips header
    next(reader, None)

    # Loop over each row of data
    for row in reader:
        # calculate total number of months
        total_months += 1
        date.append(row[0])
        # calculate total net profit and 
        net_total += int(row[1])
        # track changes in profits/losses over entire period
        profit.append(int(row[1]))

# Loop through each month's data
for m in range(len(profit)-1):
    # calculate monthly change and append to list
    change = profit[m] - profit[m-1]
    monthly_changes.append(change)
        
# get average of these changes
avg_change = round(sum(monthly_changes)/(len(monthly_changes)), 2)

# determine greatest increase in profits
greatest_increase = max(monthly_changes)
best_month = monthly_changes.index(greatest_increase)

# determine greatest decrease in losses
greatest_decrease = min(monthly_changes)
worst_month = monthly_changes.index(greatest_decrease)

# print report
# create new variable using f-strings for formatting to easily create txt document
FinancialAnalysis = (
f"Financial Analysis \n"
f"---------------------- \n"
f"Total Months:  {total_months} \n"
f"Net Total: $ {net_total} \n"
f"Average Change: $ {avg_change} \n"
f"Greatest Increase in Profits: {date[best_month]}, (${greatest_increase}) \n"
f"Greatest Decrease in Profits: {date[worst_month]}, (${greatest_decrease}) \n")
print(FinancialAnalysis)

# create text file
PyBankResults = open("PyBankResults.txt",'w')
PyBankResults.write(FinancialAnalysis)
PyBankResults.close()
