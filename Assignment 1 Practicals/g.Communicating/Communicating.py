# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:03:31 2022

@author: Akos
"""
#This practical looks at creating code to make agents communicate with
# eachother through the use of a pythagerous function from the agentframework

# Import libaries
import csv
import matplotlib
import agentframeworkC
import random

# Set out parametres
num_agents = 10
num_iterations = 100
neighbourhood = 20

#Create lists
environment = []
agents = []

# Connect to agentframework
for i in range(num_agents):
    agents.append(agentframeworkC.Agent(environment, agents))

# Open text and read it. adding it to lists
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        #print(agents)
        #print(environment)

# Loop through and shuffle agents list
#Using functions make agents move, eat, vommit, and communicate        
for j in range(num_iterations):
    random.shuffle(agents)
    for i in range(num_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].vommit()
        
            
# Create pyplot, set axis and add in enviroment    
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)

#Using a for loop, add agents to plot
for i in range(num_agents): 
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    
#Show pyplot
matplotlib.pyplot.show()