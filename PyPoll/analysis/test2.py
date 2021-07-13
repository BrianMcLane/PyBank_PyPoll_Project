import csv
import os

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

with open(pypoll_csv,"r") as PyPoll:
    pypoll_reader = csv.reader(PyPoll)

    next(pypoll_reader)

    candidate_options = []
    candidate_votes = {}
    winning_candidate = ""
    winning_count = 0
    vote_count = 0

    for row in pypoll_reader:
        vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        

    print(candidate_options)
    print(candidate_votes)
    

