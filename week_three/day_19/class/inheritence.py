class Milk:
    def __init__(self, colour, density):
        self.colour = colour
        self.density = density

    def get_colour(self):
        return self.colour

    def get_density(self):
        return self.density


class Sweet:
    def __init__(self, sweet):
        self.sweet = sweet


class Tea(Milk, Sweet):
    def __init__(self, colour, density, sweet, ingrediant1, ingrediant2):
        Milk.__init__(self, colour, density)
        Sweet.__init__(self, sweet)
        self.ingrediant1 = ingrediant1
        self.ingrediant2 = ingrediant2


tea = Tea("white", "thick", "Sugar", "tea leaves", "water")
print(tea.colour)
