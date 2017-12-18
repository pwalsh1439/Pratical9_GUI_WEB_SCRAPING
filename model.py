# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:19:14 2017

@author: Paul
"""

import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import tkinter
import bs4
import requests



num_of_agents = 10
num_of_iterations = 100
agents = []
environment = []
neighbourhood = 20




r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

soup = bs4.BeautifulSoup(content, 'html.parser') 
tdsy = soup.find_all(attrs={"class" : "y"})
tdsx = soup.find_all(attrs={"class" : "x"})

"""
print ("Y column")
print (tdsy) 
print ("x column")
print (tdsx) 
"""

"""    
tdsz= soup.find_all(attrs={"class" : "z"})
print ("z column")
for td in tdsz:
    print (td.text) 
"""

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show()
#

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])    
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fil=tkinter.BOTH, expand=1)




menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Run Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


with open(r"Z:\D\Workspace\Personal\UNI\Year2_Modules\Programming\python\src\unpackaged\abm\in.txt", newline="") as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist=[]
        for values in row:
            rowlist.append(values)
        environment.append(rowlist)

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
 
max_enviroment = max(environment)[0]

  
#print("********** " + str(max_enviroment))     
#print(type(max_enviroment))
# Make the agents.
for i in range(num_of_agents):
    y = int(tdsy[i].text)
    x = int(tdsx[i].text)
    agents.append(agentframework.Agent(environment, max_enviroment, agents, y, x))
   # print(agents[i].x)

   
def update(frame_number):
    
    fig.clear()
    
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            #agents[i].eat()
            #[i].share_with_neighbours(neighbourhood)
        
            matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
            
tkinter.mainloop()
        
#print("here " + str(agents[i].x))

#for ag in agents:
#    print(ag.store)

#matplotlib.pyplot.xlim(0, max_enviroment)
#matplotlib.pyplot.ylim(0, max_enviroment)
#matplotlib.pyplot.imshow(environment)

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#matplotlib.pyplot.show()


#for agent0 in agents:
 #   for agent1 in agents:
  #      distance = distance_between(agent0, agent1) 
 
"""       
# write out enviroment data to out.txt
with open("out.txt", "w", newline="") as f2:
    writer = csv.writer(f2, delimiter=",") 
    for row in environment:
        writer.writerow(row)
        
with open("Store.txt", "a", newline="") as f3:
    writer = csv.writer(f3, delimiter=",")
    storelist = []
    for agent in agents:
        storelist.append(agent.store)
    writer.writerow(storelist)           

# Get each agent to tell its x location and the x location of agent6
#proves each agent has a list of each other agents
for singleagent in agents:
    myx = singleagent.x
    print("my x is " + str(myx))
   # print("my store is " + str(singleagent.store))
    agent6x = singleagent.otheragents[5].x
    print("agent 6 x is " + str(agent6x))
"""