# PyBank

# import our necessary tools 
# Create file paths across operating systems
import os

# Module to read our csv 
import csv

# Store the file path associated with the file -- include 'r' pre-filepath 
# Update file path on seperate machines 
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

        # Display csv
        print (row)

        # Append total months and total profit 
        totalMonths.append(row[0])
        totalProfit.append(int(row[1]))

    # Iterate through profits to get monthly change in profits
    for i in range (len(totalProfit)-1):
        monthlyProfitChange.append(totalProfit[i+1] - totalProfit[i])

# Find max and min of the monthly profit change 
maxIncrease = max(monthlyProfitChange)    
maxDecrease = min(monthlyProfitChange)

# Find the respective month for the min and max value 
# Be sure to add one becasue we are looking for the ending month, not the beginning 
maxUpMonth = monthlyProfitChange.index(max(monthlyProfitChange)) + 1
maxDownMonth = monthlyProfitChange.index(min(monthlyProfitChange)) + 1

# Find the total number of months in the dataset 
print("Financial Analysis")
print(25 * "-")

# Count of total months in dataset 
print(f"Total Months: {len(totalMonths)}")

# Find the sum of the total Profit 
print(f"Total: ${sum(totalProfit)}")

# Round two decimal places to find the average 
print(f"Average Change: {round(sum(monthlyProfitChange)/len(monthlyProfitChange),2)}")

# Display the month and its associated max / min value 
print(f"Greatest Increase in Profits: {totalMonths[maxUpMonth]} (${(str(maxIncrease))})")
print(f"Greatest Decreasw in Profits: {totalMonths[maxDownMonth]} (${(str(maxDecrease))})")


# Create output file 
outputFile = os.path.join("nwBootCamp", "python-challenge", "PyBank", "analysis", "results.txt")

with open(outputFile, "w") as file:

    # Write out methods that will replicate terminal output
    # \n creates a new line 
    file.write("Financial Analysis")
    file.write("\n")
    file.write(25 * "-")
    file.write("\n")
    file.write(f"Total Months: {len(totalMonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(totalProfit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthlyProfitChange)/len(monthlyProfitChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {totalMonths[maxUpMonth]} (${(str(maxIncrease))})")
    file.write("\n")
    file.write(f"Greatest Decreasw in Profits: {totalMonths[maxDownMonth]} (${(str(maxDecrease))})")