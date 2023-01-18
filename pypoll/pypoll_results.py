#!/usr/bin/env python
# coding: utf-8

# In[26]:


import os
import csv


# files to load and output
file_to_load = os.path.join(".", "Resources", "election_data.csv")
file_to_output = os.path.join(".", "election_analysis.txt")



# In[45]:


#total vote counter
total_votes = 0

#candidate vote counters and options
candidate_votes ={}
candidate_options = []

#election winner and number of votes
winning_candidate = ""
winning_count =  0

with open(file_to_load) as election_data:
    
    reader = csv.reader(election_data)
    
    #read header
    header = next(reader)
    #print(header)
    
    for row in reader:
        #add total votes
        total_votes = total_votes + 1
        
        #gets candidate name from each row
        candidate_name = row[2]
        
        # if doesn't match any known candidate
        #loop discovering candidates
        
        if candidate_name not in candidate_options:
           
            #add it the list of candidates
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
            
print(candidate_votes)
print(candidate_options)


# In[48]:


#creating table
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes} \n"
        f"----------------------\n"
         
    )
    print(election_results)  
    
    txt_file.write(election_results)
    
    #finding vote count and percentage for candidates
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) *100
        
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
    
        print(voter_output)    
        
        txt_file.write(voter_output)
    
    #summarizing the actual winner
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate} \n"
        f"----------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)

