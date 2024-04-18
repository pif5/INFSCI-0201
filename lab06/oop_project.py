class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def equip(self, weapon):
        self.weapon = weapon

    def take_turn(self):
        if self.weapon:
            self.weapon.use_weapon(self)
        else:
            print(f"{self.name} has no weapon to use.")


class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

    def use_weapon(self, character):
        character.health += self.damage
        action = "heals" if self.damage < 0 else "deals"
        if self.damage == 0:
            action = "does nothing"
        print(f"{character.name} uses {self.name} and {action} {abs(self.damage)} points, health now {character.health}")


class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


class Enemy(Character):
    def __init__(self, name, health, weapon=None):
        super().__init__(name, health)
        if weapon:
            self.equip(weapon)


empty_handed = Weapon(name="Empty handed", weapon_type="dummy", damage=0, value=0)
healing_staff = Weapon(name="Healing Staff", weapon_type="magic", damage=-3, value=0)

protagonist = Hero(name="Hero", health=100)
protagonist.equip(empty_handed)

ally = Enemy(name="Friendly Enemy", health=100)
ally.equip(healing_staff)


def game_loop():
    turns = 5
    for _ in range(turns):
        protagonist.take_turn()
        ally.take_turn()
        if protagonist.health <= 0 or ally.health <= 0:
            print("Game over")
            break


game_loop()



