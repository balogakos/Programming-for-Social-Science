# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:38:22 2022

@author: Akos
"""
#Import relavent libaries
import random
import operator
import matplotlib.pyplot
import time
import doctest

#Set a random seed to allow testing and development
    #random.seed(0)

#Start time
start = time.process_time()

#Set func for finding the distance between two agents
    #Test with 3,4,5 triangle
def distance_between(agents_row_a, agents_row_b):
    '''
    Using a for loop find the distance between agents for the specified
    number of agents

    Parameters
    ----------
    agents_row_a : Float
        Coordinates of one agent
    agents_row_b : Float
        Coordinates of one agent

    Returns
    -------
    Float
        Distance between two agents
    
    >>> distance_between([3,4],[0,0])
    5.0

    '''
    for i in range(num_of_agents):
       distance = (((agents_row_a[0] - agents_row_b[0])**2) + 
                ((agents_row_a[1] - agents_row_b[1])**2))**0.5
       return distance

#Make a list for agents
agents = []

#Set number of agents and iterations
num_of_agents = 10
num_of_iterations = 5

#Make the agents, with random starting coordinates
    #Use for loop to create amount specified earlier
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#Move the agents
    #Use for loop to loop through the number of iterations specified
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            


#Create variables for min and max distances
max_distance = 0
min_distance = None

#Find the distance between agents using a for loop and max distance
for i in range(0, num_of_agents):
    for j in range(i+1,num_of_agents):
        d = distance_between(agents[i], agents[j])
        if d > max_distance:
            max_distance = d
        if min_distance == None:
            min_distance = d
        elif d < min_distance:
            min_distance = d

#Set max and min distances to 2dp
dpmax_distance = "{:.2f}".format(max_distance)
dpmin_distance = "{:.2f}".format(min_distance)

#print max and min distances
print("Maximum distance is", dpmax_distance, "\nMinimum Distance is",
      dpmin_distance)
        
#Create scatterplot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#Using a for loop plot agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#Show plot
matplotlib.pyplot.show()

#End time and print out total time
end = time.process_time()
print('Total time is ' + str(end - start))

#doctest for distance_between function
doctest.testmod(name="distance_between", verbose=True)