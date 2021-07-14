#PyPoll

# Import Dependencies 
import os 
import csv 

# Upload file path 
pollData = os.path.join("Resources", "election_data.csv")

# Open the .CSV file 
with open(pollData) as pollFile:
    csvReader = csv.reader(pollFile, delimiter = ',')

    # Read the header row
    csvHeader = next(csvReader)
    print (f"CSV Header: {csvHeader}")

    # Find the total number of votes that were casted (this doesn't include the header)
    next(csvReader)
    numberVotes = list(csvReader)
    rowCount = len(numberVotes)



