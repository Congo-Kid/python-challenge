#import modules
import os
import csv


# create file path and save as file
file = os.path.join('budget_data.csv')

#create empty lists for month and revenue data
months = []
revenue = []

#read csv and put data into lists
#revenue list will be list of integers
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#calculate total months
total_months = len(months)

#list variables for greatest increase, decrease and total revenue. 
#These should be first entry for revenue before the loop starts
#set total revenue = 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#initiate loop to find greatest increase and decrease,
#add each revenue figure to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    #short cut for equation total_rev=total_rev+ revenue[r]
    total_revenue += revenue[r]

#calculate average_change
average_delta = round(total_revenue/total_months, 2)

#generate path for output txt file
output_file = os.path.join('pybank_output.txt')

# opens the output destination in write mode and prints the summary
with open(output_file, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_delta) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())