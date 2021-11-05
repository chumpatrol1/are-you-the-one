from resources.graphics_engine.background_handler import draw_background as draw_background
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

def draw_main_menu(game_display, selector_position):
    draw_background(game_display, 'main_menu')
    menu_font = boxes['text']
    text_array = [
        menu_font.render('Start!', False, (0, 0, 150)),
        menu_font.render('Credits', False, (0, 0, 150)),
        menu_font.render('Quit', False, (0, 0, 150))
    ]


    ball = pg.image.load(cwd + "/resources/images/balls/selector_ball.png")
    ball = pg.transform.scale(ball, (76, 76))
    game_display.blit(ball, (850, (76 * (selector_position + 4)) + 38))

    text_y = 76 * 5
    for text_box in text_array:
        text_rect = text_box.get_rect()
        text_rect.center = (683, text_y)
        game_display.blit(text_box, text_rect)
        text_y += 76
    
    menu_font = boxes['text_big']
    text_box = menu_font.render('Are You the One?', False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 200)
    game_display.blit(text_box, text_rect)

def draw_simulation_initial(game_display):
    draw_background(game_display, 'main_menu')

color_to_tuple = {
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


        meeple_x += 200
        if(meeple_x > 1200):
            meeple_y += 200
            if(meeple_y == 600):
                meeple_x = 400
            else:
                meeple_x = 200

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


            meeple_x += 200
            if(meeple_x > 1200):
                meeple_y += 200
                if(meeple_y == 600):
                    meeple_x = 400
                else:
                    meeple_x = 200

        if(pair.check_match()):
            pairing_box = boxes['green']
        else:
            pairing_box = boxes['red']

        game_display.blit(pairing_box, (box_x, box_y))
        
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80)
    text_box = menu_font.render('Correct Matches: ' + str(info_getter.return_match_num()), False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 100)
    game_display.blit(text_box, text_rect)