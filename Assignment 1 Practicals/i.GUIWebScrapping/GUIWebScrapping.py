# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:03:31 2022

@author: Akos
"""
# Import libaries
import csv
import agentframeworkG
import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import matplotlib.animation
import requests
import bs4
from tkinter import simpledialog
import doctest

#WebScraping website for coordinates
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

#Fefine values of y and x from table
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# Move agents, communicate, eat, and animate        
def update(frame_number):
    '''
    Function clears plot, then for in the range of iterations and then agents
    moves agents, while making them eat, vommit, and share locations with
    eachother
    
    Function also moves agents and if they are near sheep(agents) the wovles
    eat the sheep
    
    Then the function creates the plot and plots the environment, wolves
    and sheep (agents) on it

    '''
    global carry_on
    fig.clear()
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
        agent.vommit()
        
    for wolf in wolves:
        wolf.movewolf()
        wolf.eat_sheep(neighbourhood, wolves, agents)
        
    # Update and visualise the placement of agents on pyplot
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
    for agent in agents:
        matplotlib.pyplot.scatter(agent.x,agent.y)
    for wolf in wolves:
        matplotlib.pyplot.scatter(wolf.x,wolf.y, c = 'red', marker='*')
        
def gen_function(b = [0]):
    '''
    Function for animation

    Parameters
    ----------
    a : Integer
    Starts at zero, increases by 1 each time
    
    Testing
    >>>a = 1
    2

    '''
    a = 0
    global carry_on
    while (a < 100) & (carry_on) :
        yield a   
        a = a + 1
        


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                                                   frames=gen_function, 
                                                   repeat=False)
    canvas.draw()

def exit_mod():
    global root
    root.destroy()

# Set number of agents and iterations from the user
num_agents = int(simpledialog.askstring(title="Number of sheep",
                                  prompt="How many sheep?:"))
num_wolves = int(simpledialog.askstring(title="Number of Wolves",
                                  prompt="How many hungry wolves?:"))
neighbourhood = 20

#Create lists for agents and environment
environment = []
agents = []
wolves = []

#Create GUI
root = tkinter.Tk()

# Open text and read through it, adding it to environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        #print(agents)

# Create pyplot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#
for i in range(num_agents):
    if (i>=len(td_ys)):
        y = random.randint(0,299)
        x = random.randint(0,299)
    else:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
    agents.append(agentframeworkG.Agent(environment, agents, y, x))

for i in range(num_wolves):
    wolves.append(agentframeworkG.Wolf(environment,
                                       neighbourhood, y, x))
    
carry_on = True

#Create model tittle and canvas in GUI
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Create run model button in GUI
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Run", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

#Exit the model
exit_menu = tkinter.Menu(menu)
menu.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Exit model", command=exit_mod)

tkinter.mainloop()