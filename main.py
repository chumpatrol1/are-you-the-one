'''
INSTRUCTIONS FOR EVERY RELEASE
Update Game Stats Version
Update Setup.py Game Version
python setup.py bdist_msi
Install the Game
Add Missing Resources/Files
Update the Changelog
ZIP the files together for release!
'''

'''OPTIMIZING'''
#python -m cProfile -o out.prof main.py
#snakeviz out.prof
'''CREATING AN INSTALLER'''
#python setup.py bdist_msi

import os
from sys import argv
#COMMENT THIS OUT WHEN MAKING THE EXE
#os.chdir(os.path.dirname(argv[0]))

cwd = os.getcwd()
print("MAIN",cwd)

import pygame as pg
from engine.game_handler import update_game_state as ugs
import resources.graphics_engine.display_graphics as dg
import resources.sound_engine.handle_sound as hs
import sys
import engine.handle_input
from json import loads, dumps
import time
game_state = "main_menu"
new_game_state = "main_menu"

done = False

def handle_input():
    engine.handle_input.get_keypress()

def get_game_state(game_state, cwd):
    return ugs(game_state, cwd)

def display_graphics(game_state, cwd, info_getter):
    dg.handle_graphics(game_state, cwd, info_getter)

def handle_sound(game_state):
    hs.handle_sound(game_state)

clock = pg.time.Clock()
def run():
    global done
    global clock
    global game_state
    global cwd
    clock.tick_busy_loop(60)
    handle_input()
    new_game_state, info_getter, bgm_song = get_game_state(game_state, cwd)
    display_graphics(game_state, cwd, info_getter)
    #handle_sound(bgm_song)
    game_state = new_game_state
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    pressed =  pg.key.get_pressed()
    if(pressed[pg.K_ESCAPE]):
        done = True #Ends the game
    if(game_state == "quit"):
        done = True
        
    '''Runs the program'''
    return game_state

while not done:
    game_state = run()
else:
    print("All done!")
    pg.quit()
    sys.exit()
        