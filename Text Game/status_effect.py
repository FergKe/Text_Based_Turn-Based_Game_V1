
class status_effect:
    def __init__(self, name, duration, value, apply_fn, remove_fn, per_turn_fn=None):
        self.name = name
        self.duration = duration
        self.value = value
        self.apply_fn = apply_fn
        self.remove_fn = remove_fn
        self.per_turn_fn = per_turn_fn
    
    def on_turn_start(self, target):
        if self.per_turn_fn: 
            self.per_turn_fn(target, self)
        self.duration -= 1
        if self.duration <= 0:
            self.remove_fn
            return True
        return False


def apply_bleed(target, effect: status_effect):
    print(f"{target.name} is {effect.name}")

def remove_bleed(target, effect: status_effect):
    print(f"{target.name} is not longer {effect.name}")

def bleed_per_turn(target, effect: status_effect):
    target.health -= effect.value
    print(f"\n{target.name} takes {effect.value} damage from bleed, there health is {target.health}")

bleed = status_effect(
    name="Bleeding",
    duration=0,
    value=0,
    apply_fn=apply_bleed,
    remove_fn=remove_bleed,
    per_turn_fn=bleed_per_turn
)

def apply_slow(target):
    print(f"{target.name} is slowed")

def remove_slow(target):
    print(f"{target.name} is no longer slowed")

def slow_per_turn(target):
    from utils import handle_player_turn
    from utils import hero
    print(f"{target.name} misses its turn")
    handle_player_turn(hero, target)

slow = status_effect(
    name="Slow",
    duration=0,
    value=0,
    apply_fn=apply_slow,
    remove_fn=remove_slow,
    per_turn_fn=slow_per_turn,
)

def apply_buff_ac(target, effect:status_effect):
    print(f"{target.name}'s AC has increased")
    target.ac += effect.value

def remove_buff_ac(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.ac -= effect.value

def buff_ac_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

buff_ac = status_effect(
    name="Buff AC",
    duration=0,
    value=0,
    apply_fn=apply_buff_ac,
    remove_fn=remove_buff_ac,
    per_turn_fn=buff_ac_per_turn,
)

def apply_debuff_ac(target, effect:status_effect):
    print(f"{target.name}'s AC has decreased")
    target.ac -= effect.value

def remove_debuff_ac(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.ac += effect.value

def debuff_ac_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

debuff_ac = status_effect(
    name="Debuff AC",
    duration=0,
    value=0,
    apply_fn=apply_debuff_ac,
    remove_fn=remove_debuff_ac,
    per_turn_fn=debuff_ac_per_turn,
)

def apply_buff_attack(target, effect:status_effect):
    print(f"{target.name}'s Attack has increased")
    target.ac += effect.value

def remove_buff_attack(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.ac -= effect.value

def buff_attack_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

buff_attack = status_effect(
    name="Buff Attack",
    duration=0,
    value=0,
    apply_fn=apply_buff_attack,
    remove_fn=remove_buff_attack,
    per_turn_fn=buff_attack_per_turn,
)

def apply_debuff_attack(target, effect:status_effect):
    print(f"{target.name}'s Attack has decreased")
    target.ac -= effect.value

def remove_debuff_attack(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.ac += effect.value

def debuff_attack_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

debuff_attack = status_effect(
    name="Debuff Attack",
    duration=0,
    value=0,
    apply_fn=apply_debuff_attack,
    remove_fn=remove_debuff_attack,
    per_turn_fn=debuff_attack_per_turn,
)

def apply_buff_phys_damage(target, effect:status_effect):
    print(f"{target.name}'s Physical damage has increased")
    target.phys_dam += effect.value

def remove_buff_phys_damage(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.phys_dam -= effect.value

def buff_phys_damage_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

buff_phys_damage = status_effect(
    name="Buff Physical Damage",
    duration=0,
    value=0,
    apply_fn=apply_buff_phys_damage,
    remove_fn=remove_buff_phys_damage,
    per_turn_fn=buff_phys_damage_per_turn,
)

def apply_buff_spell_damage(target, effect:status_effect):
    print(f"{target.name}'s Physical damage has increased")
    target.spell_dam += effect.value

def remove_buff_spell_damage(target, effect:status_effect):
    print(f"{target.name} Lost his buff")
    target.spell_dam -= effect.value

def buff_spell_damage_per_turn(target, effect: status_effect):
    print(f"{target.name}'s has {effect.name}")

buff_spell_damage = status_effect(
    name="Buff Spell Damage",
    duration=0,
    value=0,
    apply_fn=apply_buff_spell_damage,
    remove_fn=remove_buff_spell_damage,
    per_turn_fn=buff_spell_damage_per_turn,
)