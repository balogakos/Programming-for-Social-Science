# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:03:31 2022

@author: Akos
"""
#import relavent libaries
import csv
import matplotlib
#import agentframe work
import agentframeworkIO

#set the number of agents and iterations
num_agents = 10
num_iterations = 10

#create lists for environment(read in from in.txt) and agents
environment = []
agents = []


for i in range(num_agents):
    agents.append(agentframeworkIO.Agent(environment))

#open text file using CSV
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #using two for loops read through it by row then by word
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

#clear output file
agents[i].clear()

#for loop for the number of iterations and agents making agents do actions
for j in range(num_iterations):
    for i in range(num_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].vommit()
        agents[i].output()    
        
            
#Create plot         
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#map environment onto plot
matplotlib.pyplot.imshow(environment)

#using a for loop plot agents
for i in range(num_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#show plot
matplotlib.pyplot.show()