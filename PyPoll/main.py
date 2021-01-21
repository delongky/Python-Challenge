import os
import csv

# path to collect data from resources folder
election_csv = os.path.join(r'C:\Users\kyucz\Desktop\UPenn Data & Visualization\Python-Challenge\PyPoll\Resources\election_data.csv')

# establish variables and dictionary
votes = 0
candidate_tally = {}

# open and read csv
with open(election_csv, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # skips header
    next(reader, None)

    for row in reader:
        # calculate total number of votes
        votes += 1
        #creates list for candidate names
        name = row [2]
        # total number of votes each candidate received
        if name in candidate_tally.keys():
           candidate_tally[name] += 1 
        else:
            candidate_tally[name] = 1

# establish lists for dictionary info and adds this info to lists
candidate = []
vote_count = []
for key, value in candidate_tally.items():
    candidate.append(key)
    vote_count.append(value)

# calculate percentages of votes for each candidate using a list
vote_percent = []
for i in vote_count:
    vote_percent.append("{:.0%}".format(i/votes))

# zip list data into tuples
election_data = list(zip(candidate, vote_count, vote_percent))

# calculate winner based on popular vote
final_results = []
for person in election_data:
    if max(vote_count) == person[1]:
        final_results.append(person[0])
winner = final_results[0]

# print report
# create new variable using f-strings for formatting to easily write to txt file
ElectionResults = (
f"Election Results \n"
f"-------------------- \n"
f"Total Votes: {votes} \n"
f"-------------------- \n"
f"{election_data[0]} \n"
f"{election_data[1]} \n"
f"{election_data[2]} \n"
f"{election_data[3]} \n"
f"-------------------- \n"
f"The winner is: {winner} \n")
print(ElectionResults)

# create text file
PyPollResults = open("PyPollResults.txt",'w')
PyPollResults.write(ElectionResults)
PyPollResults.close()