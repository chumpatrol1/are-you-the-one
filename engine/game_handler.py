from json import loads, dumps
import engine.menu
import engine.meeple
import engine.simulation

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
        engine.simulation
        info_getter = tuple()
        game_state = "simulation_start_wait"
    elif(game_state == "simulation_start_wait"):
        engine.simulation.hold_meeple()
        info_getter, game_state = engine.simulation.return_meeple(), engine.menu.simulation_advance(timer, game_state)
    elif(game_state == "simulation_logic"):
        engine.simulation.handle_logic()
        info_getter, game_state = engine.simulation.return_decision(), "simulation_logic_wait"
    elif(game_state == "simulation_logic_wait"):
        info_getter, game_state = engine.simulation.return_decision(), engine.menu.simulation_advance(timer, game_state)
    elif(game_state == "credits"):
        game_state = engine.menu.credits_waiter(timer)
        info_getter = tuple()
    else:
        game_state = game_state
        info_getter = tuple()
        music = "main_menu"
    return game_state, info_getter, music