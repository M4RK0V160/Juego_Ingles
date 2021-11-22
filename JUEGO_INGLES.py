
import subprocess
import sys
mport os
import time

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
    
install('pygame')


import pygame
from pygame import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)





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
        
        
class Stage_Manager:
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
DEV_MODE = False

IMG_DIC = {'start_stage':'IMG2.png','restart_stage': 'IMG2b.png','emotions_square': 'OPT_SQR.png','welldone':'WELL_DONE.png',
           'happy_girlA':'IMG1a.png','happy_girlB':'IMG1b.png','happy_girl_options':'OPT_IMG1.png','scared_boyA':'IMG3a.png',
           'scared_boyB':'IMG3b.png','scared_boy_options':'OPT_IMG3.png','angry_boyA':'IMG4a.png','angry_boyB':'IMG4b.png',
           'angry_boy_options':'OPT_IMG4.png','sad_girlA':'IMG5a.png', 'sad_girlB':'IMG5b.png','sad_girl_options':'OPT_IMG5.png'
           }

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
    global ACTUAL_STAGE, NEXT_STAGE
    ACTUAL_STAGE = stage;
    
def reset_buttons():
    global BUTTON_DIC
    for button in BUTTON_DIC:
        BUTTON_DIC[button].next_stage = 'happy_girlA'
        
def Aux_Sceen_info():
    global DEV_MODE, STAGE_DIC, ACTUAL_STAGE
    if DEV_MODE:
        stage_name = myfont.render(('STAGE_NAME:' + STAGE_DIC[ACTUAL_STAGE].name),True,(0,0,0))
        stage_correct_option = myfont.render(('CORRECT_OPTION:' + STAGE_DIC[ACTUAL_STAGE].right_option),True,(0,0,0))
        stage_next_path = myfont.render(('NEXT_STAGE:' + STAGE_DIC[ACTUAL_STAGE].right_option_path),True,(0,0,0))
    
        SCREEN.blit(stage_name,pygame.Rect((10,10),(100,20)))
        SCREEN.blit(stage_correct_option,pygame.Rect((10,40),(100,20)))
        SCREEN.blit(stage_next_path,pygame.Rect((10,70),(100,20)))
#-------------------------------------------------------
#
#
#
#SETUP--------------------------------------------------
ACTUAL_STAGE = 'start_stage'
NEXT_STAGE = 'start_screen'

start_stage = Stage('start_stage',None, 'start_button','happy_girlA', (0,0),(300,300), ['start_button'])

restart_stage = Stage('restart_stage',None, 'start_button','happy_girlA', (0,0),(300,300), ['start_button'])

happy_girlA = Stage('happy_girlA','emotions_square' , 'button11','welldone1' , (470,300),(100,100), ['button11','button21','button12','button22'])
welldone1 = Stage('welldone',None ,'start_button', 'happy_girlB' , (470,300),(100,100), ['start_button'])
happy_girlB = Stage('happy_girlB','happy_girl_options' , 'button22','welldone2' , (470,300),(100,100), ['button11','button21','button12','button22'])

welldone2 = Stage('welldone',None ,'start_button', 'scared_boyA' , (470,300),(100,100), ['start_button'])

scared_boyA = Stage('scared_boyA','emotions_square' , 'button12','welldone3' , (470,300),(100,100), ['button11','button21','button12','button22'])
welldone3 = Stage('welldone',None ,'start_button', 'scared_boyB' , (470,300),(100,100), ['start_button'])
scared_boyB = Stage('scared_boyB','scared_boy_options' , 'button21','welldone4' , (470,300),(100,100), ['button11','button21','button12','button22'])

welldone4 = Stage('welldone',None ,'start_button', 'angry_boyA' , (470,300),(100,100), ['start_button'])

angry_boyA = Stage('angry_boyA','emotions_square' , 'button22','welldone5' , (470,300),(100,100), ['button11','button21','button12','button22'])
welldone5 = Stage('welldone',None ,'start_button', 'angry_boyB' , (470,300),(100,100), ['start_button'])
angry_boyB = Stage('angry_boyB','angry_boy_options' , 'button11','welldone6' , (470,300),(100,100), ['button11','button21','button12','button22'])

welldone6 = Stage('welldone',None ,'start_button', 'sad_girlA' , (470,300),(100,100), ['start_button'])

sad_girlA = Stage('sad_girlA','emotions_square' , 'button21','welldone7' , (470,300),(100,100), ['button11','button21','button12','button22'])
welldone7 = Stage('welldone',None ,'start_button', 'sad_girlB' , (470,300),(100,100), ['start_button'])
sad_girlB = Stage('sad_girlB','sad_girl_options' , 'button12','restart_stage' , (470,300),(100,100), ['button11','button21','button12','button22'])


start_button = Button((185,365),(400,200),(20,20,200),'happy_girl')

button11 = Button((470,300),(165,150),(20,20,200),'happy_girl')
button21 = Button((470,450),(165,150),(20,20,200),'happy_girl')
button12 = Button((635,300),(165,150),(20,20,200),'happy_girl')
button22 = Button((635,450),(165,150),(20,20,200),'happy_girl')



STAGE_DIC = {'start_stage': start_stage,'restart_stage':restart_stage,
             'welldone1': welldone1,'welldone2': welldone2,'welldone3': welldone3,'welldone4': welldone4,'welldone5': welldone5,'welldone6': welldone6,'welldone7': welldone7,
             'happy_girlA':happy_girlA, 'happy_girlB': happy_girlB,
             'scared_boyA':scared_boyA, 'scared_boyB': scared_boyB,
             'angry_boyA':angry_boyA, 'angry_boyB': angry_boyB,
             'sad_girlA':sad_girlA, 'sad_girlB': sad_girlB,
             
             }
BUTTON_DIC = {'start_button':start_button,'button11':button11,'button21':button21,'button12':button12,'button22':button22}

STAGE_MANAGER = Stage_Manager(STAGE_DIC)
clock = pygame.time.Clock()
pygame.init()

STAGE_MANAGER.startup_game()
#-------------------------------------------------------
#
#
#
#MAIN LOOP----------------------------------------------
while MAIN:
   
    STAGE_MANAGER.main_game_control()

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:    
            if event.key == ord('w'):
                DEV_MODE = not DEV_MODE
        
        if event.type == pygame.QUIT:
            pygame.quit()
            try:

                sys.exit()
            finally:
                MAIN = False

        
            
           
        
        button_tracker(ACTUAL_STAGE,event) 
    reset_buttons() 
    
    Aux_Sceen_info()
    pygame.display.flip()  
    clock.tick(FPS)
#-------------------------------------------------------








