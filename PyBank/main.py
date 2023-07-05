import csv
import os

total_months=0
total_money=0
CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    
    csv_reader= csv.reader(csv_file)
    header=next(csv_reader)
    #average change
    #sum of the profit/loss changes divided by length of profit/loss changes
    #net change=profit loss for current month minus profit loss for previous month
    #profit loss changes is a list of all the net changes
    #in order to calculate net change, we need to determine previous profit loss for first month
    first_row = next(csv_reader)
    previous_profit_loss= int(first_row[1])
    total_months=1
    total_money=int(first_row[1])
    net_change_list =[]
    for row in csv_reader:
        
        total_months=total_months+1
        total_money=total_money+int(row[1])

        net_change=int(row[1])-previous_profit_loss
        net_change_list.append(net_change)
        previous_profit_loss=int(row[1])
    print(total_months)
    print(total_money)
    average_change=sum(net_change_list)/len(net_change_list)
    print(average_change)
    

