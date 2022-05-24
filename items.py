class Item():
    # Base class for all items. 
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amount)), value=self.amount)


#Base class for all Weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                        description="A fist-sized rock, suitable for bludgeoning.",
                        value=0,
                        damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                        description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                        value=0,
                        damage=10)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                        description="A great sword found in the stone. Said to be the ultimate weapon and can slay anything",
                        value = 0,
                        damage=20)