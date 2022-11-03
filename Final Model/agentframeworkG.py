# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:56:18 2022

@author: Akos
This is the agent framework for the finalmodel.py file.
Two classes can be found one for the agents and one for wolves.
"""

# Import libaries
import random

# Create class
class Agent():
    def __init__(self, environment, agents, y, x):
        '''
        First function to initiate attributes of agents

        Parameters
        ----------
        environment : A list of lists
            The environment in which the agents exist within
        agents : list
            Agents within the environment
        y : Float
            Y-coordinate of agent
        x : Float
            X-coordinate of agent
        store : Float
            Amount agents have eaten

        Returns
        -------
        Creates agents, enironment and storage for agents

        '''
        self.environment = environment
        self.store = 0 
        self.y = y
        self.x = x
        self.agent = agents
        
    # Create move function to move coordinates randomly 
    
    def move(self):
        '''
        Function to move agents randomly
        

        Returns
        -------
        New X and Y coordinates for agents
        Tested with printing coordinates before and after move function and
        random seed
        '''
        #print(self.y, self.x)
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300

        if random.random() < 0.5:
            self.x = (self.x + 5) % 300
        else:
            self.x = (self.x - 5) % 300
        #print(self.y, self.x)
        
    # Eat function to eat all numbers at a coordinate
    def eat(self):
        '''
        Agents eat all numbers on enviroment coordinate
        
        Tested by printing self.environment and self.store before and after
        the if statement
        '''
        #print(self.environment[self.y][self.x] + self.store)  
        if self.environment[self.y][self.x] > 0:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #print(self.environment[self.y][self.x] + self.store)  
        
    def vommit(self):
        '''
        If the agent eats more than 250 than it vommits the contents onto
        the coordinates it is on

        '''
        #print(self.store)
        if self.store >= 250:
            self.environment[self.y][self.x] += self.store
            self.store = 0
        #print(self.store)
            
   
    def share_with_neighbours(self, neighbourhood):
        '''
        Comminicate with neighbours if they are touching if they are the 
        store equals their average.
        '''
        for agent in self.agent:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
               sum = self.store + agent.store
               ave = sum/2
               self.store = ave
               agent.store = ave
               #print("sharing " + str(distance) + " " + str(ave))
                    
    #Calculate the distance between agents    
    def distance_between(self, agent):
        '''
        

        Parameters
        ----------
        self.x/self.y : Integer
            X/Y Coordinates of current agent
        agent.x/agent.y: Integer
            X/Y Coordinates of other agent

        Returns
        -------
        Integer
            Distance between two agents
            
        Tested with pythag thereom using coordinates 3,4 and 0,0 with an
        expected distance of 5 which was produced.
        '''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
         #distance = (((0 - 3)**2) + ((0 - 4)**2))**0.5
         #print(distance), 5
     
class Wolf:
    
    def __init__(self, neighbourhood, environment, x, y):
        '''
        Function to initiate attributes of wolves

        Parameters
        ----------
        neighbourhood : Integer
        Communicates with agents to meassure distance
        environment : list of list
            Environment in which agents exist
        x : Integer
            X coordinate of wolves
        y : Integer
            Y coordinate of wolves

        Returns
        -------
        Tested by printing out starting coordinates #print(self.x, self.y)
        '''
        self.y = random.randint(0,299)
        self.x = random.randint(0,299)
        self.environment = environment
        self.neighbourhood = neighbourhood
        self.wolfstore = 0
        
    def movewolf(self):
        '''
        Function to move wolves using random libaray

        Returns
        -------
        New oordinates for wolves
        
        Tested by printing coordinates for one wolf before and after movewolf
        function was called.
        '''
        #print(self.x, self.y)
        if random.random() < 0.5:
            self.y = (self.y + 10) % 300
        else:
            self.y = (self.y - 10) % 300

        if random.random() < 0.5:
            self.x = (self.x + 10) % 300
        else:
            self.x = (self.x - 10) % 300
        #print(self.x, self.y)
            
    def distance_from(self, sheep):
        '''
        Fucntion to calulate distance between sheep(agents) and wolves

        Parameters
        ----------
        sheep : Integer
        Coordinates of sheep
        self: Integer
        Coordinates of wolf

        Returns
        -------
        Integer
            Distance between wovles and sheep
        
        Tested with pythag thereom using coordinates 3,4 and 0,0 with an
        expected distance of 5 which was produced.

        '''
        return (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5
        #distance = (((0 - 3)**2) + ((0 - 4)**2))**0.5
        #print(distance), 5
    def eat_sheep(self, neighbourhood, wolves, agents):
        '''
        Function for wovles to eat sheep if they are close together

        Parameters
        ----------
        wolves : list
            Coordinate list of wolves
        agents : list
            Coordinate list of sheep

        Tested by using printing out number of sheep before function was run
        and after function was run
        '''
        #print(agents)
        for wolf in wolves:
            for agent in agents:
                distance = self.distance_from(agent)
                if distance <= neighbourhood:
                    self.wolfstore += agent.store
                    agents.remove(agent)
        #print(agents)
     

        
        
        
        
        
        
        