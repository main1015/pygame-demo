# -*- coding: utf-8 -*-
from game.event.mouse import Mouse
from game.role import RoleIcon
from game.util import load_character

__author__ = 'Administrator'


background_image_filename = '../icon/fighting-bg/bg_Z001[1].jpg'
mouse_image_filename = '../icon/character/summoner.png'
#指定图像文件名称
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

pygame.init()
#初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((1260, 660), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题

background = pygame.image.load(background_image_filename).convert()
# mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# _mouse_cursor = load_character(mouse_image_filename,100,120,8,4)
mouse_cursor = RoleIcon(mouse_image_filename)
allsprites = pygame.sprite.RenderPlain()
allsprites.add(mouse_cursor)
# mouse_cursor  = _mouse_cursor[0]
#加载并转换图像

clock=pygame.time.Clock()

while True:
#游戏主循环

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            exit()
        met = Mouse(event)
        met.click_move(mouse_cursor)

    screen.blit(background, (0,0))
    #将背景图画上去

    # x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    # x-= mouse_cursor.get_width() / 2
    # y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    # screen.blit(mouse_cursor, (150, 300))
    #把光标画上去
    allsprites.draw(screen)
    if mouse_cursor.isOver:
        current_time = pygame.time.get_ticks()
        mouse_cursor.update(current_time)
        screen.blit(mouse_cursor.image, mouse_cursor.rect)

    clock.tick(60)
    pygame.display.update()
    #刷新一下画面