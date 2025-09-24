class Father:
    name = 'Mr. Father'

    def __init__(self, age, height, colour, language):
        self.age = age
        self.height = height
        self.colour = colour
        self.language = language

    def __str__(self):
        return (
            f"name: {self.name}, "
            f"age: {self.age}, "
            f"height: {self.height}, "
            f"colour: {self.colour}, "
            f"language: {self.language} "
        )

    def get_height(self):
        return self.height

    def get_colour(self):
        return self.colour

    def get_language(self):
        return self.language


class Mother:
    name = "Mrs. Mother"

    def __init__(self, age, height, colour, language):
        self.age = age
        self.height = height
        self.colour = colour
        self.language = language

    def __str__(self):
        return (
            f"name: {self.name}, "
            f"age: {self.age}, "
            f"height: {self.height}, "
            f"colour: {self.colour}, "
            f"language: {self.language} "
        )

    def get_height(self):
        return self.height

    def get_colour(self):
        return self.colour

    def get_language(self):
        return self.language


class Child(Father, Mother):
    name = 'Master Child'

    def __init__(self, age, father, mother):
        self.age = age
        self.father = father
        self.mother = mother
        # self.height = Father.get_height()
        # self.language = Father.get_language()
        # self.colour = Mother.get_colour()

    def __str__(self):
        return (
            f"name: {self.name}, "
            f"age: {self.age}, "
            f"height: {self.father.get_height()}, "
            f"colour: {self.mother.get_colour()}, "
            f"language: {self.father.get_language()} "
        )


mother = Mother(30, 6.0, 'white', 'Hindi')
father = Father(32, 5.5, "Brown", "English")
child = Child(5, father, mother)

print("Mother-", mother, '\n')
print("Father-", father, '\n')
print("Child-", child, '\n')
