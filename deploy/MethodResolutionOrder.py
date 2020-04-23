class User:
    def __init__(self, email):
        self.email = email

    def signin(self):
        print('logged in')
        print(f'email is {self.email}')


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        User.__init__(self, email)

    def powerhouse(self):
        print(f'fighting with power: {self.power}')


class Archer(User):
    def __init__(self, name, arrows, email):
        self.name = name
        self.arrows = arrows
        User.__init__(self, email)

    def firing(self):
        print(f'firing with arrows : {self.arrows}')


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, email, arrows):
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows, email)

    def monster(self):
        print(
            f"{self.name} is a monster with power {self.power + (self.power * 2)} and has a firing range of {self.arrows + (self.arrows * 2)} and {self.name}'s email is : {self.email}")


Hb1 = Hybrid('Rouge', 60, 'rogue@gmail.com', 100)
Hb1.powerhouse()
Hb1.monster()
print(Hb1.email)
Hb1.signin()
Hb1.firing()
print(Hybrid.mro())

# class Class1:
#   def m(self):
#     print(f'class1')
# class Class2(Class1):
#   def m(self):
#     print(f'class2')
#     super().m()
# class Class3(Class1):
#   def m(self):
#     print(f'class3')
#     super().m()
# class Class4(Class2,Class3):
#   def m(self):
#     print(f'class4')
#     super().m()


# cl =Class4()
# cl.m()

# class Class1:
#   def m(self):
#     print(f'class1')

# class Class2(Class1):
#   def m(self):
#     print(f'class2')

# class Class3(Class1):
#   def m(self):
#     print(f'class3')
#     Class1.m(self)

# class Class4(Class2,Class3):
#   def m(self):
#     print(f'class4')
#     Class3.m(self)
#     Class2.m(self)
#     Class1.m(self)#class die call dte gele sef use kora hoi


# cl1 =Class4()
# cl1.m()