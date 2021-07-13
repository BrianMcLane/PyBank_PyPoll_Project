import csv
import os

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

with open(pypoll_csv,"r") as PyPoll:
    pypoll_reader = csv.reader(PyPoll)

    next(pypoll_reader)

    voting_booth = {}
   
    # vote_count = 0
    # Khan = 0 
    # Correy = 0
    # Li = 0
    # OTooley = 0

    for row in  pypoll_reader:
        # vote_count = vote_count + 1
        if row[2] == 'Khan':
            if 'canidate' not in voting_booth:
                voting_booth['canidate'] = []
            voting_booth['canidate'].append(row[2])
       



        print(voting_booth)


    #     if row[2] == "Khan":
    #         Khan += 1
    #     elif row[2] == "Correy":
    #         Correy += 1
    #     elif row[2] == "Li":
    #         Li += 1
    #     else:
    #         OTooley += 1
    
    # Khan_perc = (Khan / vote_count) * 100
    # Correy_perc = (Correy / vote_count) * 100
    # Li_perc = (Li / vote_count) * 100
    # OTooley_perc = (OTooley / vote_count) * 100

    # print (voting_booth)

    # print(vote_count) # 3521001 
    # print(Khan_perc, Khan)
    # print(Correy_perc, Correy)
    # print(Li_perc, Li)
    # print(OTooley_perc, OTooley)

   
