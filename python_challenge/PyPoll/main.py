import os import csv csvpath=os.path.join("Resources", "election_data.csv")output_path=os.path.join("analysis", "output.txt")candidates=[]candidates_votes={}total_votes=0winning_count=0print("Election Results")print("---------------------------\n")with open(csvpath, newline="") as electionfile:    csvreader=csv.reader(electionfile)    csv_header=next(csvreader)            for row in csvreader:       total_votes=total_votes+1       candidate=(row[2])           if candidate not in candidates:           candidates.append(candidate)           candidates_votes[candidate]=1       else:            candidates_votes[candidate]=candidates_votes[candidate]+1print(f"Total Votes: {total_votes}\n")print("---------------------------\n")           with open(output_path, "w") as file:    file.write("Election Results\n")    file.write("---------------------------\n")    file.write(f"Total Votes: {total_votes}\n")    file.write("---------------------------\n")    for candidate in candidates:        votes=candidates_votes.get(candidate)          percent=round(((votes/total_votes)*100),3)        print(f'{candidate}: {percent}% ({votes})')        file.write(f'{candidate}: {percent}% ({votes})\n')            if votes> winning_count:            winning_count=votes            winner=candidate    file.write("---------------------------\n")    file.write(f"Winner: {winner}")    print("---------------------------\n")    print(f"Winner: {winner}")                          