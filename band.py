"""
Band class with Hsu and Gayle
"""


class Band:
    """"""
    def __init__(self, name=""):
        """"""
        self.name = name
        self.musicians = []

    def __repr__(self):
        return f"{self.name} ({','.join([str(musician) for musician in self.musicians])})"

    # def __repr__(self):
    #     """"""
    #     return str(vars(self))

    def add(self, musician):
        """"""
        self.musicians.append(musician)

    def play(self):
        """"""
        for musician in self.musicians:
            print(musician.play())
