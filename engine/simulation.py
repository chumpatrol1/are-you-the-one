import random
if(__name__ != "__main__"):
    from engine.meeple import initialize_meeple
    from engine.decision import Decision, Pairing


round = 0
meeple_array = []
decision_array = []
true_pairs = []
false_pairs = []

def make_random_pairings(meeple_array):
    temp_array = meeple_array.copy()
    pairing_array = []

    while temp_array != []:
        random_num = random.randint(0, len(temp_array) - 1)
        meepleA = temp_array[random_num]
        temp_array.pop(random_num)
        random_num = random.randint(0, len(temp_array) - 1)
        meepleB = temp_array[random_num]
        temp_array.pop(random_num)

        pairing_array.append(Pairing(meepleA, meepleB))
        #print("Paired {} and {}".format(meepleA, meepleB))

    first_decision = Decision(pairing_array)
        
    return first_decision

def make_informed_pairings(meeple_array, true_pairs, false_pairs):
    temp_array = meeple_array.copy()
    for true_pair in true_pairs:
        print("TRUE:", true_pair)
        temp_array.remove(true_pair.meeple1)
        temp_array.remove(true_pair.meeple2)
    
    for false_pair in false_pairs:
        print("FALSE:", false_pair)

    #Super inefficient lol
    new_random_pairings = make_random_pairings(temp_array).return_pairings()
    good_pairings = 0
    while good_pairings < 1:
        good_pairings = 1 # Start out as good

        for new_pair in new_random_pairings: # Look through each pairing we made
            for false_pair in false_pairs: # Looks through each false pairing (through truth booth)
                if(false_pair == new_pair): # If they match, that's bad!
                    good_pairings = 0
                    break
            if good_pairings == 0:
                break
        
        if(good_pairings == 0): # If it's a bad result, reroll the pairs!
            new_random_pairings = make_random_pairings(temp_array).return_pairings()
        
    new_guess = true_pairs + new_random_pairings
    return Decision(new_guess)

def truth_booth(pairing):
    return pairing.check_match()

def handle_logic():
    global round
    global meeple_array
    global decision_array
    global true_pairs
    global false_pairs

    if(round == 0):
        decision_array.append(make_random_pairings(meeple_array))
        pairings_list = decision_array[0].return_pairings()
        pairing = random.choice(pairings_list)
        truth_booth_check = truth_booth(pairing)
        print()
        print("Checked {}: {}".format(pairing, truth_booth_check))
        if(decision_array[-1].return_match_num() == 0):
            for pair in decision_array[-1].return_pairings():
                false_pairs.append(pair)
        else:
            if(truth_booth_check):
                true_pairs.append(pairing)
            else:
                false_pairs.append(pairing)
    else:
        decision_array.append(make_informed_pairings(meeple_array, true_pairs, false_pairs))
        pairings_list = decision_array[-1].return_pairings()[len(true_pairs):]
        pairing = random.choice(pairings_list)
        truth_booth_check = truth_booth(pairing)
        print("Checked {}: {}".format(pairing, truth_booth_check))

        if(truth_booth_check):
            true_pairs.append(pairing)
            new_false_pairs = []
            for false_pair in false_pairs:
                if(false_pair.meeple1 == pairing.meeple1) or (false_pair.meeple1 == pairing.meeple2)\
                    or (false_pair.meeple2 == pairing.meeple1) or (false_pair.meeple2 == pairing.meeple2):
                    continue
                else:
                    new_false_pairs.append(false_pair)

            false_pairs = new_false_pairs.copy()

        else:
            for f_pair in false_pairs:
                if f_pair == pairing:
                    break
            else:
                false_pairs.append(pairing)




        print(len(true_pairs))
    
    round += 1

def hold_meeple():
    global meeple_array
    if(meeple_array == []):
        meeple_array = initialize_meeple()

def return_meeple():
    global meeple_array
    return meeple_array

def return_decision():
    global decision_array
    return decision_array[-1]

def return_round():
    global round
    return round

if __name__ == "__main__":
    print("BEGIN")
    random.seed(1)
    import meeple
    meeple_array = meeple.initialize_meeple()
    from decision import Decision, Pairing
    for meeple in meeple_array:
        print(meeple)
    
    handle_logic()
    while not decision_array[-1].get_solved():
        print("ROUND {}".format(round))
        handle_logic()
        print()

    print("FINAL PAIRINGS")
    for pairing in decision_array[-1].return_pairings():
        print(pairing)