# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:56:18 2022

@author: Akos
"""

# Import libaries

import random
import doctest

# Create class
class Agent():
    random.seed(1)
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
        None.

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
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
        #print(self.y, self.x)
        
    # Eat function to eat all numbers at a coordinate
    def eat(self):
        '''
        Agents eat all numbers on enviroment coordinate

        Returns
        -------
        No return
        
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
         return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
     
     
class Wolf:
    
    def __init__(self, neighbourhood, environment, x, y):
        self.y = random.randint(0,299)
        self.x = random.randint(0,299)
        self.environment = environment
        self.neighbourhood = neighbourhood
        self.wolfstore = 0
        
    def movewolf(self):
        if random.random() < 0.5:
            self.y = (self.y + 10) % 300
        else:
            self.y = (self.y - 10) % 300

        if random.random() < 0.5:
            self.x = (self.x + 10) % 300
        else:
            self.x = (self.x - 10) % 300
            
    def distance_from(self, sheep):
        return (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5
   
    def eat_sheep(self, neighbourhood, wolves, agents):
        for wolf in wolves:
            for agent in agents:
                distance = self.distance_from(agent)
                if distance <= neighbourhood:
                    self.wolfstore += agent.store
                    agents.remove(agent)
     

        
        
        
        
        
        
        