#Learning Classes

class People:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

David = People("David", 25, "Ecto-Cardiologist")
print(David)