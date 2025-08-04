import random
import status_effect
import utils

def use_firebolt(character, target):
    print(f"\n{character.name} uses Firebolt against {target.name}")
    damage = random.randint(20, 40)
    character.use_mana(25)
    target.take_damage(damage)

def use_god(character, target):
    print(f"\n{character.name} uses God against {target.name}")
    damage = random.randint(1000, 1100)
    print(f"\n{character.name} hits {target.name}")
    target.take_damage(damage)

def use_fireball(character, target):
    print(f"\n{character.name} uses Fireball against {target.name}")
    damage = random.randint(25, 50)
    character.use_mana(50)
    target.take_damage(damage)

def use_ice_shard(character, target):
    print(f"\n{character.name} uses Ice Shard against {target.name}")
    damage = random.randint(15, 30)
    character.use_mana(25)
    target.take_damage(damage)

def use_shocking_grasp(character, target):
    print(f"\n{character.name} uses Shocking Grasp against {target.name}")
    damage = random.randint(40, 60)
    character.use_mana(60)
    target.take_damage(damage)

def use_improved_shield(character):
    print(f"\n{character.name} uses Improved Shield")
    character.use_mana(80)
    character.apply_status_effect(status_effect.buff_ac, 3, 4)

def use_shield(character):
    print(f"\n{character.name} uses Shield")
    character.use_mana(40)
    character.apply_status_effect(status_effect.buff_ac, 2, 2)

def use_enchant_weapon(character):
    print(f"\n{character.name} uses Enchant Weapon")
    character.use_mana(60)
    character.apply_status_effect(status_effect.buff_attack, 2, 3)

def use_vampiric_touch(character, target):
    print(f"\n{character.name} uses Vampiric Touch against {target.name}")
    damage = random.randint(25, 40)
    character.use_mana(70)
    target.take_damage(damage)
    character.heal(damage / 2)

def use_incinerate(character, target):
    print(f"\n{character.name} uses Incinerate against {target.name}")
    damage = random.randint(100, 150)
    character.use_mana(100)
    target.take_damage(damage)

def use_sap_strength(character, target):
    print(f"\n{character.name} uses Sap Strength against {target.name}")
    damage = random.randint(20, 40)
    character.use_mana(60)
    target.take_damage(damage)
    target.apply_status_effect(status_effect.debuff_attack, 2, 3)

def use_berserk(character):
    print(f"\n{character.name} uses berserk")
    character.use_mana(80)
    character.apply_status_effect(status_effect.buff_phys_damage, 3, 2)