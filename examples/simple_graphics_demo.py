# -*- coding: utf-8 -*-
__author__ = 'Administrator'
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
'''
作图，画一些简单的图形。
'''

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

pi=3.141592653

# Set the height and width of the screen
size=[400,500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

#Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()

while done==False:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(white)

    # Draw on the screen a green line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen,green,[0,0],[100,100],5)

    # Draw on the screen several green lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    y_offset=0
    while y_offset < 100:
        pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
        y_offset=y_offset+10

    # Select the font to use. Default font, 25 pt size.
    font = pygame.font.Font(None, 25)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("My text",True,black)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250,250])

    # Draw a rectangle
    pygame.draw.rect(screen,black,[20,20,250,100],2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen,black,[20,20,250,100],2)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen,black,[20,220,250,200], 0, pi/2, 2)
    pygame.draw.arc(screen,green,[20,220,250,200], pi/2, pi, 2)
    pygame.draw.arc(screen,blue, [20,220,250,200], pi,3*pi/2, 2)
    pygame.draw.arc(screen,red, [20,220,250,200],3*pi/2, 2*pi, 2)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen,black,[[100,100],[0,200],[200,200]],5)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit ()