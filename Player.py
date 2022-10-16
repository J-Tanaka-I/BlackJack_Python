class Player:
    def __init__(self, name):
        self.Point = 1000
        self.name = name
    def AddPoint(self, p) :
        self.Point += p



pl = Player("pl1" )
pl.AddPoint(-1)

print(pl.Point)