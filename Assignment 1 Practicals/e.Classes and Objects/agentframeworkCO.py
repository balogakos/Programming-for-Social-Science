# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:51:53 2022

@author: Akos
"""
#import libaries
import random

#Create Agent class
class Agent():

    #Make "init" to set up agent and create coordinates
    def __init__(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
    #Create move function to move coordinates randomly    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
            