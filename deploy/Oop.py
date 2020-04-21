# class
class PlayerCharacter:
    membership = True;  # class object attributes

    def __init__(self, name, age):  # constructor method self refers to class name eta hocche ei cls er method
        self._name = name  # like constructor .these are attributes of the class
        self._age = age

    def run(self,
            hello):  # all method e 1st parameter hocche self jate shbjagai use korte pari but eta differrent method
        self.hello = hello  # or shudhu hello dieo hoi
        print('run')
        print(f'my name is{self.hello}')
        return hello

    def run1(self):
        print(self)
        return self

        # classmethods

    @classmethod
    def adding_numbers(self, num1, num2):
        return self('Ted', num1 + num2)  # self dieo object instaniate kra jabe

    # def adding_numbers(cls,num1,num2):
    #   return num1+num2 cls o use kra jai self er jagai
    @staticmethod
    def adding_numbers1(num1, num2):
        return num1 + num2
        # static method die kono object instaniate korte parbo na


player1 = PlayerCharacter("Lucy", 20)
player2 = PlayerCharacter("Berserk", 18)
print(player1._name)
player1.run('Clara')
print(player2._name)
print(type(player1._name))
player2.run('Jugg')
player4 = PlayerCharacter.adding_numbers(10, 2)
print(player4._age)
print(player1.adding_numbers(2, 3))
print(PlayerCharacter.adding_numbers(10, 2))
print(player4.adding_numbers1(10, 10))
print(player4.run1().run('saki'))


# python e public private ksu nei
# but private bolte '-' dea jai

# inheritance
# a fight between 2 wizards game
class user:
    def sign_in(self):
        print("logged in")


class wizard(user):  # bracket e class dile inherit kora bujhai
    def __init__(self, name, power):
        self.name = name
        self.power = power


def attack(times):
    if (wizard2.power > wizard1.power):
        damage = wizard2.power * 0.2
        print(damage)
        damaged = wizard1.power
        for i in range(times):
            damaged = damaged - damage

            print(damaged)
        if (damaged <= 0):
            print(f'{wizard2.name} is winner')
        else:
            print(f'{wizard1.name} is winner')

    else:
        damage1 = wizard1.power * 0.15
        damaged1 = wizard2.power
        for i in range(times):
            damaged1 = damaged1 - damage1
        print(damaged1)
        if (damaged1 <= 0):
            print(f'{wizard1.name} is winner')
        else:
            print(f'{wizard2.name} is winner')


# end


class archer(user):  # inherit kortesi
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self, times):
        print(f'starting arrows: {self.num_arrows}')
        for i in range(times):
            print(f'arrows decreasing: {self.num_arrows - (i + 1)}')


name = input('State your Name: ')
power = 65
a = int(input('how many times attacked?'))

wizard1 = wizard(name, power)
wizard2 = wizard('Roy', 45)
attack(a)
print(wizard1.sign_in())
archer1 = archer('Robin', 50)
archer1.attack(a)
print(PlayerCharacter.membership)
print(isinstance(wizard1, user))  # wizard1 object wizard er->wizard class->user class->base class object theke
print(isinstance(wizard1, object))  # base class object upper hierarchy