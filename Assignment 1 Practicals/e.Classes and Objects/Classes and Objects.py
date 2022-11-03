import random
import operator
import matplotlib.pyplot
import agentframework
import doctest

#Find the distance between two agents
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
        distance = (((agents_row_a.x - agents_row_b.x)**2) + 
                ((agents_row_a.y - agents_row_b.y)**2))**0.5
        return distance

#Set random seed for development and testing
    #random.seed(0)

#Create list for agents
agents = []

#Set out num of agents and iterations
num_of_agents = 10
num_of_iterations = 100

#Connect to agent framework
a = agentframework.Agent()

#Test if move() is working
'''
print(a.y, a.x)
a.move()
print(a.y, a.x)
'''

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        agents[i].move()

# #Create variables for min and max distances
max_distance = 0
min_distance = None

# #Find the distance between agents using a for loop and max distance
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

#Create plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

#Plot agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

#Show plot
matplotlib.pyplot.show()

#doctest for distance_between function
    #doctest.testmod(name="distance_between", verbose=True)

