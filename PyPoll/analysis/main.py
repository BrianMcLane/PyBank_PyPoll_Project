import csv
import os

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

with open(pypoll_csv,"r") as PyPoll:
    pypoll_reader = csv.reader(PyPoll)

    next(pypoll_reader)

    candidate_options = []
    candidate_votes = {}
    winning_count = 0
    winner = ""
    vote_count = 0

    for row in pypoll_reader:
        vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        if candidate_votes[candidate_name] > winning_count:
            winning_count = candidate_votes[candidate_name]
            winner = candidate_name
        candidate_votes[candidate_name] += 1
    # print(winning_count)
    # print(winner)
    
    khan = candidate_votes["Khan"] 
    correy = candidate_votes["Correy"] 
    li = candidate_votes["Li"]  
    otooley = candidate_votes["O'Tooley"] 

    
    kp = round(((khan/ vote_count) * 100), 3) # 63.0
    cp = round(((correy / vote_count) * 100), 3) # 20.0
    lp = round(((li / vote_count) * 100), 3) # 14.0 
    op = round(((otooley / vote_count) * 100), 3) #3.0
    
    # print(candidate_options)
    # print(candidate_votes)
    # print(kp, cp, lp , op)
   
    
results = (f' Election Results \n -------------------- \n Total Votes: {vote_count} \n -------------------- \n {candidate_options[0]}: {kp}% ({khan}) \n {candidate_options[1]}: {cp}% ({correy}) \n {candidate_options[2]}: {lp}% ({li}) \n {candidate_options[3]}: {op}% ({otooley}) \n -------------------- \n Winner: {winner} \n --------------------')
print(results)

output_path = os.path.join("election_analysis.txt")
with open(output_path, "w") as final:
    final.write(str(results)) 