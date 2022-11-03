# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:27:34 2022

@author: sgabalog
"""


import agentframeworkG
import requests
import bs4
import random



num_agents = 1
agents = []
environment = []

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text

soup = bs4.BeautifulSoup(content, 'html.parser')

#define values of y and x from table
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


for i in range(num_agents):
    if (i>=len(td_ys)):
        y = random.randint(0,99)
        x = random.randint(0,99)
    else:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
    agents.append(agentframeworkG.Agent(environment, agents, y, x))
    
for i in range(num_agents):
    agents[i].move()