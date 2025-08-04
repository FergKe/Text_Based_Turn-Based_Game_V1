import status_effect
import random
# Enemy Class
class enemy():
    def __init__(self, name, en_class, race, level):
        self.name = name
        self.en_class = en_class
        self.race = race
        self.level = level
        self.max_health = (en_class.health + race.health) * ((self.level +1) // 2)
        self.health = self.max_health
        self.clamped_health = min(self.health, self.max_health)
        self.ac = en_class.ac + race.ac + ((level +1) // 2)
        self.attack = en_class.attack + race.attack + ((level +1) // 2)
        self.phys_res = en_class.phys_res + race.phys_res
        self.toxic_res = en_class.toxic_res + race.toxic_res
        self.attacks = dict(en_class.attacks)
        self.phys_dam = ((level +3) // 3)
        self.spell_dam = ((level +3) // 3)
        self.status_effects = []
        self.gold_reward = random.randint(30, 50) * level

    @property
    def health(self):
        return self.clamped_health
        
    @health.setter
    def health(self, value):
        self.clamped_health = max(0, min(value, self.max_health))
    
     # Function for being alive 
    def is_alive(self):
        return self.health > 0
    
    # Function for being dead
    def is_not_alive(self):
        return self.health <= 0
    
    # Function for taking damage
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} has taken {amount} damage, their health is {self.health}")

    #Function for Healing health
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} has healed {amount}, their health is {self.health}")
    
    def apply_status_effect(self, effect: status_effect, duration, value):
        if effect in self.status_effects:
            if effect.duration > duration:
                effect.duration = effect.duration
            else:
                effect.duration = duration
            if effect.value < value:
                effect.value = value
            return
        effect.duration = duration
        effect.value = value
        effect.apply_fn(self, effect)
        self.status_effects.append(effect)


    def start_turn(self):
        expired = []
        for effect in self.status_effects:
            if effect.on_turn_start(self):
                expired.append(effect)
            for effect in expired:
                self.status_effects.remove(effect)

class enemy_class:
    def __init__(self, name, health, attack, ac, phys_res, toxic_res, attacks):
        self.name = name
        self.health = health
        self.attack = attack
        self.ac = ac
        self.phys_res = phys_res
        self.toxic_res = toxic_res
        self.attacks = attacks

class enemy_race:
    def __init__(self, name, health, attack, ac, phys_res, toxic_res):
        self.name = name
        self.health = health
        self.attack = attack
        self.ac = ac
        self.phys_res = phys_res
        self.toxic_res = toxic_res


fighter = enemy_class(
    name="Fighter",
    health=60,
    attack=2,
    ac=11,
    phys_res=0,
    toxic_res=0,
    attacks={
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
)

wizard = enemy_class(
    name="Wizard",
    health=40,
    attack=0,
    ac=8,
    phys_res=0,
    toxic_res=0,
    attacks={
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
)

thief = enemy_class(
    name="Thief",
    health=50,
    attack=1,
    ac=10,
    phys_res=0,
    toxic_res=0,
    attacks={
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
)

barbarian = enemy_class(
    name="Barbarian",
    health=70,
    attack=3,
    ac=8,
    phys_res=0,
    toxic_res=0,
    attacks={
        "empowering slash": {
            "name" : "Empowering Slash",
            "atk func" : "use_empowering_slash"
        },
        "patient strike": {
            "name" : "Patient Strike",
            "atk func" : "use_patient_strike"
        },
        "lethal strike": {
            "name" : "Lethal Strike",
            "atk func" : "use_lethal_strike"
        }
    }
)

dark_blade = enemy_class(
    name="Dark Blade",
    health=40,
    attack=3,
    ac=10,
    phys_res=0,
    toxic_res=0,
    attacks={
        "corrupting slash": {
            "name" : "Corrupting Slash",
            "atk func" : "use_corrupting_slash"
        },
        "hidden blade": {
            "name" : "Hidden Blade",
            "atk func" : "use_hidden_blade"
        },
        "corruption blast": {
            "name" : "Corruption Blast",
            "atk func" : "use_corruption_blast"
        }
    }
)

dread_lord = enemy_class(
    name="Dread Lord",
    health=70,
    attack=3,
    ac=12,
    phys_res=0,
    toxic_res=0,
    attacks={
        "hell hammer smash": {
            "name" : "Hell Hammer Smash",
            "atk func" : "use_hell_hammer_smash"
        },
        "engulfed in darkness": {
            "name" : "Engulfed In Darkness",
            "atk func" : "use_engulfed_in_darkness"
        },
        "inferno": {
            "name" : "Inferno",
            "atk func" : "use_inferno"
        }
    }
)

dark_elf = enemy_race(
    name="Dark Elf",
    health=0,
    attack=1,
    ac=0,
    phys_res=0,
    toxic_res=0
)

undead = enemy_race(
    name="Undead",
    health=20,
    attack=0,
    ac=0,
    phys_res=0,
    toxic_res=0
)

goblin = enemy_race(
    name="Goblin",
    health=10,
    attack=0,
    ac=0,
    phys_res=0,
    toxic_res=0
)

human = enemy_race(
    name="Human",
    health=0,
    attack=1,
    ac=1,
    phys_res=0,
    toxic_res=0
)

golum = enemy_race(
    name="Golum",
    health=30,
    attack=0,
    ac=3,
    phys_res=0,
    toxic_res=0
)

demon = enemy_race(
    name="Demon",
    health=10,
    attack=2,
    ac=1,
    phys_res=0,
    toxic_res=0
)

Orc = enemy_race(
    name="Orc",
    health=20,
    attack=2,
    ac=0,
    phys_res=0,
    toxic_res=0
)

enemy_name = ["Gaz", "Grog", "Dunk", "Snork", "Zobble", "Grint", "Nerk", "Granny", "Bob", "Dave", "Klemp"]
available_enemy_classes = [fighter, thief, wizard, dark_blade, dread_lord, barbarian]
available_enemy_races = [dark_elf, goblin, undead, human, golum, demon, Orc]



