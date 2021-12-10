import pygame as pg
import os
import ctypes

from pygame import image
from pygame.constants import FULLSCREEN, RESIZABLE
from engine.handle_input import toggle_fullscreen
from resources.graphics_engine.display_credits import draw_credits_screen
from resources.graphics_engine.display_main_menu import draw_main_menu
from json import loads, dumps
from resources.graphics_engine.display_simulation import draw_simulation_initial, draw_simulation_initial_wait, draw_simulation_logic, draw_simulation_win
cwd = os.getcwd()
pg.quit()
os.environ['SDL_VIDEO_CENTERED'] = '1'

x = 100
y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pg.init()

try:
    user32 = ctypes.windll.user32
    real_screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
except:
    print("Real Screen Size Exception")
    real_screen_size = (960, 540)

display_width = 1024
display_height = 576

pg.display.set_caption('Are You the One?')
game_display = pg.display.set_mode((display_width, display_height)) # The canvas
game_surface = pg.Surface((1366, 768))
pg.display.set_icon(pg.image.load(cwd+"/resources/images/ico_blob.ico"))
game_stats = ()
previous_screen = ""
toggle_timer = 0
full_screen = False
def handle_graphics(game_state, main_cwd, info_getter):
    global real_screen_size
    global game_surface
    global game_display
    global p1_blob
    global p2_blob
    global p1_is_cpu
    global p2_is_cpu
    global cwd
    global timer
    global ruleset
    global game_stats
    global previous_screen

    screen_size = (1366, 768)
    cwd = main_cwd
    if(game_state == "main_menu"):
        selector_position = info_getter[0]
        draw_main_menu(game_surface, selector_position)
    elif(game_state == "credits"):
        draw_credits_screen(game_surface)
    elif(game_state == "simulation_start"):
        draw_simulation_initial(game_surface)
    elif(game_state == "simulation_start_wait"):
        draw_simulation_initial_wait(game_surface, info_getter)
    elif(game_state == "simulation_logic" or game_state == "simulation_logic_wait"):
        draw_simulation_logic(game_surface, info_getter)
    elif(game_state == "simulation_win"):
        draw_simulation_win(game_surface, info_getter)
    
    global toggle_timer
    global full_screen
    global display_height, display_width
    if(toggle_timer > 0):
        toggle_timer -= 1
    else:
        toggle = toggle_fullscreen()
        if(toggle):
            if(full_screen):
                pg.display.quit()
                pg.display.init()
                pg.display.set_caption('Are You the One?')
                game_display = pg.display.set_mode((display_width, display_height))
                full_screen = False
            else: 
                game_display = pg.display.set_mode(real_screen_size, FULLSCREEN)
                display_width = 1024
                display_height = 576
                full_screen = True
            
            toggle_timer = 10


    if(full_screen):
            game_display.blit(pg.transform.scale(game_surface, (real_screen_size[0], real_screen_size[1])), (0, 0))
    else:
        for event in pg.event.get():
            if(event.type == pg.VIDEORESIZE):
                display_width, display_height = event.w, event.h
            game_display.blit(pg.transform.scale(game_surface, (display_width, display_height)), (0, 0))
    pg.display.flip()
