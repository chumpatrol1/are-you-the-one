import pygame as pg
import sys
import engine.handle_input
from engine.handle_input import reset_inputs
from json import dumps
from os import getcwd
cwd = getcwd()

pg.init()
clock = pg.time.Clock()
clock.tick(60)

selector_position = 0
p1_selector_position = [4, 2, 0, 0] #0 is unselected, 1 is selected, 2 is confirmed... 0 is human, 1 is cpu
p2_selector_position = [4, 2, 0, 0] #0 is unselected, 1 is selected, 2 is confirmed... 0 is human, 1 is cpu
p1_blob = "quirkless"
p2_blob = "quirkless"

def menu_navigation(timer):
    game_state = "main_menu"
    pressed = engine.handle_input.menu_input()
    global selector_position
    if('p1_up' in pressed or 'p2_up' in pressed):
        if selector_position == 0:
            selector_position = 2
        else:
            selector_position -= 1
    elif('p1_down' in pressed or 'p2_down' in pressed):
        if selector_position == 2:
            selector_position = 0
        else:
            selector_position += 1
    if(not timer) and ('p1_ability' in pressed or 'p2_ability' in pressed or 'return' in pressed):
        if(selector_position == 0): #Casual
            game_state = "simulation_start"
        elif(selector_position == 1):
            game_state = "credits"
            selector_position = 0
        elif(selector_position == 2): #Quits the game
            game_state = "quit"
            
    return selector_position, game_state

def credits_waiter(timer):
    game_state = "credits"
    pressed = engine.handle_input.menu_input()
    if(not timer) and ('p1_ability' in pressed or 'p2_ability' in pressed or 'return' in pressed):
        game_state = "main_menu"
    return game_state

def simulation_advance(timer, game_state):
    pressed = engine.handle_input.menu_input()
    if(game_state == "simulation_start_wait"):
        if(not timer) and ('p1_ability' in pressed or 'p2_ability' in pressed or 'return' in pressed):
            game_state = "simulation_logic"
    elif(game_state == "simulation_logic_wait"):
        if(not timer) and ('p1_ability' in pressed or 'p2_ability' in pressed or 'return' in pressed):
            game_state = "simulation_logic"
    
    return game_state