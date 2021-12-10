from resources.graphics_engine.background_handler import draw_background as draw_background
import pygame as pg
from os import getcwd
cwd = getcwd()

def draw_credits_screen(game_display):
    draw_background(game_display, 'main_menu')
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 40)
    text_array = [
        menu_font.render('Program by Elijah "chumpatrol1" McLaughlin', False, (0, 0, 150)),
        menu_font.render('Background Art by "Ellexium"', False, (0, 0, 150)), # He's an online friend, I don't wanna dox him without permission
        menu_font.render('Assigned by Professor Jake Scoggin', False, (0, 0, 150)),
        menu_font.render('CSE2050 Honors Assignment', False, (0, 0, 150))
    ]

    text_y = 76 * 5
    for text_box in text_array:
        text_rect = text_box.get_rect()
        text_rect.center = (683, text_y)
        game_display.blit(text_box, text_rect)
        text_y += 76
    
    menu_font = pg.font.Font(cwd + "/resources/fonts/neuropol-x-free.regular.ttf", 80)
    text_box = menu_font.render('Credits', False, (0, 0, 150))
    text_rect = text_box.get_rect()
    text_rect.center = (683, 200)
    game_display.blit(text_box, text_rect)