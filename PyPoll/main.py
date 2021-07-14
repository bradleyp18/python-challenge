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
    candData = list(csvReader)
    rowCount = len(candData)

    # Create a list of Candidates 
    candidateList = []
    candMark = []

    # Run through the file 
    for c in range (0, rowCount):

        #Create candidate variable that tracks for loops through the 2nd index (3rd column)
        candidate = candData[c][2]
        candMark.append(candidate)

        # Conditional to keep track of candidate list
        if candidate not in candidateList:
            candidateList.append(candidate)
    candidateCount = len(candidateList)

    # Find the vote count for each candidate and their respective %
    votes = []
    percentage = []

    for v in range(0, candidateCount):
        candidateName = candidateList[v]
        votes.append(candData.count(candidateName))
        votePct = votes[v] / rowCount
        percentage.append(votePct)
    winningCandidate = votes.index(max(votes))

    bars = 30 * '-'
    print ('Election Results')
    print (bars)
    print (f"Total Votes: {rowCount: ,}")
    print (bars)
    
    




