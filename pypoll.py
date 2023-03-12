import os

import csv

csvpath =  os.path.join('election_data.csv')

candidate = []
candidate_votes = {}
count = 0
tot_vote = 0
percent_vote = []

with open(csvpath) as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    

    
    csv_header = next(csvreader)
    
     
    
    for row in csvreader:
         
        candidate = row[2]
        count = count + 1 
        
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1
print("                        ")
print("Election Results") 
print("---------------------------")            
print("Total Votes: " + str(count))

for i in candidate_votes:
    percent = round((float(candidate_votes[i])/count)*100, 0)
    constant = "% ("
    print (f'{i} {percent} {constant} {candidate_votes[i]}' + ")")

for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key


print("---------------------------")      
print ("The winner is : " + winner)
print("---------------------------")

 
Pypoll_analysis = os.path.join("analysis", "Pypoll_analysis.txt")
   
     
with open (Pypoll_analysis , "w") as text:
    
    text.write("                        \n")
    text.write("Election Results\n") 
    text.write("---------------------------\n")            
    text.write("Total Votes: " + str(count) + "\n")

    for i in candidate_votes:
        percent = round((float(candidate_votes[i])/count)*100, 0)
        constant = "% ("
        text.write (f'{i} {percent} {constant} {candidate_votes[i]}' +")\n")
        
    text.write("---------------------------\n")      
    text.write("The winner is : " + winner +"\n")
    text.write("---------------------------\n")   