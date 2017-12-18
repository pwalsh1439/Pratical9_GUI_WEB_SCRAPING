# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:24:59 2017

@author: Paul
"""
import random


#
class Agent():
    def __init__(self, environment, max_environment, agents, iny, inx):
       #self._x = random.randint(0,max_environment)
        #self._y = random.randint(0,max_environment)
        self.environment = environment
        self.max_environment = max_environment
        self.store = 0
        #print(type(self.max_environment))
        self.otheragents = agents
        if (inx == None):
            self._x = random.randint(0,max_environment)
        else:    
            self.x = inx
         
        if (iny == None):
            self._y = random.randint(0,max_environment)
        else:
            self.y = iny 
        
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def setx(self, value):
        self._x = value
    def sety(self, value):
        self._y = value  
    x = property(getx, setx, "I'm the 'x' property.")     
    y = property(gety, sety, "I'm the 'y' property.")  

    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % int(self.max_environment)
        else:
            self._y = (self._y - 1) % int(self.max_environment)

        if random.random() < 0.5:
            self._x = (self._x + 1) % int(self.max_environment)
        else:
            self._x = (self._x - 1) % int(self.max_environment)
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -=10
            self.store += 10
        elif self.environment[self.y][self.x] < 10:
            self.store += self.environment[self.y]
            self.store += self.environmentS[self.x]
            self.environment[self.y][self.x] = 0
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.otheragents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                storesum = self.store + agent.store
                storeaverage = storesum / 2 
                self.store = storeaverage
                agent.stroe = storeaverage
               # print("sharing " + str(distance) + " " + str(storeaverage))
                
        
    def distance_between(self, agent1):
        return (((self.x - agent1.x)**2) + ((self.y - agent1.y)**2))**0.5
    
    
    