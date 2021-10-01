import random
class Meeple:
    def __init__(self, color = 'brown'):
        self.color = color
        self.perfect_pair = None
    
    def assign_perfect_pair(self, color):
        self.perfect_pair = color

    def check_pair(self, color):
        if(self.perfect_pair == color):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.color} meeple, perfect match is {self.perfect_pair}."

def assign_matches(meeple_array):
    matched_array = []
    while len(meeple_array) > 0:
        random_meeple = random.randint(1, len(meeple_array) - 1)
        meeple_array[0].assign_perfect_pair(meeple_array[random_meeple].color)
        meeple_array[random_meeple].assign_perfect_pair(meeple_array[0].color)
        matched_array.append(meeple_array[0])
        matched_array.append(meeple_array[random_meeple])
        meeple_array.pop(random_meeple)
        meeple_array.pop(0)
    return matched_array


def initialize_meeple():
    meeple_colors = ['brown', 'maroon', 'red', 'orange', 'yellow', 'green', 'forest', 'navy', 'blue', 'cyan', 'purple', 'magenta', 'pink', 'white', 'gray', 'black']
    meeple_array = []
    for color in meeple_colors:
        meeple_array.append(Meeple(color=color))
    meeple_array = assign_matches(meeple_array)
    return meeple_array
    
if __name__ == "__main__":
    random.seed(1)
    for meeple in initialize_meeple():
        print(meeple)
        
    print()
    print()
    print()

    meeple_array = initialize_meeple()
    for meeple in initialize_meeple():
        print(meeple)
    
    print(meeple_array[0].check_pair(meeple_array[1].color))
    print(meeple_array[0].check_pair(meeple_array[2].color))