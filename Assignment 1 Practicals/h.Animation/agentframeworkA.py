# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:56:18 2022

@author: Akos
"""
#Agent framework for the animation practical
# Import libaries

import random

# Create class
class Agent():

    # Set up with init with agents and environment lists
    def __init__(self, environment, agents):
        self.environment = environment
        self.store = 0 
        self.y = random.randint(0,99) # Random Y coordinates
        self.x = random.randint(0,99) # Random X coordinates
        self.agent = agents
        
    # Create move function to move coordinates randomly 
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    # Eat function to eat all numbers at a coordinate
    def eat(self): 
        if self.environment[self.y][self.x] > 0:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            
    # Vommit function to vommit if eaten too much
    def vommit(self):
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
    #Comminicate with neighbours if they are touching the agent stores = avg        
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agent:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
               sum = self.store + agent.store
               ave = sum/2
               self.store = ave
               agent.store = ave
               #TEST print("sharing " + str(distance) + " " + str(ave))
                    
    #Calculate the distance between agents    
    def distance_between(self, agent):
         return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

        
        
        
        
        
        
        