if(__name__ != "__main__"):
    from engine.meeple import initialize_meeple


round = 0
meeple_array = []
decision_array = []

def handle_logic():
    global round
    global meeple_array
    global decision_array

    if(round == 0):
        print("ROUND 0")

if __name__ == "__main__":
    print("BEGIN")
    import random
    random.seed(1)
    import meeple
    meeple_array = meeple.initialize_meeple()

    for meeple in meeple_array:
        print(meeple)

    handle_logic()