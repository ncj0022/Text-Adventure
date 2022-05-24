from telnetlib import XASCII
import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles"""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room"""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class SlimeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Slime())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A slime jumps out in front of you!
            """
        else:
            return """
            The corpse of a dead slime rots on the ground.
            """
 
class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        You see something shiny on the ground.
        You found 5 gold!
        """

class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        return """
        You found a sword sticking out of the stone.
        """

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An Ogre came charging at you!
            """
        else:
            return """
            The corpse of a slain ogre rots on the ground.
            """

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x,y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider fell from the roof of the cave.
            """
        else:
            return """
            The dead body of a giant spider rest here.
            """

class DragonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x,y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A massive dragon towers over you, ready to strike.
            """
        else:
            return """
            The corpse of the fallen dragon are on the ground.
            """


class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen in a room full of snakes

        You have died!
        """

    def modify_player(self, player):
        player.hp = 0

class HealRoom(MapTile):
    def intro_text(self):
        return """
        A heavenly light shines in the room.
        
        The light has healed you!
        """
    def modify_player(self, player):
        player.hp = 100


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
         
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True