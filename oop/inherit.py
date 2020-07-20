class User:
    def Sign_in(self):
        print("Logged in");


class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')

class Archer(User):
    def __init__(self,name,arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'attacking with the arrow, Arrow left {self.arrow}')
           

wizard1 = Wizard("Merry", 45)
archer1 = Archer("terry",441)
wizard1.attack()
archer1.attack()

print(isinstance(wizard1,User))