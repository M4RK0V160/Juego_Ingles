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
    def __init__(self, stage_dic):
        self.stage_dic = stage_dic   
        
        
    def startup_game(self):
        global ACTUAL_STAGE
        ACTUAL_STAGE = 'start_stage'
        
        
    def main_game_control(self):
        global ACTUAL_STAGE
        self.run_event(ACTUAL_STAGE)
        
                
    def run_event(self, stage_tag):
        
        #set all button paths to the current stage and the set the correct button path to the next state
        for tag in STAGE_DIC[stage_tag].button_tag_list:
            BUTTON_DIC[tag].next_stage = stage_tag
        BUTTON_DIC[STAGE_DIC[stage_tag].right_option].next_stage = STAGE_DIC[stage_tag].right_option_path
        
        
        #display event
        STAGE_DIC[stage_tag].display()      
#-------------------------------------------------------
#
#
#
#CONSTANT DECLARATION-----------------------------------
#             X,  Y
RESOLUTION = (800,700)
FPS = 30
MAIN = True


IMG_DIC = {'happy_girlA':'IMG1a.png','happy_girlB':'IMG1b.png','happy_girl_options':'OPT_IMG1.png', 'start_stage':'IMG2.png', 'emotions_square': 'OPT_SQR.png'}

SCREEN = pygame.display.set_mode([RESOLUTION[0],RESOLUTION[1]])
SCREENBOX = SCREEN.get_rect()
SCREEN_MANAGER= Screen_Manager(IMG_DIC)

#-------------------------------------------------------
#
#
#
#MULTY-INSTANCE CLASS DEFINITION------------------------
class Stage:
    def __init__(self, name, options_tag, right_option, right_option_path, option_position, option_size, button_tag_list):
        self.name = name
        self.right_option = right_option
        self.option_position = option_position
        self.option_size = option_size
        self.options_tag = options_tag
        self.button_tag_list = button_tag_list
        self.right_option_path = right_option_path
        

    def display(self):
        SCREEN_MANAGER.display(self.name, (0,0), RESOLUTION)
        if self.options_tag != None:
            SCREEN_MANAGER.display(self.options_tag, self.option_position, self.option_size)
        
        
class Button:
    def __init__(self, pos, size, bgcolor, next_stage):
        self.x, self.y = pos
        self.size = size
        self.bgcolor = bgcolor
        self.next_stage = next_stage
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.bgcolor)
        
    def show(self):
        SCREEN.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    update_stage(self.next_stage)
                    self.show()
#-------------------------------------------------------
#
#
#
#AUXILIARY FUNCTIONS------------------------------------
def button_tracker(stage, event):
    for tag in STAGE_DIC[stage].button_tag_list:
        BUTTON_DIC[tag].click(event)

def update_stage(stage):
    global ACTUAL_STAGE
    ACTUAL_STAGE = stage;
    
def reset_buttons():
    global BUTTON_DIC
    for button in BUTTON_DIC:
        BUTTON_DIC[button].next_stage = 'happy_girlA'
#-------------------------------------------------------
#
#
#
#SETUP--------------------------------------------------
start_stage = Stage('start_stage',None, 'start_button','happy_girlA', (0,0),(300,300), ['start_button'])

happy_girlA = Stage('happy_girlA','emotions_square' , 'button11','happy_girlB' , (400,300),(100,100), ['button11','button21','button12','button22'])
happy_girlB = Stage('happy_girlB','happy_girl_options' , 'button22','start_stage' , (400,300),(100,100), ['button11','button21','button12','button22'])



start_button = Button((185,365),(400,200),(20,20,200),'happy_girl')

button11 = Button((400,300),(200,190),(20,20,200),'happy_girl')
button21 = Button((400,490),(200,190),(20,20,200),'happy_girl')
button12 = Button((600,300),(200,190),(20,20,200),'happy_girl')
button22 = Button((600,490),(200,190),(20,20,200),'happy_girl')


ACTUAL_STAGE = 'start_stage'
STAGE_DIC = {'start_stage': start_stage,'happy_girlA':happy_girlA, 'happy_girlB': happy_girlB }
BUTTON_DIC = {'start_button':start_button,'button11':button11,'button21':button21,'button12':button12,'button22':button22}

EVENT_MANAGER = Event_Manager(STAGE_DIC)
clock = pygame.time.Clock()
pygame.init()

EVENT_MANAGER.startup_game()
#-------------------------------------------------------
#
#
#
#MAIN LOOP----------------------------------------------
while MAIN:
    
    EVENT_MANAGER.main_game_control()

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
        
           
    
        button_tracker(ACTUAL_STAGE,event) 
    reset_buttons() 
    
    x, y = pygame.mouse.get_pos()
    print("(" + str(x) + "," + str(y) + ")")
    
    pygame.display.flip()  
    clock.tick(FPS)
#-------------------------------------------------------








