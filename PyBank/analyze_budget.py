# Import modules os and csv
import os
import csv

# Set the path for the CSV file in budget_data.csv
budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Create the lists to store data. 
profit = []
monthly_changes = []
date = []

# Initialize the variables as required.
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the data CSV file

with open(budget_data_csv, 'r', newline='') as csvfile:
    #Instantiate the csv file reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    #Get the data file header record, ignore and do nothing with it
    csv_header = next(csvreader)    #print(f"CSV Header: {csv_header}")

    for row in csvreader:    
      # Counter for number of records/months in the data file
      count = count + 1 

      # List to store dates for calulation later
      date.append(row[0])

      # List to hold the Profit & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Average change in profits every month. Then calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print('----------------------------------------------------------')
    print('Financial Analysis')
    print('----------------------------------------------------------')
    print(f'                Total Months:            {count:>11}')
    print(f'                Total Profit:           ${total_profit:>11,.0f}')
    print(f'              Average Change:           ${average_change_profits:>11,.0f}')
    print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase_profits:>11,.0f})')
    print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits:>11,.0f})')

with open('financial_analysis.txt', 'w') as text:
    text.write('----------------------------------------------------------\n')
    text.write('Financial Analysis\n')
    text.write('----------------------------------------------------------\n\n')
    text.write(f'                Total Months:            {count:>11}\n')
    text.write(f'                Total Profit:           ${total_profit:>11,.0f}\n')
    text.write(f'              Average Change:           ${average_change_profits:>11,.0f}\n')
    text.write(f'Greatest Increase in Profits: {increase_date} (${greatest_increase_profits:>11,.0f})\n')
    text.write(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits:>11,.0f})\n')
    text.write('----------------------------------------------------------\n')
