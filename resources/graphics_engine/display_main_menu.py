from resources.graphics_engine.background_handler import draw_background as draw_background
import pygame as pg
from os import getcwd
cwd = getcwd()

menu_memory = {
    'ball': pg.transform.scale(pg.image.load(cwd + "/resources/images/balls/selector_ball.png"), (76, 76)),
}

def draw_main_menu(game_display, selector_position):
    draw_background(game_display, 'main_menu')
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 40)
    # Attempting to store this font in a global dict/cache causes a crash for some reason
    text_array = [
        menu_font.render('Start!', False, (0, 0, 150)),
        menu_font.render('Credits', False, (0, 0, 150)),
        menu_font.render('Quit', False, (0, 0, 150)),
        menu_font.render('Arrows/WASD to Navigate', False, (0, 0, 150)),
        menu_font.render('Enter to Select', False, (0, 0, 150)),
    ]

    game_display.blit(menu_memory['ball'], (850, (76 * (selector_position + 4)) + 38))

    text_y = 76 * 5
    for text_box in text_array:
        text_rect = text_box.get_rect()
        text_rect.center = (683, text_y)
        game_display.blit(text_box, text_rect)
        text_y += 76
    
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80)
    text_box = menu_font.render('Are You the One?', False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 200)
    game_display.blit(text_box, text_rect)