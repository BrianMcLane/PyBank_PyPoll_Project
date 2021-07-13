import csv
import os

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

with open(pypoll_csv,"r") as PyPoll:
    pypoll_reader = csv.reader(PyPoll)

    next(pypoll_reader)

    voting_booth = []
    vote_count = 0
    Khan = 0 
    Correy = 0
    Li = 0
    OTooley = 0
    winning_count = 0

    for row in  pypoll_reader:
        vote_count = vote_count + 1
        if row[2] not in voting_booth:
            voting_booth.append(row[2])
        
        if row[2] == voting_booth[0]:
            Khan += 1
        elif row[2] == voting_booth[1]:
            Correy += 1
        elif row[2] == voting_booth[2]:
            Li += 1
        else:
            OTooley += 1
        
        if Khan > Correy and Khan > Li and Khan > OTooley:
            Winner = voting_booth[0]
        elif Correy > Khan and Correy > Li and Correy > OTooley:
            Winner = voting_booth[1]
        elif Li > Khan and Li > Correy and Li > OTooley:
            Winner = voting_booth[2]
        elif OTooley > Khan and OTooley > Correy and OTooley > Li:
            Winner = voting_booth[3]
        
    
    Khan_perc = round(((Khan / vote_count) * 100), 3)
    Correy_perc = round(((Correy / vote_count) * 100), 3)
    Li_perc = round(((Li / vote_count) * 100), 3)
    OTooley_perc = round(((OTooley / vote_count) * 100), 3)
    
    
    
    
    #print(vote_count) # 3521001 
    #print(voting_booth)
    #print(voting_booth[0], Khan_perc, Khan)
    #print(voting_booth[1], Correy_perc, Correy)
    #print(voting_booth[2], Li_perc, Li)
    #print(voting_booth[3], OTooley_perc, OTooley)
    #print(Winner)
   


print(f" Election Results \n -------------------- \n Total Votes: {vote_count} \n -------------------- \n {voting_booth[0]}: {Khan_perc} ({Khan}) \n {voting_booth[1]}: {Correy_perc} ({Correy}) \n {voting_booth[2]}: {Li_perc} ({Li}) \n {voting_booth[3]}: {OTooley_perc} ({OTooley}) \n -------------------- \n Winner: {Winner}")

