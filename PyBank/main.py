
import pathlib
import csv


# setup working directory and data file path
working_dir = pathlib.Path.cwd()
data_path = working_dir / "resources" / "budget_data.csv"


# open and read file 
file = data_path.open(mode="r", encoding="utf-8")
reader = csv.reader(file)

# parse data and save elements in lists
row_counter = 1
dates = []
profit_loss = []
for row in reader:
    # store header row in header
    if row_counter == 1:
        
        header = row

    # store data in dates and profit/loss data in lists    
    else:
        dates.append(row[0])
        profit_loss.append(float(row[1]))

    row_counter += 1

# calculate the number of months
numMonths = len(dates)

# calculate the difference in profits/loss per month & total profit/loss
total_profit_loss = 0
last_month_profit_loss = profit_loss[:-1]
last_month_profit_loss.insert(0, 0)

monthly_diff = []
for month in range(numMonths):
    total_profit_loss += profit_loss[month]
    diff = profit_loss[month] - last_month_profit_loss[month]
    monthly_diff.append(diff)

# need to set the first month difference to 0 as we don't have the previous months info
monthly_diff[0] = 0

# calculate changes in profit
total_change_in_profit_loss = 0
for month in range(numMonths):
    total_change_in_profit_loss += monthly_diff[month]

# calculate the average change in profit/loss   
avg_change_profit_loss = total_change_in_profit_loss / (numMonths-1)

# calculate which month and quantity of the greatest increase in profit
max_profit_index = monthly_diff.index(max(monthly_diff))
max_profit_month = dates[max_profit_index]
max_profit_amt = monthly_diff[max_profit_index]

# calculate which month and quantity of the greatest decrease in profit
min_profit_index = monthly_diff.index(min(monthly_diff))
min_profit_month = dates[min_profit_index]
min_profit_amt = monthly_diff[min_profit_index]

# output results into console and file
output_text = \
f"""Financial Analysis
-----------------------------------
Total Months: {numMonths}
Total: ${int(total_profit_loss)}
Average change: ${avg_change_profit_loss:.2f}
Greatest Increase in Profits: {max_profit_month} (${int(max_profit_amt)})
Greatest Decrease in Profits: {min_profit_month} (${int(min_profit_amt)})
"""
print(output_text)

output_file = working_dir / "pybank_output.txt"
with output_file.open(mode="w", encoding="utf-8") as file:
    file.write(output_text)
