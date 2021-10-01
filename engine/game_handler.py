from json import loads, dumps
import engine.menu

timer = 0

def update_game_state(game_state, cwd):
    global timer

    music = "main_menu"
    if(game_state == "main_menu"):
        if(timer > 0):
            timer -= 1
        info_getter = engine.menu.menu_navigation(timer)
        game_state = info_getter[1]
    elif(game_state == "simulation_start"):
        info_getter = engine.meeple
    else:
        game_state = game_state
        info_getter = tuple()
        music = "main_menu"
    return game_state, info_getter, music