# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:56:18 2022

@author: Akos
"""
#This is the agent framework for the communicating practical
#
#Import libaries
import random

#Create class
class Agent():

    # Set random coordinates for agents
    # Create storage for agents
    # Set agents and environment lists 
    def __init__(self, environment, agents):
        self.environment = environment
        self.store = 0
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.agent = agents
        
    #Function to move coordinates randomly    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    # Make agents eat all numbers on the square their on        
    def eat(self): 
        if self.environment[self.y][self.x] > 0:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
    
    # Make agents throw up if storage is more than 250
    def vommit(self):
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
            
    # Calculate distance between agents         
    def distance_between(self, agent):
         return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    #Function calculate the distance between agents
    #When two agents are close their storage = average 
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agent:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
               sum = self.store + agent.store
               ave = sum/2
               self.store = ave
               agent.store = ave
               # TEST print("sharing " + str(distance) + " " + str(ave))
                    
        
   

        
        
        
        
        
        
        