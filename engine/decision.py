import random

class Pairing:
    def __init__(self, meeple1 = None, meeple2 = None, match = None):
        self.meeple1 = meeple1
        self.meeple2 = meeple2
        if(match is None):
            self.match = self.check_match()
        else:
            self.match = match

    def check_match(self):
        try:
            return self.meeple1.check_pair(self.meeple2.color)
        except Exception as ex:
            print("Error!" + ex)
            return False

    def __str__(self):
        return "Pairing of {} and {}: {}".format(self.meeple1, self.meeple2, self.check_match())
    
    def __eq__(self, other):
        if(self.meeple1 == other.meeple1 or self.meeple1 == other.meeple2) and (self.meeple2 == other.meeple1 or self.meeple2 == other.meeple2):
            return True
        else: 
            return False

class Decision:
    def __init__(self, pairings = None):
        self.pairings = pairings

        self.correct_matches = 0
        if self.pairings is not None:
            for pairing in self.pairings:
                if pairing.check_match():
                    self.correct_matches += 1

    def add_pairing(self, meeple1, meeple2):
        if(self.pairings is None):
            self.pairings = [Pairing(meeple1=meeple1, meeple2=meeple2)]
        else:
            self.pairings.append(Pairing(meeple1=meeple1, meeple2=meeple2))

        if(self.pairings[-1].check_match):
                self.correct_matches += 1

    def return_pairing_str(self):
        pairing_array = []
        for pairing in self.pairings:
            pairing_array.append(pairing.__str__())
        return pairing_array

    def return_pairings(self):
        return self.pairings

    def get_solved(self):
        if(self.correct_matches == len(self.pairings)):
            return True
        else: 
            return False

    def __str__(self):
        return "Correct Matches: {}, Pairings: {}".format(self.correct_matches, self.return_pairing_str())