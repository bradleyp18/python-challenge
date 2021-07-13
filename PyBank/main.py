# PyBank

# import our necessary tools 
# Create file paths across operating systems
import os

# Module to read our csv 
import csv

# Store the file path associated with the file -- include 'r' pre-filepath 
csvFile = R"C:\Users\bradl\Desktop\Git\nwBootCamp\python-challenge\PyBank\Resources\budget_data.csv"

# Read CSV file 

with open(csvFile, 'r') as budgetFile:
    csvReader = budgetFile.read()
    print (csvReader)

    # Iterate through the rows in the file 
    for row in csvReader:
        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))

    # Iterate through profits to get monthly change in profits
    for i in range (len(totalProfit)-1):
        monthlyProfitChange.append(totalProfit[i+1])

        

# Find the total number of months in the dataset 

