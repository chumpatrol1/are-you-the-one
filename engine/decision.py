class Pairing:
    def __init__(self, meeple1 = None, meeple2 = None, match = None):
        self.meeple1 = meeple1
        self.meeple2 = meeple2
        self.match = match

    def check_match(self):
        try:
            self.meeple1.check_pair(self.meeple2.color)
        except Exception as ex:
            print("Error!" + ex)

class Decision:
    def __init__(self, pairings):
        self.pairings = pairings
        self.correct_matches = 0