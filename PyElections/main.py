import os
import csv

with open('houston_election_data.csv', newline="") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
       # for row in csvreader:
           # print(', '.join(row))
           print(csvreader)

name = str(houston_election_data[0])
county = str(houston_election_data[1])
vote = int(houston_data[2])

total_votes = sum(vote)