import random
import utils
import status_effect

#Function for Slash
def use_slash(character, target):
    print(f"\n{character.name} uses Slash against {target.name}")
    damage = random.randint(10, 30) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_hammer_toss(character, target):
    print(f"\n{character.name} uses Hammer Toss against {target.name}")
    damage = random.randint(30, 45) * character.phys_dam
    character.attack -= 2
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
        character.attack += 2
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        character.attack += 2

def use_headbutt(character, target):
    print(f"\n{character.name} uses Headbutt against {target.name}")
    damage = random.randint(70, 80) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        character.take_damage(10)

def use_stab(character, target):
    print(f"\n{character.name} uses Stab against {target.name}")
    damage = random.randint(5, 15) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.bleed, 2, 10)

def use_piercing_strike(character, target):
    print(f"\n{character.name} uses Piercing Strike against {target.name}")
    damage = random.randint(20, 25) * character.phys_dam
    target.ac -= 2
    on_hit = utils.roll_hit(character, target)
    target.ac += 2
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_off_balancing_blow(character, target):
    print(f"\n{character.name} uses Off Balancing Blow against {target.name}")
    damage = random.randint(10, 20) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.debuff_attack, 3, 2)

def use_crushing_blow(character, target):
    print(f"\n{character.name} uses Crushing Blow against {target.name}")
    damage = random.randint(35, 45) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.debuff_ac, 3, 2)

def use_devastating_strike(character, target):
    print(f"\n{character.name} uses Devastating Strike against {target.name}")
    damage = random.randint(90, 110) * character.phys_dam
    character.attack -= 4
    on_hit = utils.roll_hit(character, target)
    character.attack += 4
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_risky_maneuver(character, target):
    print(f"\n{character.name} uses Risky Maneuver against {target.name}")
    damage = random.randint(20, 100) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
    character.apply_status_effect(status_effect.debuff_ac, 3, 2)

def use_defensive_strike(character, target):
    print(f"\n{character.name} uses Defensive Strike against {target.name}")
    damage = random.randint(10, 30) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        character.apply_status_effect(status_effect.buff_ac, 3, 2)

def use_frying_pan_to_the_face(character, target):
    print(f"\n{character.name} uses Frying Pan To The Face against {target.name}")
    damage = random.randint(70, 100) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)

def use_lacerate(character, target):
    print(f"\n{character.name} uses Lacerate against {target.name}")
    damage = random.randint(20, 35) * character.phys_dam
    on_hit = utils.roll_hit(character, target)
    if on_hit < target.ac:
        print(f"\n{character.name} misses {target.name}")
    else:
        print(f"\n{character.name} hits {target.name}")
        target.take_damage(damage)
        target.apply_status_effect(status_effect.bleed, 3, 25)
