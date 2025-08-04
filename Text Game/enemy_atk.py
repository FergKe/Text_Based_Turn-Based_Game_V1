import random
import utils
import status_effect

# Figther attacks
fighter_atks = {
    "sword slash": {
        "name" : "Sword Slash",
        "atk func" : "use_sword_slash"
    },
    "shield bash": {
        "name" : "Shield Bash",
        "atk func" : "use_shield_bash"
    },
    "hilt smash": {
        "name" : "Hilt Smash",
        "atk func" : "use_hilt_smash"
    }
}

def use_sword_slash(character, target):
    print(f"\n{character.name} uses Sword Slash against {target.name}")
    damage = random.randint(20, 30) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_shield_bash(character, target):
    print(f"\n{character.name} uses Shield Bash against {target.name}")
    damage = random.randint(15, 25) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_hilt_smash(character, target):
    print(f"\n{character.name} uses Hilt Smash against {target.name}")
    damage = random.randint(10, 30) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

thief_atks = {
    "stab": {
        "name" : "Stab",
        "atk func" : "use_stab"
    },
    "sneak attack": {
        "name" : "Sneak Attack",
        "atk func" : "use_sneak_attack"
    },
    "headbutt": {
        "name" : "Headbutt",
        "atk func" : "use_headbutt"
    }
}

def use_stab(character, target):
    print(f"\n{character.name} uses Stab against {target.name}")
    damage = random.randint(5, 15) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_sneak_attack(character, target):
    print(f"\n{character.name} uses Sneak Attack against {target.name}")
    damage = random.randint(25, 50) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_headbutt(character, target):
    print(f"\n{character.name} uses Headbutt against {target.name}")
    damage = random.randint(20, 35) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

wizard_atks = {
    "ray of sickness": {
        "name" : "Ray of Sickness",
        "atk func" : "use_ray_of_sickness"
    },
    "vampiric touch": {
        "name" : "Vampiric Touch",
        "atk func" : "use_vampiric_touch"
    },
    "ice blast": {
        "name" : "Ice Blast",
        "atk func" : "use_ice_blast"
    }
}

def use_ray_of_sickness(character, target):
    print(f"\n{character.name} uses Ray of Sickness against {target.name}")
    damage = random.randint(20, 40) * character.spell_dam
    target.take_damage(damage)

def use_vampiric_touch(character, target):
    print(f"\n{character.name} uses Vampiric Touch against {target.name}")
    damage = random.randint(20, 40) * character.spell_dam
    heal = damage / 2
    target.take_damage(damage)
    character.heal(heal)

def use_ice_blast(character, target):
    print(f"\n{character.name} uses Ice Blast against {target.name}")
    damage = random.randint(15, 30) * character.spell_dam
    target.take_damage(damage)

# ---Barbarian Attacks---

def use_empowering_slash(character, target):
    print(f"\n{character.name} uses Empowering Slash against {target.name}")
    damage = random.randint(20, 30) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        character.apply_status_effect(status_effect.buff_phys_damage, 2, 1)

def use_patient_strike(character, target):
    print(f"\n{character.name} uses Patient Strike against {target.name}")
    damage = random.randint(30, 40) * character.phys_dam
    character.attack += 2
    on_hit = utils.roll_hit(character, target)
    character.attack -= 2
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_lethal_strike(character, target):
    print(f"\n{character.name} uses Lethal Strike against {target.name}")
    damage = random.randint(50, 70) * character.phys_dam
    character.attack -= 2
    on_hit = utils.roll_hit(character, target)
    character.attack += 2
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

#---Dark Blade Attacks---

def use_corrupting_slash(character, target):
    print(f"\n{character.name} uses Corrupting Slash against {target.name}")
    damage = random.randint(25, 40) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.debuff_ac, 2, 2)

def use_hidden_blade(character, target):
    print(f"\n{character.name} uses Hidden Blade against {target.name}")
    damage = random.randint(40, 55) * character.phys_dam
    character.attack += 1
    on_hit = utils.roll_hit(character, target)
    character.attack -= 1
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_corruption_blast(character, target):
    print(f"\n{character.name} uses Corruption Blast against {target.name}")
    damage = random.randint(20, 40) * character.spell_dam
    print(f"\n{character.name} hits {target.name}")
    target.take_damage(damage)
    target.apply_status_effect(status_effect.debuff_ac, 2, 2)

#---Dread Lord Attacks---

def use_hell_hammer_smash(character, target):
    print(f"\n{character.name} uses Hell Hammer Smash against {target.name}")
    damage = random.randint(30, 60) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.debuff_ac, 2, 2)

def use_engulfed_in_darkness(character, target):
    print(f"\n{character.name} uses Engulfed In Darkness against {target.name}")
    damage = random.randint(40, 55) * character.spell_dam
    print(f"\n{character.name} hits {target.name}")
    target.take_damage(damage)
    target.apply_status_effect(status_effect.debuff_attack, 2, 2)
    target.apply_status_effect(status_effect.debuff_ac, 2, 2)
    character.apply_status_effect(status_effect.buff_spell_damage, 2, 2)
    character.apply_status_effect(status_effect.buff_phys_damage, 2, 2)

def use_inferno(character, target):
    print(f"\n{character.name} uses Inferno against {target.name}")
    damage = random.randint(45, 60) * character.spell_dam
    print(f"\n{character.name} hits {target.name}")
    target.take_damage(damage)
    target.apply_status_effect(status_effect.debuff_attack, 2, 2)