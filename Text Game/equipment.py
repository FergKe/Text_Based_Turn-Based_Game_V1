class ring:
    def __init__(self, name, description, quanity, cost, ac, attack, health, mana, phys_dam, spell_dam):
        self.name = name
        self.description = description
        self.cost = cost
        self.ac = ac
        self.quanity = quanity
        self.attack = attack
        self.health = health
        self.mana = mana
        self.phys_dam = phys_dam
        self.spell_dam = spell_dam

class armour:
    def __init__(self, name, description, quanity, cost, ac, attack, health, mana, phys_dam, spell_dam):
        self.name = name
        self.description = description
        self.cost = cost
        self.quanity = quanity
        self.ac = ac
        self.attack = attack
        self.health = health
        self.mana = mana
        self.phys_dam = phys_dam
        self.spell_dam = spell_dam

class weapon:
    def __init__(self, name, description, quanity, cost, ac, attack, health, mana, phys_dam, spell_dam):
        self.name = name
        self.description = description
        self.cost = cost
        self.quanity = quanity
        self.ac = ac
        self.attack = attack
        self.health = health
        self.mana = mana
        self.phys_dam = phys_dam
        self.spell_dam = spell_dam

class necklace:
    def __init__(self, name, description, cost, quanity, ac, attack, health, mana, phys_dam, spell_dam):
        self.name = name
        self.description = description
        self.cost = cost
        self.quanity = quanity
        self.ac = ac
        self.attack = attack
        self.health = health
        self.mana = mana
        self.phys_dam = phys_dam
        self.spell_dam = spell_dam


ring_of_accuracy = ring(
    name="Ring of Accuracy",
    description="A ring that increases the wearers accuracy",
    cost=10,
    quanity=1,
    ac=0,
    attack=2,
    health=0,
    mana=0,
    phys_dam=0,
    spell_dam=0
)

standard_armour = armour(
    name="Standard Armour",
    description="Slightly increases wearers defence",
    cost=10,
    quanity=1,
    ac=1,
    attack=0,
    health=0,
    mana=0,
    phys_dam=0,
    spell_dam=0
)

fine_sword = weapon(
    name="Fine Sword",
    description="Slightly increases wielders attack",
    cost=10,
    quanity=1,
    ac=0,
    attack=1,
    health=0,
    mana=0,
    phys_dam=0,
    spell_dam=0
)

frying_pan = weapon(
    name="Frying Pan",
    description="A Hobbits favoured Weapn",
    cost=10,
    quanity=1,
    ac=0,
    attack=4,
    health=0,
    mana=0,
    phys_dam=0,
    spell_dam=0
)

amulet_of_health = necklace(
    name="Amulet of Health",
    description="A necklace that increases the wearers health",
    cost=10,
    quanity=1,
    ac=0,
    attack=0,
    health=40,
    mana=0,
    phys_dam=0,
    spell_dam=0
)

available_equipment = [ring_of_accuracy, standard_armour, fine_sword, amulet_of_health]