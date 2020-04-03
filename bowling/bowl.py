class Bowl:

    def __init__(self):
        self.current_score = 0

    def score(self, score):
        self.current_score += score

    def get_score(self):
        return self.current_score
