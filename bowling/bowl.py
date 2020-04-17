class Bowl:

    def __init__(self):
        self.current_score = 0
        self.is_spare = False
        self.is_strike = [ False, False]

    def score(self, bowl1, bowl2):
        if self.is_spare:
            self.current_score += bowl1

        # The last two bowls were strikes
        if self.is_strike[0]:
            self.current_score = self.current_score + bowl1
            self.is_strike[0] = False

        # The last bowl was a strike
        if self.is_strike[1]:
            self.current_score = self.current_score + bowl1 + bowl2
            self.is_strike[1] = False

        self.current_score = self.current_score + bowl1 + bowl2
        self.is_spare = bowl1 + bowl2 == 10

    def get_score(self):
        return self.current_score

    def strike(self):
        self.current_score += 10
        if self.is_spare:
            self.current_score += 10
            self.is_spare = False
        if self.is_strike[0]:
            self.current_score += 10
        if self.is_strike[1]:
            self.current_score += 10
        self.is_strike.pop(0)
        self.is_strike.append(True)
