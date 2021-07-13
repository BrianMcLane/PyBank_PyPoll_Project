import csv
import os

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(pybank_csv,"r") as PyBank:
    pybank_reader = csv.reader(PyBank)

    next(pybank_reader)

    # for bottle in pybank_reader:
    #     print(bottle)

    # Total Months & Net Profit Amount
    # # Calculate the Change (then Average)
    month_count = 0
    net_profit = 0
    temp = 0
    change_list = list()
    change_row = 0
    for row in list(pybank_reader):
        month_count = month_count + 1
        net_profit = net_profit + int(row[1])
        if change_row == 0:
            temp = int(row[1])
        else:
            change_list.append(int(row[1]) - temp)
            temp = int(row[1])
        change_row = change_row + 1 
    
    print(month_count)
    print(net_profit)
    print(round(sum(change_list) / len(change_list), 2))
    print(max(change_list))
    print(min(change_list))
    