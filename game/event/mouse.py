# -*- coding: utf-8 -*-
import pygame

__author__ = 'Administrator'



class Mouse(object):


    def __init__(self,event):
        self.event = event

    def click_move(self,obj):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            x,y = pygame.mouse.get_pos()
            obj.set_move((x,y))


