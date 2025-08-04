import status_effect
class item:
    def __init__(self, name, use_fn, description, quanity, cost):
        self.name = name
        self.use_fn = use_fn
        self.description = description
        self.quanity = quanity
        self.cost = cost

    

def use_health_potion(character, item: item):
    print(f"\n{character.name} uses a Health Potion")
    character.heal(50)
    item.quanity -= 1

def use_greater_health_potion(character, item: item):
    print(f"\n{character.name} uses a Greater Health Potion")
    character.heal(100)
    item.quanity -= 1

def use_supreme_health_potion(character, item: item):
    print(f"\n{character.name} uses a Supreme Health Potion")
    character.heal(150)
    item.quanity -= 1

def use_mana_potion(character, item: item):
    print(f"\n{character.name} uses a Mana Potion")
    character.restore_mana(50)
    item.quanity -= 1

def use_greater_mana_potion(character, item: item):
    print(f"\n{character.name} uses a Greater Mana Potion")
    character.restore_mana(100)
    item.quanity -= 1

def use_supreme_mana_potion(character, item: item):
    print(f"\n{character.name} uses a Supreme Mana Potion")
    character.restore_mana(150)
    item.quanity -= 1

def use_potion_of_iron_skin(character, item: item):
    print(f"\n{character.name} uses a Potion of Iron Skin")
    character.apply_status_effect(status_effect.buff_ac, 2, 2)
    item.quanity -= 1

def use_potion_of_diamond_skin(character, item: item):
    print(f"\n{character.name} uses a Potion of Diamond Skin")
    character.apply_status_effect(status_effect.buff_ac, 2, 4)
    item.quanity -= 1

def use_potion_of_accuracy(character, item: item):
    print(f"\n{character.name} uses a Potion of Accuracy")
    character.apply_status_effect(status_effect.buff_attack, 2, 2)
    item.quanity -= 1

def use_potion_of_greater_accuracy(character, item: item):
    print(f"\n{character.name} uses a Potion of Accuracy")
    character.apply_status_effect(status_effect.buff_attack, 2, 4)
    item.quanity -= 1

def use_potion_of_berserkers_rage(character, item: item):
    print(f"\n{character.name} uses a Potion of Berserkers Rage")
    character.apply_status_effect(status_effect.buff_phys_damage, 2, 1)
    item.quanity -= 1

def use_potion_of_spell_strength(character, item: item):
    print(f"\n{character.name} uses a Potion of Spell Strength")
    character.apply_status_effect(status_effect.buff_spell_damage, 2, 1)
    item.quanity -= 1

health_potion = item(
    name="Health Potion",
    use_fn=use_health_potion,
    description="Heals health by 50",
    quanity=1,
    cost= 40
)

mana_potion = item(
    name="Mana Potion",
    use_fn=use_mana_potion,
    description="Restores mana by 50",
    quanity=1,
    cost= 40
)

greater_health_potion = item(
    name="Greater Health Potion",
    use_fn=use_greater_health_potion,
    description="Restores health by 100",
    quanity=1,
    cost= 70
)

greater_mana_potion = item(
    name="Greater Mana Potion",
    use_fn=use_greater_mana_potion,
    description="Restores mana by 100",
    quanity=1,
    cost= 70
)

supreme_health_potion = item(
    name="Supreme Health Potion",
    use_fn=use_supreme_health_potion,
    description="Restores health by 150",
    quanity=1,
    cost= 100
)

supreme_mana_potion = item(
    name="Supreme Mana Potion",
    use_fn=use_supreme_mana_potion,
    description="Restores mana by 150",
    quanity=1,
    cost= 100
)

potion_of_iron_skin = item(
    name="Potion of Iron Skin",
    use_fn=use_potion_of_iron_skin,
    description="Buffs users defence for 2 turns",
    quanity=1,
    cost= 60
)

potion_of_diamond_skin = item(
    name="Potion of Diamond Skin",
    use_fn=use_potion_of_diamond_skin,
    description="Greatly buffs users defence for 2 turns",
    quanity=1,
    cost= 120
)

potion_of_accuracy = item(
    name="Potion of Accuracy",
    use_fn=use_potion_of_accuracy,
    description="Buffs users accuracy for 2 turns",
    quanity=1,
    cost= 60
)

potion_of_greater_accuracy = item(
    name="Potion of Greater Accuracy",
    use_fn=use_potion_of_greater_accuracy,
    description="Greatly buffs users accuracy for 2 turns",
    quanity=1,
    cost= 120
)

potion_of_berserker_rage = item(
    name="Potion of Berserker Rage",
    use_fn=use_potion_of_berserkers_rage,
    description="Double users physical damage for 2 turns",
    quanity=1,
    cost= 200
)

potion_of_spell_strength = item(
    name="Potion of Spell Strength",
    use_fn=use_potion_of_spell_strength,
    description="Double users spell damage for 2 turns",
    quanity=1,
    cost= 200
)

available_items = [mana_potion,
                   health_potion,
                   greater_health_potion,
                   greater_mana_potion,
                   supreme_health_potion,
                   supreme_mana_potion,
                   potion_of_iron_skin,
                   potion_of_diamond_skin,
                   potion_of_accuracy,
                   potion_of_greater_accuracy,
                   potion_of_berserker_rage,
                   potion_of_spell_strength]