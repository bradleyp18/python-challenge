# PyBank

# import our necessary tools 
# Create file paths across operating systems
import os

# Module to read our csv 
import csv

# Store the file path associated with the file -- include 'r' pre-filepath 
csvFile = R"C:\Users\bradl\Desktop\Git\nwBootCamp\python-challenge\PyBank\Resources\budget_data.csv"

# Create empty lists to iterate through
totalMonths = []
totalProfit = [] 
monthlyProfitChange = [] 

# Read CSV file 
with open(csvFile) as budgetFile:
    csvReader = csv.reader(budgetFile, delimiter=',')

    # This will read the header row
    csvHeader = next(csvReader)
    print(f"CSV Header: {csvHeader}")

    # Read the rows (excluding the header)
    for row in csvReader:

        # Append total months and total profit 
        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))

    # Iterate through profits to get monthly change in profits
    for i in range (len(totalProfit)-1):
        monthlyProfitChange.append(totalProfit[i+1] - totalProfit[i])

# 
        

# Find the total number of months in the dataset 

