# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:03:31 2022

@author: Akos
"""
#Animation practical, creating an animation for agents and stopping conditions
# Import libaries
import csv
import agentframeworkA
import random
import matplotlib.pyplot
import matplotlib.animation

# Set parametres

num_agents = 10
num_iterations = 10
neighbourhood = 20

#Create lists
environment = []
agents = []

# Open text and read through it, adding it to environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        #print(agents)
        
# Create pyplot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Create agents
for i in range(num_agents):
    agents.append(agentframeworkA.Agent(environment, agents))
    
carry_on = True
        

#Update animation       
def update(frame_number):     
    #Clear figure, add carry on, and shuffle agents
    fig.clear()
    global carry_on
    random.shuffle(agents)
    for i in range(num_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].vommit()
    
    # Update and visualise the placement of agents on pyplot
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
    #if random is less then 0.1 animation stops
    if random.random() < 0.1:
        carry_on = False
        print("Stopping Condition Met")

#Creating gen function
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on) :
        yield a
        a = a + 1

# New animation with gen function updated from num_iterations for frames
animation = matplotlib.animation.FuncAnimation(fig, update, 
                                               frames=gen_function, 
                                               repeat=False)

# Show on pyplot
matplotlib.pyplot.show()


