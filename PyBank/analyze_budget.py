#--------------------------------------------------------------------------------------------------
'''
  * In this challenge, you are tasked with creating a Python script for analyzing the financial
    records of your company. You will give a set of financial data called
    [budget_data.csv](PyBank/Resources/budget_data.csv).
    The dataset is composed of two columns: `Date` and `Profit/Losses`.
    (Thankfully, your company has rather lax standards for accounting so the records are simple.)

  * Your task is to create a Python script that analyzes the records to calculate each of the following:

    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The average of the changes in "Profit/Losses" over the entire period
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in losses (date and amount) over the entire period

  * As an example, your analysis should look similar to the one below:

    Financial Analysis
    ----------------------------
    Total Months: 86
    Total: $38382578
    Average  Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159)
    Greatest Decrease in Profits: Sep-2013 ($-2196167)

  Date file Column Header
    Date,Profit/Losses
    row[0], row[1]

    ======================================================================================================
    Self Notes:
    * Total count of the records is the total count of the month as each record corresponds to a month.
    *
'''
#--------------------------------------------------------------------------------------------------

# Import modules os and csv
import os
import csv

# Set the path for the CSV file in budget_data.csv
budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Create the lists to store data.
# List to hold monthly Profit/Loss value
profit = []
# List to hold Profit/Loss changes each month from prior month
monthly_changes = []
# List to hold the months
budget_month = []

# Initialize the variables as required.
count = 0                     # Variable to count the months (number of records)
net_profit = 0              # Variable to hold the total/Net Profit/Loss
total_change_profits = 0
initial_profit = 0

# Open the data CSV file

with open(budget_data_csv, 'r', newline="") as csvfile:
    #Instantiate the csv file reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    #Get the data file header record, ignore and do nothing with it
    csv_header = next(csvreader)    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
      # Counter for number of records/months in the data file
      count = count + 1

      # List to store dates for calulation later
      budget_month.append(row[0])

      # List to hold the Profit & calculate the total profit
      profit.append(row[1])
      net_profit = net_profit + int(row[1])

      #Average change in profits every month. Then calculate the average change in profits
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

      increase_date = budget_month[monthly_changes.index(greatest_increase_profits)]
      decrease_date = budget_month[monthly_changes.index(greatest_decrease_profits)]

    print('----------------------------------------------------------')
    print('Financial Analysis')
    print('----------------------------------------------------------')
    print(f'                Total Months:            {count:>11}')
    print(f'                Total Profit:           ${net_profit:>11,.0f}')
    print(f'              Average Change:           ${average_change_profits:>11,.0f}')
    print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase_profits:>11,.0f})')
    print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits:>11,.0f})')

with open('financial_analysis.txt', 'w') as text:
    text.write('----------------------------------------------------------\n')
    text.write('Financial Analysis\n')
    text.write('----------------------------------------------------------\n\n')
    text.write(f'                Total Months:            {count:>11}\n')
    text.write(f'                Total Profit:           ${net_profit:>11,.0f}\n')
    text.write(f'              Average Change:           ${average_change_profits:>11,.0f}\n')
    text.write(f'Greatest Increase in Profits: {increase_date} (${greatest_increase_profits:>11,.0f})\n')
    text.write(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits:>11,.0f})\n')
    text.write('----------------------------------------------------------\n')
