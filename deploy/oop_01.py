class User:
    def __init__(self, email):
        self.email = email


class Wizard(User):
    def __init__(self, name, age, email):
        # User.__init__(self,email)
        super().__init__(email)  # uporer r evbe  parent r child 2 ta te constructor thakle super() call  korte pari
        self.name = name
        self.age = age

    def intro(self):
        print(f'my name is {self.name} and age is {self.age} and email is {self.email}')


wizard1 = Wizard('merlin', 18, 'merlin@gmail.com')
print(wizard1.email)
wizard1.intro()

# object introspection -ability to determine the type of object during runtime

print(dir(wizard1))  # dir die  ei object er jn ne ki ki method,attributes avaliable jana jai


# Test of inheritance and super() And encapsulattion

class Toy:
    action_figure = []

    def __init__(self, action):
        self.action_figure = action
        self.list = [1, 2, 3, 4, 5]
        self.my_dict = {'name': 'pussy cats',
                        'age': 17}

        def __str__(self):
            return f'heyaaaaa!!!!'

    def __del__(self):
        print('deleted')

    def __getitem__(self, i):
        # return self.list[i]
        return self.my_dict[i]

    def __repr__(self):
        return f'GRIS'

    def manufracturer(self):
        for figure in self.action_figure:
            print(figure.name)
            print(figure.age)
            print(figure.power)
            print(figure.country)
            figure.manufracturer()


class Hero(Toy):
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def manufracturer(self):
        print(f'{self.name} is an action figure and was made in {self.country}')


class Deku(Hero):
    def __init__(self, name, age, power, country):
        self.power = power
        super().__init__(name, age, country)


class bakugo(Hero):
    def __init__(self, name, age, power, country):
        self.power = power
        super().__init__(name, age, country)


my_hero = [Deku('midoriya', 17, 1000, 'Japan'), bakugo('Fire', 17, 2000, 'Italy')]
print(my_hero[1].power)
print(my_hero[0].name)

action_fig = Toy(my_hero)
action_fig.manufracturer()

# Dunder methods(__init__)
print(action_fig)
print(action_fig.__str__())
print(str(action_fig))


# why use dunder method?Ans is to avoid errors
# class Nolen:
#   pass
# obj1 =Nolen()
# print(len(obj1))#TypeError: object of type 'Nolen' has no len() because class is empty BUT

class LenSupps:
    def __len__(self):
        return 19


obj = LenSupps()
print(len(obj))  # len() is now returning the value i modified it with the dunder method __len__ = 19
# del action_fig delete kore debe object
# print(action_fig[0]) for list
print(action_fig['age'])
print(action_fig['name'])
print(action_fig)
print(action_fig.__repr__())
print(repr(action_fig))


class SuperList(list):
    def __len__(self):
        return 1000


list1 = SuperList()
print(len(list1))
list1.append(5)
print(list1[0])
print(issubclass(SuperList, list))


class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def add_transactions(self, amount):
        self.transactions.append(amount)

    def add_balance(self):
        return self.amount + sum(self.transactions)

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, i):
        return self.transactions[i]


acc = Account('rahim', 100)
print(acc.add_balance())
count = int(input('how ma ny transactions?'))
for i in range(0, count):
    amount = int(input('add amount: '))
    acc.add_transactions(amount)
    print(acc.add_balance())
print(len(acc))
for i in acc:
    print(i)

