from resources.graphics_engine.background_handler import draw_background as draw_background
from engine.simulation import return_truth as return_truth
from engine.simulation import return_round as return_round
from engine.simulation import return_tb_pair as return_tb_pair
from engine.simulation import return_decision as return_decision
import pygame as pg
from os import getcwd
cwd = getcwd()
print(cwd)

boxes = {
    'black': pg.image.load(cwd + '/resources/images/boxes/black_box.png'),
    'green': pg.image.load(cwd + '/resources/images/boxes/green_box.png'),
    'red': pg.image.load(cwd + '/resources/images/boxes/red_box.png'),
    'text_small': pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 40),
    'text_big': pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80),
}

def draw_simulation_initial(game_display):
    draw_background(game_display, 'main_menu')

color_to_tuple = { # Translates meeple name into tuple
    'brown': (125, 50, 0),
    'maroon': (50, 0, 0),
    'red': (255, 0, 0),
    'orange': (255, 124, 0),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'forest': (0, 125, 0),
    'navy': (0, 0, 125),
    'blue': (0, 0, 255),
    'cyan': (0, 255, 255),
    'purple': (125, 0, 125),
    'magenta': (255, 0, 255),
    'pink': (255, 125, 255),
    'white': (255, 255, 255),
    'gray': (125, 125, 125),
    'black': (0, 0, 0)
}

def increment_meeple(meeple_x, meeple_y):
    meeple_x += 200
    if(meeple_x > 1200):
        meeple_y += 200
        if(meeple_y == 600):
            meeple_x = 400
        else:
            meeple_x = 200
    return meeple_x, meeple_y

def draw_simulation_initial_wait(game_display, info_getter):
    draw_background(game_display, 'main_menu')
    meeple_x = 200
    meeple_y = 200
    for meeple in info_getter:
        pg.draw.circle(game_display, color_to_tuple[meeple.color], (meeple_x, meeple_y), 75)
        if(meeple.color == "black"):
            pg.draw.circle(game_display, color_to_tuple['white'], (meeple_x, meeple_y), 75, width = 5)
        else:
            pg.draw.circle(game_display, color_to_tuple['black'], (meeple_x, meeple_y), 75, width = 5)

        meeple_x, meeple_y = increment_meeple(meeple_x, meeple_y)

def draw_simulation_logic(game_display, info_getter):
    draw_background(game_display, 'main_menu')
    meeple_x = 200
    meeple_y = 200
    for pair in info_getter.return_pairings():
        box_x = meeple_x - 90
        box_y = meeple_y + 50
        for meeple in pair.return_meeple():
            pg.draw.circle(game_display, color_to_tuple[meeple.color], (meeple_x, meeple_y), 75)
            if(meeple.color == "black"):
                pg.draw.circle(game_display, color_to_tuple['white'], (meeple_x, meeple_y), 75, width = 5)
            else:
                pg.draw.circle(game_display, color_to_tuple['black'], (meeple_x, meeple_y), 75, width = 5)


            meeple_x, meeple_y = increment_meeple(meeple_x, meeple_y)

        if(pair.check_match()):
            if(pair in return_truth()):
                pairing_box = boxes['green']
            else:
                pairing_box = boxes['black']

        else:
            if(pair == return_tb_pair() or len(return_truth()) == return_decision().return_match_num()):
                pairing_box = boxes['red']
            else:
                pairing_box = boxes['black']

        game_display.blit(pairing_box, (box_x, box_y))
        
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80)
    text_box = menu_font.render('Correct Matches: ' + str(info_getter.return_match_num()), False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 75)
    game_display.blit(text_box, text_rect)

def draw_simulation_win(game_display, info_getter):
    draw_background(game_display, 'main_menu')
    meeple_x = 200
    meeple_y = 200
    for pair in info_getter.return_pairings():
        box_x = meeple_x - 90
        box_y = meeple_y + 50
        for meeple in pair.return_meeple():
            pg.draw.circle(game_display, color_to_tuple[meeple.color], (meeple_x, meeple_y), 75)
            if(meeple.color == "black"):
                pg.draw.circle(game_display, color_to_tuple['white'], (meeple_x, meeple_y), 75, width = 5)
            else:
                pg.draw.circle(game_display, color_to_tuple['black'], (meeple_x, meeple_y), 75, width = 5)


            meeple_x, meeple_y = increment_meeple(meeple_x, meeple_y)


        if(pair in return_truth()):
            pairing_box = boxes['green']
        else:
            pairing_box = boxes['black']


        game_display.blit(pairing_box, (box_x, box_y))
        
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80)
    text_box = menu_font.render('Won in ' + str(return_round()) + " Rounds!", False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 75)
    game_display.blit(text_box, text_rect)