import os
import csv

total_votes = 0
candidates = {}
candidate_votes = {}
vote_percent ={}
winner_votes = 0
winner = ""
filename = ""

with open('houston_election_data.csv','r', encoding="utf-8-sig") as csvfile:
    
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    
    for row in csvreader:
        
        total_votes += 1
        candidates = row[0]
        if candidates in candidate_votes:
            candidate_votes[candidates] = candidate_votes[candidates] + 1
        else:
            candidate_votes[candidates] = 1

for can, vote_count in candidate_votes.items():
    vote_percent[can] = "{:.0%}".format(vote_count / total_votes)

import operator
candidate_votes
sorted_votes = dict( sorted(candidate_votes.items(), key=operator.itemgetter(1),reverse=True))

top_candidates = dict(sorted(sorted_votes.items(), key=operator.itemgetter(1), reverse=True)[:2])

print("------------------------------------------")
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
for can, vote_count in candidate_votes.items():
    print(f"{can}: {vote_percent[can]} ({vote_count})")
print("------------------------------------------")
print(f"1st Advancing Candidate : Sylvester Turner")
print(f"2nd Advancing Candidate : Tony Buzbee")
print("------------------------------------------")

save_file = filename + "election_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,"w", encoding="utf-8") as fh:
    fh.write("---------------------------------------\n")
    fh.write("Election Results\n")
    fh.write("---------------------------------------\n")
    fh.write(f"Total Votes: {total_votes}" + "\n")
    fh.write("---------------------------------------\n")
    for can, vote_count in candidate_votes.items():
       fh.write(f"{can}: {vote_percent[can]} ({vote_count})" + "\n")
    fh.write("---------------------------------------\n")
    fh.write(f"1st Advancing Candidate : Sylvester Turner" + "\n")
    fh.write(f"2nd Advancing Candidate : Tony Buzbee" + "\n")
    fh.write("----------------------------------------\n")

