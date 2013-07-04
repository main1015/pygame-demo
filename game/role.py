# -*- coding: utf-8 -*-
import pygame
from wx import Rect
from gameobjects.vector2 import Vector2
from game.util import load_character

__author__ = 'Administrator'

class RoleIcon(pygame.sprite.Sprite):
    _rate = 100
    _width = 100
    _height = 120
    _X_STEP = 80
    _Y_STEP = 0

    X_STEP = _X_STEP
    Y_STEP = _Y_STEP
    _w_number = 8
    _h_number = 4
    isOver = False
    move_step = 1
    step = 0
    images = []
    MAX = 10

    def __init__(self,filename):
        self.order = 0
        pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_character(filename, self._width,self._height,self._w_number,self._h_number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._width, self._height)
        # self.life = self._life
        self.passed_time = 0
        self.rect.left = 0
        self.rect.top = 0

        self.count = 1


    def _isRun(self):
        self.count += 1
        if self.count > self.MAX:
            self.count = 1
            return True
        else:
            return False

    def update(self,current_time):




        self.move()
        # if self.passed_time < current_time:
        #     self.step += 1
        #     if self.step == self._w_number:
        #         self.step = 0
        #     self.order = self.step
        #     self.image = self.images[self.order]
        # self.rect.left,self.rect.top  = pygame.mouse.get_pos()
        #     self.move()

    def set_move(self,form_to):
        self.form_to = form_to


        x,y = self.form_to
        start_point = Vector2(self.rect.left,self.rect.top)
        end_point = Vector2(x,y)
        point = end_point - start_point
        if point:
            self.isOver = True
            self.move_step = self._get_step(point[0])



    def move(self):
        if self._isRun():
            self.step += 1
            if self.step == self._w_number:
                self.step = 0
            self.order = self.step
            self.image = self.images[self.order]
            if self.isOver:
                self._move()

    def _move(self):

        x,y = self.form_to
        start_point = Vector2(self.rect.left,self.rect.top)
        end_point = Vector2(x,y)
        point = end_point - start_point

        self.Y_STEP = (point[1]//self.move_step) if self.move_step else 0
        if point[0]*self.X_STEP<0:
            self.X_STEP = -self.X_STEP
        if point[1]*self.Y_STEP<0:
            self.Y_STEP = -self.Y_STEP

        self.move_step = self.move_step-1 if self.move_step-1 >=1 else 1


        if self.move_step == 1:

            self.isOver = False
            self.X_STEP = self._X_STEP
            self.Y_STEP = self._Y_STEP
            self.rect.left = x
            # if self.rect.top>=y:
            self.rect.top = y
        else:
            self.rect.left += self.X_STEP
            self.rect.top += self.Y_STEP

        print '~'*20,self.rect.left,self.rect.top,self.X_STEP,self.Y_STEP,self.move_step,x,y


    def _get_step(self,distance):
        steps = abs(distance // self.X_STEP)
        if distance % self.X_STEP !=0:
            steps += 1

        return steps








