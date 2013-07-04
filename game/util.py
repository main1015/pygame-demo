# -*- coding: utf-8 -*-
import pygame
from wx import Rect

__author__ = 'Administrator'


def load_character(file, width,height, w_number,h_number):
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if width == None:
        return surface

    images = []
    for i in xrange(h_number):
        for j in xrange(w_number):
            images.append(surface.subsurface(Rect(j*width,i*height,width,height)))
    return  images

    # return [surface.subsurface(
    #     Rect((i * width, i*height), (width, height))
    # ) for i in xrange(number)]