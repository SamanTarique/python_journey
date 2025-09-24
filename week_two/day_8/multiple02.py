class Father:
    def __init__(self, name, height=None):
        self.name = name
        self.height = height   # store as attribute


class Mother:
    def __init__(self, name, language=None):
        self.name = name
        self.language = language   # store as attribute


class Child(Father, Mother):
    def __init__(self, name, height, language):
        Father.__init__(self, name, height)
        Mother.__init__(self, name, language)

    def __str__(self):
        return (
            f"Child(name={self.name}, height={self.height}, language={self.language})"
        )


# --- usage ---
f = Father("Father", 6.0)
m = Mother("Mother", "Hindi")

c = Child("Child", 4.8, "English")
print(c)  # Child(name=Child, height=4.8, language=English)
