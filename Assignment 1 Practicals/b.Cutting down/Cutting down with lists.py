#import relavent libaries
import random
import operator
import matplotlib.pyplot
import doctest

#During testing set random seed to 0
    #random.seed(0)

#Make an empty list
agents = []

#Add an agent with random coordinates to list
agents.append([random.randint(0,99),random.randint(0,99)])

# Change y0 and x0 based on random numbers 3 times.
if random.random() < 0.5:
    agents[0][0]+= 1
else:
    agents[0][0]-= 1
if random.random() < 0.5:
    agents[0][1]+= 1
else:
    agents[0][1]-= 1
    
if random.random() < 0.5:
    agents[0][0]+= 1
else:
    agents[0][0]-= 1
if random.random() < 0.5:
    agents[0][1]+= 1
else:
    agents[0][1]-= 1
    
if random.random() < 0.5:
    agents[0][0]+= 1
else:
    agents[0][0]-= 1
if random.random() < 0.5:
    agents[0][1]+= 1
else:
    agents[0][1]-= 1

# Make a second set of coordinates and add them to the list 
    # Under y1 = agents[1][0] x1 = agents[1][1]
agents.append([random.randint(0,99),random.randint(0,99)])

# Change y1 and x1 based on random numbers 3 times
if random.random() < 0.5:
    agents[1][0]+= 1
else:
    agents[1][0]-= 1
if random.random() < 0.5:
    agents[1][1]+= 1
else:
    agents[1][1]-= 1

if random.random() < 0.5:
    agents[1][0]+= 1
else:
    agents[1][0]-= 1
if random.random() < 0.5:
    agents[1][1]+= 1
else:
    agents[1][1]-= 1

if random.random() < 0.5:
    agents[1][0]+= 1
else:
    agents[1][0]-= 1
if random.random() < 0.5:
    agents[1][1]+= 1
else:
    agents[1][1]-= 1

# Find the distance using pythag thereom fuction
def pythag(x0, x1, y0, y1):
    '''
    Finding the distance between two coordinates

    Parameters
    ----------
    x0 : Int
        X coordinate of agent[0]
    x1 : Int
        X coordinate of agent[1]
    y0 : Int
        Y coordinate of agent[0]
    y1 : Int
        Y coordinate of agent[1]

    Returns
    -------
    Int
    The distance between two agents
    
    >>> pythag(4,1,5,1)
    5.0

    '''
    difference = (((x1 - x0)**2) + ((y1 - y0)**2))**0.5
    print(difference)

pythag(agents[0][1], agents[1][1], agents[1][0], agents[0][0])

# Code before making function
'''
difference = (((agents[1][1] - agents[0][1])**2) + 
 ((agents[1][0] - agents[0][0])**2))**0.5
'''

#Plotting the coordinates on a scatter plot using matplot
    #Set perimeters of plot, (0-99 is 100)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#Plot the position of agents
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# Adding a plot for the maximum X value
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0] =='red')
matplotlib.pyplot.show()

#Doctest to see if pythag function works
    #doctest.testmod(name="pythag", verbose=True)

#print coordinates of agents
print(agents)
