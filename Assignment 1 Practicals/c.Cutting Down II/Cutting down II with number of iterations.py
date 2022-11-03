#Import relavent libaries
import random
import operator
import matplotlib.pyplot

# Create a variable for the number of agents and iterations
num_agents = 10
num_iterations = 10

# Make a list
agents = []

# Using a for loop create the number of agents specified
for i in range(num_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents randomly accounting for edges by using %100
    # Using iteration allows for agents to be moved more
for n in range(num_iterations):
    for i in range(num_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

# Testing with 10 to see greater movements
    #to test if random mover is working
        #print(agents)

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




# Plotting the coordinates on a scatter plot using matplot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Using a for loop to plot all agenets
for i in range(num_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#Show on plot
matplotlib.pyplot.show()


