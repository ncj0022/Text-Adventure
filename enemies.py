class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Slime(Enemy):
    def __init__(self):
        super().__init__(name="Slime", hp = 5, damage = 1)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp = 20, damage = 5)

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp = 40, damage=5)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=100, damage=10)