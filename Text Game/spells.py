available_spells = {
    "fireball": {
        "name": "Fireball",
        "damage_range": (25, 50),
        "mana_cost": 50,
        "description": "A spell doing medium damage",
        "spell_func": "use_fireball"
    },
    "ice shard": {
        "name": "Ice Shard",
        "damage_range": (15, 30),
        "mana_cost": 25,
        "description": "A weak spell that slow the target, making them miss a turn",
        "spell_func": "use_ice_shard"
    },
    "shocking grasp": {
        "name": "Shocking Grasp",
        "damage_range": (40, 60),
        "mana_cost": 65,
        "description": "A spell doing medium damage",
        "spell_func": "use_shocking_grasp"
    },
    "improved shield": {
        "name": "Improved Shield",
        "damage_range": (0, 0),
        "mana_cost": 80,
        "description": "Greatly increases defence over 3 turns",
        "spell_func": "use_improved_shield"
    },
    "shield": {
        "name": "Shield",
        "damage_range": (0, 0),
        "mana_cost": 40,
        "description": "Improves defence over 2 turns",
        "spell_func": "use_shield"
    },
    "enchant weapon": {
        "name": "Enchant Weapon",
        "damage_range": (0, 0),
        "mana_cost": 60,
        "description": "Increase users accuracy",
        "spell_func": "use_enchant_weapon"
    },
    "vampiric touch": {
        "name": "Vampiric Touch",
        "damage_range": (25, 40),
        "mana_cost": 70,
        "description": "A spell doing medium damage, that steal health from target",
        "spell_func": "use_vampiric_touch"
    },
    "incinerate": {
        "name": "Incinerate",
        "damage_range": (100, 150),
        "mana_cost": 100,
        "description": "A spell doing high damage",
        "spell_func": "use_incinerate"
    },
    "sap strength": {
        "name": "Sap Strength",
        "damage_range": (20, 40),
        "mana_cost": 60,
        "description": "A spell doing weak damage, that saps the strength of the target temporarily",
        "spell_func": "use_sap_strength"
    },
    "berserk": {
        "name": "Berserk",
        "damage_range": (0, 0),
        "mana_cost": 80,
        "description": "Double the physical damage of the user temporarily",
        "spell_func": "use_berserk"
    },
}