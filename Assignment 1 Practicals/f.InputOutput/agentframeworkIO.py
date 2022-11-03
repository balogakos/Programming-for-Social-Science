# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:56:18 2022

@author: Akos
"""


import random

class Agent():

    #make init to set up agent and create coordinates
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
    #create move function to move coordinates randomly    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    #eat environment, everything on square        
    def eat(self):
        if self.environment[self.y][self.x] > 0:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0

    #vommit if eaten 100 or more
    def vommit(self):
        
        if self.store >= 250:
            print(self.store)
            self.environment[self.y][self.x] += self.store
            self.store = 0
            print(self.store)
    #clear output file 
    def clear(self):
        with open("output.txt",'w') as file:
            pass
    #add self store to new file      
    def output(self):
        f = open("output.txt", "a+")
        a = str(self.store)
        f.write(a + "\n")
        f.close()
            