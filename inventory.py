class Weapon:
    def __init__(self, name, accuracy, damage):
        self.name = name
        self.accuracy = accuracy
        self.damage = damage

class Item:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal = heal_amount

class Inventory:
    def __init__(self, name, weapons = [], itens = []):
        self.unit = name
        self.weapons = weapons
        self.itens = itens
        self.equipped = False

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_item(self, item):
        self.itens.append(item)

    def equip_weapon(self, name):
        for i in range(len(self.weapons)):
            if self.weapons[i].name == name:
                self.equipped = self.weapons[i]
                return self.weapons[i]
        return self.equipped

    def use_item(self, name):
        for i in range(len(self.itens)):
            if self.itens[i].name == name:
                heal = self.itens[i].heal
                self.itens.remove(self.itens[i])
                return heal
        return 0

    def get_inventory(self):
        return self.unit, self.weapons, self.itens

    def get_equipped(self):
        return self.equipped
