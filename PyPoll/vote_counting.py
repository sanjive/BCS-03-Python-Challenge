#--------------------------------------------------------------------------------------------
'''
  * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 

  * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
    The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
    Your task is to create a Python script that analyzes the votes and calculates each of the following:

    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.

      * As an example, your analysis should look similar to the one below:

        Election Results
        -------------------------
        Total Votes: 3521001
        -------------------------
        Khan: 63.000% (2218231)
        Correy: 20.000% (704200)
        Li: 14.000% (492940)
        O'Tooley: 3.000% (105630)
        -------------------------
        Winner: Khan
        -------------------------

    * In addition, your final script should both print the analysis to the terminal 
      and export a text file with the results.

'''
#--------------------------------------------------------------------------------------------
# My notes:
'''
    * Create a loop, count and add all the votes
    * Create a list to track the candidates
    * Create a list to track the votes for the candidate
    * Calculate Vote percentage of total votes
    * Candidate with max votes is the winner

    - The data file has voterid for each each record and assigned to the candidate and the county.
    - The county data can be ignored as it does not seem to play any role in the analysis
'''
#--------------------------------------------------------------------------------------------

# Import modules os and csv
import os
import csv

# Set the path for the CSV file in election_data.csv
election_data_csv = os.path.join('.', 'Resources', 'election_data.csv')

# Create lists/Variables to store data. 
# A list to capture the names of candidates
candidates = []

# A list to capture the number of votes each candidate
num_votes = []

# A list to capture the percentage of total votes each candidate garners 
percent_votes = []

# A counter for the total number of votes 
total_votes = 0

# The column headers in the data file and corresponding csvreader list mapping
# csvheader:  Voter ID, County, Candidate
# csvreader:  row[0],   row[1], row[2]

# Open the data CSV file
with open(election_data_csv, 'r', newline='') as csvfile:
    #Instantiate the csv file reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    #Get the data file header record, ignore and do nothing with it
    csv_header = next(csvreader)    #print(f'CSV Header: {csv_header}')

    for row in csvreader:
        # Add to our vote-counter (Each row has a voter id and assigned to a candidate)
        total_votes += 1 

        # Add the Candidate to the list, if does not exist and add the vote count 
        # assigned the respective candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = votes/total_votes
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print('----------------------------------------------------------')
print('Election Results                                          ')
print('----------------------------------------------------------')
print(f'  Total Votes:          {total_votes:>9,}')
print('----------------------------------------------------------')
for i in range(len(candidates)):
    print(f' {candidates[i]:>12}: {percent_votes[i]:>7.3%} ({num_votes[i]:>9,})')
print('----------------------------------------------------------')
print(f'       Winner: {winning_candidate}')
print('----------------------------------------------------------')

# Outputting the result to a text file
with open('election_results.txt', 'w') as text:
    text.write('----------------------------------------------------------\n')
    text.write('Election Results\n')
    text.write('----------------------------------------------------------\n')
    text.write(f'  Total Votes:          {total_votes:>9,}\n')
    text.write('----------------------------------------------------------\n')
    for i in range(len(candidates)):
        text.write(f' {candidates[i]:>12}: {percent_votes[i]:>7.3%} ({num_votes[i]:>9,})\n')
    text.write('----------------------------------------------------------\n')
    text.write(f'       Winner: {winning_candidate}\n')
    text.write('----------------------------------------------------------\n')
