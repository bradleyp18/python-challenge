# PyBank

# import our necessary tools 
# Create file paths across operating systems
import os

# Module to read our csv 
import csv

# Store the file path associated with the file -- include 'r' pre-filepath 
csvPath = R"C:\Users\bradl\Desktop\Git\nwBootCamp\python-challenge\PyBank\Resources\budget_data.csv"

# Read CSV file 

with open(csvPath, 'r') as filePath:
    csvReader = filePath.read()
    print (csvReader)



