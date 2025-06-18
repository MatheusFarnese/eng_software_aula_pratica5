from inventory import Weapon, Item, Inventory

def test_add_weapons():
    w1 = Weapon("Aymr", 60, 24)
    w2 = Weapon("Silver axe", 70, 16)
    inv = Inventory("Edelgard", [w1, w2], [])
    w3 = Weapon("Hand axe", 70, 5)
    inv.add_weapon(w3)

    unit, wps, _ = inv.get_inventory()
    assert unit == "Edelgard"
    assert wps[0] == w1
    assert wps[1] == w2
    assert wps[2] == w3

def test_add_itens():
    i1 = Item("Vulnerary", 20)
    i2 = Item("Vulnerary", 20)
    inv = Inventory("Dorothea", [], [i1, i2])
    i3 = Item("Elixir", 99)
    inv.add_item(i3)

    unit, _, its = inv.get_inventory()
    assert unit == "Dorothea"
    assert its[0] == i1
    assert its[1] == i2
    assert its[2] == i3

def test_equip_weapon():
    w1 = Weapon("Silver Lance", 80, 13)
    w2 = Weapon("Sword of the Creator", 90, 15)
    w3 = Weapon("Wo dao", 90, 8)
    inv = Inventory("Byleth", [w1, w2], [])
    inv.add_weapon(w3)

    w = inv.equip_weapon("Sword of the Creator")
    assert inv.unit == "Byleth"
    assert w == inv.get_equipped()
    assert w.accuracy == 90
    assert w.damage == 15

def test_use_item():
    i1 = Item("Herb", 10)
    i2 = Item("Vulnerary", 20)
    i3 = Item("Elixir", 99)
    inv = Inventory("Bernadetta", [], [i1, i2, i3])
    i4 = Item("vulnerary", 20)
    inv.add_item(i4)

    heal = inv.use_item("Vulnerary")
    unit, _, itens = inv.get_inventory()
    assert unit == "Bernadetta"
    assert heal == 20
    assert len(itens) == 3
    assert itens[0] == i1
    assert itens[1] == i3
    assert itens[2] == i4

def test_bad_statments():
    i1 = Item("Elixir", 99)
    i2 = Item("Vulnerary", 20)
    w1 = Weapon("Brave bow", 70, 10)
    w2 = Weapon("Training lance", 90, 4)
    inv = Inventory("Petra", [w1, w2], [i1, i2])

    w = inv.equip_weapon("Iron axe")
    heal = inv.use_item("Herb")
    assert not w
    assert heal == 0
