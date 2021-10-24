#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Attack_object:
    def __init__(self,surface,x,y):
        self.surface=surface
        self.x=x
        self.y=y
        self.Collision=False
    def player_pos(self,pos):
        self.player=pos
    def add(self,addx=0,addy=0):
        self.x+=addx
        self.y+=addy
    def return_x(self):
        return self.x
    def return_y(self):
        return self.y
    def collision(self):
        return self.Collision
    def update(self):
        pass

class Attack:
    def __init__(self,surface,x,y):
        self.surface=surface
        self.x=x
        self.y=y
        self.Collision=False
    def player_pos(self,pos):
        self.player=pos
    def collision(self):
        return self.Collision
    def update():
        pass