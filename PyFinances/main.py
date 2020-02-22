import os
import csv

with open('budget_data.csv','r', encoding="utf-8-sig") as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    
    profit_loss = []
    profit_loss_total = 0
    date = []
    rev_total = 0
    avg_change = 0
    change_list = []
    filename = ""
    
    for row in csvreader:
        profit_loss.append(int(row[0]))
        date.append(row[1])

    total_months = (len(date))
    rev_total = sum(profit_loss)

    for i in range(len(profit_loss)-1):
        change_total = profit_loss[i + 1] - profit_loss[i]
        avg_change = avg_change + change_total
        
        change_list.append(change_total)

    total_change = avg_change/ (len(profit_loss)-1)

    change_rounded = (round(total_change, 2))

    max_change = max(change_list)
    max_month = change_list.index(max(change_list)) + 1
    min_change = min(change_list)
    min_month = change_list.index(min(change_list)) + 1

    print("---------------------------------------------------")
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${rev_total}")
    print(f"Average Change: ${change_rounded}")
    print(f"Greatest Increase in Profits: {date[max_month]} ${max_change}")
    print(f"Greatest Decrease in Profits: {date[min_month]} ${min_change}")
    print("---------------------------------------------------")

    save_file = filename + "financial_analysis.txt"
    filepath = os.path.join(".", save_file)
    with open(filepath,"w", encoding="utf-8") as fh:
        fh.write("---------------------------------------------------\n")
        fh.write("Financial Analysis\n")
        fh.write("---------------------------------------------------\n")
        fh.write(f"Total Months: {total_months}\n")
        fh.write(f"Total: ${rev_total}\n")
        fh.write(f"Average Change: ${change_rounded}\n")
        fh.write(f"Greatest Increase in Profits: {date[max_month]} ${max_change}\n")
        fh.write(f"Greatest Decrease in Profits: {date[min_month]} ${min_change}\n")
        fh.write("---------------------------------------------------\n")