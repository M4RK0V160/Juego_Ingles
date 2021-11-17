

import math
import random

import pygame
from pygame import *

import sys
import os

#SET WORKING DIRECTORY TO THE  FILE'S PATH IN THE CURRENT SYSTEM 
os.chdir(os.path.dirname(__file__))
#-------------------------------------------------------
#
#
#
#MANAGER CLASS DEFINITION DEFINITION--------------------
class Screen_Manager:
    def __init__(self, img_dic):
        
        self.RES = RESOLUTION
        
        self.img_dic = img_dic
        
    def display(self, img_tag, pos, size):
        IMG  = pygame.image.load(self.img_dic[img_tag])
        SCREEN.blit(IMG, pygame.Rect(pos,size))
        
        
class Event_Manager:
    def __init__(self, event_dic):
        self.event_dic = event_dic   
        
    def run_event(self, event_tag):
        EVENT_DIC[event_tag].display()      
#-------------------------------------------------------
#
#
#
#CONSTANT DECLARATION-----------------------------------
#             X,  Y
RESOLUTION = (800,700)
FPS = 30
MAIN = True

IMG_DIC = {'happy_girl':'IMG1.png','options_square':'OPT_SQR.png'}

SCREEN = pygame.display.set_mode([RESOLUTION[0],RESOLUTION[1]])
SCREENBOX = SCREEN.get_rect()
SCREEN_MANAGER= Screen_Manager(IMG_DIC)
#-------------------------------------------------------
#
#
#
#MULTY-INSTANCE CLASS DEFINITION------------------------
class Stage:
    def __init__(self, name, right_option, option_position, option_size):
        self.name = name
        self.right_option = right_option
        self.option_position = option_position
        self.option_size = option_size
    

    def display(self):
        SCREEN_MANAGER.display(self.name, (0,0), RESOLUTION)
        SCREEN_MANAGER.display('options_square', self.option_position, self.option_size)
#-------------------------------------------------------
#
#
#
#SETUP--------------------------------------------------
event1 = Stage('happy_girl', 1 , (600,700),(100,100))

EVENT_DIC = {'event1': event1}
EVENT_MANAGER = Event_Manager(EVENT_DIC)

clock = pygame.time.Clock()
pygame.init()
#-------------------------------------------------------
#
#
#
#MAIN LOOP----------------------------------------------
while MAIN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                MAIN = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                MAIN = False
                
    EVENT_MANAGER.run_event('event1')   
     
    pygame.display.flip()  
    clock.tick(FPS)
#-------------------------------------------------------







