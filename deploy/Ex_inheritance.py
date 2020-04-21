class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.name)
            print(animal.age)
            print(animal.walk())
            print(animal.sing('meow meow nyaaa~~~'))


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{self.name} {sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{self.name} {sounds}'


class Gris(Cat):
    def sing(self, sounds):
        return f'{self.name} {sounds}'


my_cats = [Simon('Shuha', 2), Sally('Sally', 1), Gris('Gris', 1)]
print(my_cats)

my_pets = Pets(my_cats)
print(type(my_pets))
my_pets.walk()

# 1 Add nother Cat

# 2 Create a list of all of the pets (create 3 cat instances from the above)


# 3 Instantiate the Pet class with all your cats use variable my_pets

# 4 Output all of the cats walking using the my_pets instance