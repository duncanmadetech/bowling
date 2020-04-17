class Bowl:

    def __init__(self):
        self.current_score = 0

    def score(self, bowl1, bowl2):
        self.current_score = self.current_score + bowl1 + bowl2

    def get_score(self):
        return self.current_score
