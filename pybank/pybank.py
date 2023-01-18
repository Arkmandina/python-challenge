#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import os


file_to_load = os.path.join (".", "Resources", "budget_data.csv")

file_to_output = os.path.join (".", 'budget_analysis.txt')

total_months = 0
total_net = 0

net_change_list = []
month_change = []

increase = ["", 0]
decrease = ["", 999999999999999999]


# In[5]:


#read the csv and covert to list
with open(file_to_load) as financial_data:
    
    reader = csv.reader(financial_data)
    
    
    #read the top row as header
    header = next(reader)
    
    #print(F"Header: {header}")
    first_row = next(reader)
    
    total_net += int(first_row[1]) #1088983
    previous_net = int(first_row[1]) #1088983
    
    total_months += 1
    
    for row in reader:
       
        #Find the total
        #total_months = total_months + 1
        total_months += 1
        total_net += int(row[1])
      
    
        #Track net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
 
    
    
        # calculate greatest increase
        if(net_change > increase[1]):
            increase[0] = row[0]
            increase[1] = net_change

       # calculate greatest decrease
        if(net_change < decrease[1]):
            decrease[0] = row [0]
            decrease[1] = net_change


net_monthly_average = sum(net_change_list)/ len(net_change_list)


# In[6]:



results = (
f"Financial Analysis\n"
F"---------------------------\n"
f"Total Months: {total_months}\n"
f" Total: ${total_net}\n"
f" Average Change: ${net_monthly_average:.2f}\n"
f" Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
f" Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})"

)

print(results)


# In[8]:


with open(file_to_output, "w") as txt_file:
    txt_file.write(results)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




