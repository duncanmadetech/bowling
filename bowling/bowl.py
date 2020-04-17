class Bowl:

    def __init__(self):
        self.current_score = 0
        self.is_spare = False
        self.is_strike = False

    def score(self, bowl1, bowl2):
        if self.is_spare:
            self.current_score += bowl1
        if self.is_strike:
            self.is_strike = False
            self.current_score = self.current_score + bowl1 + bowl2
        self.current_score = self.current_score + bowl1 + bowl2
        self.is_spare = bowl1 + bowl2 == 10

    def get_score(self):
        return self.current_score

    def strike(self):
        self.current_score += 10
        self.is_strike = True
