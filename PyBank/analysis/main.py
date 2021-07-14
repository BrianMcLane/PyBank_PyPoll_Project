import csv
import os

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(pybank_csv,"r") as PyBank:
    pybank_reader = csv.reader(PyBank)
    
    next(pybank_reader) # Skips the first row i.e. the header row

    month_count = 0
    net_profit = 0
    temp = 0
    change_list = list()
    change_row = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in pybank_reader:
        month_count = month_count + 1
        net_profit = net_profit + int(row[1])
        
        if change_row == 0:  # Finding difference between each month
            temp = int(row[1])
            diff = 0
        else:
            diff = int(row[1]) - temp
            change_list.append(diff)
            temp = int(row[1])
            # print(row[0], diff) # Check your code output

        if diff >= greatest_increase:
            greatest_increase = diff
            greatest_increase_month = row[0] # month with greatest increase

        elif diff <= greatest_decrease:
            greatest_decrease = diff
            greatest_decrease_month = row[0] # month with greatest decrease 

        change_row = change_row + 1

    average_change = round(sum(change_list) / len(change_list), 2) # Finding average change between months

results = (f" Financial Analysis \n -------------------- \n Total Months : {month_count} \n Total : {net_profit} \n Averger Change : {average_change} \n Greatest Increase in Profit : {greatest_increase_month} ({greatest_increase}) \n Greatest Decrease in Profit : {greatest_decrease_month} ({greatest_decrease})")
print(results)

output_path = os.path.join("election_analysis.txt")
with open(output_path, "w") as final:
    final.write(str(results)) 