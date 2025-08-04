#Character attributes that govern the stats of each character
import status_effect
import item_func
import random
import equipment
class Character:
    def __init__(self, name, health, max_health, mana, max_mana, level, ac, attack, phys_res, toxic_res):
        self.name = name
        self.max_health = max_health
        self.clamped_health = min(health, max_health)
        self.max_mana = max_mana
        self.clamped_mana = min(mana, max_mana)
        self.ac = ac
        self.attack = attack
        self.level = level
        self.phys_dam = 1
        self.spell_dam = 1
        self.phys_res = phys_res
        self.toxic_res = toxic_res
        self.ring_slot = []
        self.armour_slot = []
        self.weapon_slot = []
        self.necklace_slot = []
        self.status_effects = []
        self.equipment_inv = []
        self.inventory = [item_func.health_potion, item_func.mana_potion]
        self.gold = 0
        self.phys_attacks = {
            "slash": {
            "name": "Slash",
            "damage_range": (10, 30),
            "mana_cost": 0,
            "description": "A weak physical attack, doing low damage",
            "attack_func": "use_slash"
            }

        }
        self.spells = {
            "firebolt": {
                "name": "Firebolt",
                "damage_range": (20, 40),
                "mana_cost": 25,
                "description": "A weak spell, doing low damage",
                "spell_func": "use_firebolt"
            },
            "god": {
                "name": "God",
                "damage_range": (1000, 1100),
                "mana_cost": 0,
                "description": "Win Everything!",
                "spell_func": "use_god"
            },
            
        }
        self.abilities ={

        }
    
    @property 
    def health(self):
        return self.clamped_health
    
    @health.setter #Set health so it can't go above max health and below 0
    def health(self, value):
        self.clamped_health = max(0, min(value, self.max_health))
    
    @property
    def mana(self):
        return self.clamped_mana
    
    @mana.setter #Set mana so it can't go above max mana and below 0
    def mana(self,value):
        self.clamped_mana = max(0, min(value, self.max_mana))

    # Function for dealing damage
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} has taken {amount} damage, their health is {self.health}")
    
    #Function for Healing health
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} has healed {amount}, their health is {self.health}")

    # Function for being alive 
    def is_alive(self):
        return self.health > 0
    
    # Function for being dead
    def is_not_alive(self):
        return self.health <= 0
    
    # Function for using mana
    def use_mana(self, amount):
        self.mana -= amount
        print(f"{self.name} used {amount}, their mana is {self.mana}")
    
    #Function to restore mana
    def restore_mana(self, amount):
        self.mana += amount
        print(f"{self.name} restores {amount} mana, their mana is now {self.mana}")

    #function for using inventory
    def use_item(self, item):
        if item == "health potion":
            if self.inventory["health potion"] > 0:
                print(f"\n{self.name} drinks a Health Potion")
                regen = random.randint(10, 20)
                self.heal(regen)
                self.inventory["health potion"] -= 1
            else:
                print("\nYou have no Health Potions")

        elif item == "mana potion":
            if self.inventory["mana potion"] > 0:
                print(f"\n{self.name} drinks a Mana Potion")
                self.restore_mana(50)
                self.inventory["mana potion"] -= 1
            else:
                print("\nYou have no Mana Potions")
    
    def learn_spell(self, key, spell_data):
        self.spells[key] = spell_data
        print(f"{self.name} has learnt a new spell: {spell_data['name']}")
    
    def learn_atk(self, key, atk_data):
        self.phys_attacks[key] = atk_data
        print(f"{self.name} has learnt a new spell: {atk_data['name']}")
    
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
    
    def add_item(self, item):
        print(f"\n{self.name} gained a {item.name}")
        if item in self.inventory:
            item.quanity += 1
            return
        self.inventory.append(item)
        return
    
    def remove_item(self, item):
        self.inventory.remove(item)
        return
    
    def remove_equipment(self, item):
        self.equipment_inv.remove(item)
        return
    
    def gain_gold(self, gold):
        self.gold += gold
        print(f"\n{self.name} gained {gold} gold, their total gold is {self.gold}")
    
    def clear_status_effect(self, effect:status_effect):
        for status in self.status_effects:
            status.remove_fn(self, effect)
            self.status_effects.remove(status)
    
    def add_equipment(self, item):
        print(f"\n{self.name} gained a {item.name}")
        if item in self.equipment_inv:
            item.quanity += 1
            return
        self.equipment_inv.append(item)
        return

    def equip_item(self, item:equipment):
        if isinstance(item, equipment.ring):
            self.equip_ring(item)
        elif isinstance(item, equipment.necklace):
            self.equip_necklace(item)
        elif isinstance(item, equipment.armour):
            self.equip_armour(item)
        elif isinstance(item, equipment.weapon):
            self.equip_weapon(item)

    def equip_ring(self, ring:equipment):
        if self.ring_slot:
            for equipment in self.ring_slot:
                self.ac -= equipment.ac
                self.attack -= equipment.attack
                self.max_health -= equipment.health
                self.max_mana -= equipment.mana
                self.phys_dam -= equipment.phys_dam
                self.spell_dam -= equipment.spell_dam
                self.equipment_inv.append(equipment)
                self.ring_slot.remove(equipment)
        self.ring_slot.append(ring)
        self.equipment_inv.remove(ring)
        self.ac += ring.ac
        self.attack += ring.attack
        self.max_health += ring.health
        self.max_mana += ring.mana
        self.phys_dam += ring.phys_dam
        self.spell_dam += ring.spell_dam

    def equip_necklace(self, item:equipment):
        if self.necklace_slot:
            for equipment in self.necklace_slot:
                self.ac -= equipment.ac
                self.attack -= equipment.attack
                self.max_health -= equipment.health
                self.max_mana -= equipment.mana
                self.phys_dam -= equipment.phys_dam
                self.spell_dam -= equipment.spell_dam
                self.equipment_inv.append(equipment)
                self.necklace_slot.remove(equipment)
        self.necklace_slot.append(item)
        self.equipment_inv.remove(item)
        self.ac += item.ac
        self.attack += item.attack
        self.max_health += item.health
        self.max_mana += item.mana
        self.phys_dam += item.phys_dam
        self.spell_dam += item.spell_dam
    
    def equip_weapon(self, item:equipment):
        if self.weapon_slot:
            for equipment in self.weapon_slot:
                self.ac -= equipment.ac
                self.attack -= equipment.attack
                self.max_health -= equipment.health
                self.max_mana -= equipment.mana
                self.phys_dam -= equipment.phys_dam
                self.spell_dam -= equipment.spell_dam
                self.equipment_inv.append(equipment)
                self.weapon_slot.remove(equipment)
        self.weapon_slot.append(item)
        self.equipment_inv.remove(item)
        self.ac += item.ac
        self.attack += item.attack
        self.max_health += item.health
        self.max_mana += item.mana
        self.phys_dam += item.phys_dam
        self.spell_dam += item.spell_dam
    
    def equip_armour(self, item:equipment):
        if self.armour_slot:
            for equipment in self.armour_slot:
                self.ac -= equipment.ac
                self.attack -= equipment.attack
                self.max_health -= equipment.health
                self.max_mana -= equipment.mana
                self.phys_dam -= equipment.phys_dam
                self.spell_dam -= equipment.spell_dam
                self.equipment_inv.append(equipment)
                self.armour_slot.remove(equipment)
        self.armour_slot.append(item)
        self.equipment_inv.remove(item)
        self.ac += item.ac
        self.attack += item.attack
        self.max_health += item.health
        self.max_mana += item.mana
        self.phys_dam += item.phys_dam
        self.spell_dam += item.spell_dam