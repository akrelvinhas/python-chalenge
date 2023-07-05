import csv
import os
# Read budget data from CSV
CSV_PATH = os.path.join("Resources", "budget_data.csv")
budgetoutput= os.path.join("analysis", "pybudgetanalysis.txt")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    
    csv_reader= csv.reader(csv_file)
    header=next(csv_reader)

    months = []
    profit_losses = []
    changes = []

    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate total months
total_months = len(months)

# Calculate net total of profit/loss
net_total = sum(profit_losses)

# Calculate change in profit/loss, store them in list
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open(budgetoutput, mode="wt") as f:
    f.write("Financial Analysis")
    f.write("-----------------------------")
    f.write(f"Total Months: {total_months}")
    f.write(f"Total: ${net_total}")
    f.write(f"Average Change: ${average_change:.2f}")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")