import random #Imports the random library
import sys
from Game_character import Character #imports class Character, giving character attributes and stats
import enemy_character
from abilities import available_abilities
from attacks import available_attacks
from spells import available_spells #Imports spells list from spells
import attack_func
import spell_func
import item_func
import enemy_atk
import equipment
import inspect
import os
import time


# Defines the characters in the game
hero = Character("Tav", 100, 100, 100, 100, 1, 10, 3, 0, 0)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for selecting spell to all to hero's list 
def choose_spell(character):
    clear()
    print("---Choose a Spell or Attack---")
    
    spell_pool = [k for k in available_spells if k not in character.spells]
    attack_pool = [k for k in available_attacks if k not in character.phys_attacks]

    rand_spell = random.choice(spell_pool)
    rand_atk = random.choice(attack_pool)

    spell = available_spells[rand_spell]
    atk = available_attacks[rand_atk]
    
    print(f"\n1. Learn Spell: {spell['name']} - Damage: {spell['damage_range']} - Mana cost {spell['mana_cost']}\n{spell["description"]}")
    print(f"\n2. Learn Attack: {atk['name']} - Damage: {atk['damage_range']} - Mana cost {atk['mana_cost']}\n{atk["description"]}")

    while True:
        choice = (input("\nWhat do you what to choose: "))

        if choice == "1":
            character.spells[rand_spell] = available_spells[rand_spell]
            print(f"\n{character.name} has learnt {rand_spell}")
            time.sleep(3)
            break
        
        elif choice == "2":
            character.phys_attacks[rand_atk] = available_attacks[rand_atk]
            print(f"{character.name} has learnt {rand_atk}")
            time.sleep(3)
            break

        else:
            print("Invalid Choice, try again")
            time.sleep(3)

#function for leveling up Player
def level_up(character):
    clear()
    print("----Level Up----")
    print("Choose one of is options")
    print("\n1. Increase Max Health by 50")
    print("2. Increase Max Mana by 50")
    print("3. Increase Armour by 1")
    print("4. Increase Attack by 1")
    character.level += 1
    
    while True:
        choice = input("\nWhat do you choose?(input 1, 2, 3, 4,): ")
        if choice == "1":
            character.max_health += 50
            print(f"{character.name}'s Max Health is now {character.max_health}")
            time.sleep(3)
            break
        elif choice == "2":
            character.max_mana += 50
            print(f"{character.name}'s Max Mana is now {character.max_mana}")
            time.sleep(3)
            break
        elif choice == "3":
            character.ac += 1
            print(f"{character.name}'s Armour is now {character.ac}")
            time.sleep(3)
            break
        elif choice == "4":
            character.attack += 1
            print(f"{character.name}'s Max Attack is now {character.attack}")
            time.sleep(3)
            break
        else:
            print("Invalid Input")
            time.sleep(3)
    choose_spell(character)
    
    character.health += character.max_health
    character.mana += character.max_mana
    shop(character)

# Function for showing Player Stats
def show_player_stats(character):
    clear()
    print(f"---{character.name}'s Stats---")
    print(f"Level: {character.level}")
    print(f"Health: {character.health} / Max Health: {character.max_health}")
    print(f"Mana: {character.mana} / Max Mana: {character.max_mana}")
    print(f"Attack: {character.attack}")
    print(f"Armour: {character.ac}")
    print(f"Gold: {character.gold}")
    print("---Active status Effects---")
    for effect in character.status_effects:
        print(f"{effect.name} - Duration: {effect.duration}")
    
    input("\nPress Enter to contiune")

# Function for opening you Spells Menu
def open_spell_menu(character):
    print("---Spell Menu---")

    for key, spl in character.spells.items():
        name = spl["name"]
        dmg_min, dmg_max = spl["damage_range"]
        cost = spl["mana_cost"]
        description = spl["description"]
        print(f"\n{name} (Mana Cost: {cost}) / (Damage: {dmg_min} - {dmg_max})\n{description}")

# Function for opening your inventory
def open_inventory_menu(character, target):
    clear()
    print(f"You fight {target.name} the {target.race.name} {target.en_class.name}, his health is {target.health}")
    print(f"Defeat the {target.name} to continue to next Level")
    print("\n---Inventory Menu---")
    inv_list = []
    for item in character.inventory:
        if item.quanity > 0:
            print(f"{item.quanity}: {item.name}\n{item.description}")
            inv_list.append(item)
    
    while True:
        choice = input("\n What item would you like to use (or type 'back' to cancel): ").lower()

        if choice == "back":
            return False
        
        item_option = next((item for item in inv_list if item.name.lower() == choice), None)

        if item_option:
            item_option.use_fn(character, item_option)
            if item_option.quanity <= 0:
                character.remove_item(item_option)
            time.sleep(3)
            return False
        else:
            print("Invalid input")
            time.sleep(3)

# Function for opening your Attack Menu
def open_attack_menu(character):
    print("---Attack Menu---")

    for key, atk in character.phys_attacks.items():
        name = atk["name"]
        dmg_min, dmg_max = atk["damage_range"]
        description = atk["description"]
        print(f"\n{name} (Damage: {dmg_min} - {dmg_max})\n{description}")

# Function for player using spells
def player_spells(character, target):
    
    while True:
        clear()
        print(f"You fight {target.name} the {target.race.name} {target.en_class.name}, his health is {target.health}")
        print(f"Defeat the {target.name} to continue to next Level")
        open_spell_menu(character)
        choice = input("\nWhat spell would you like to use? (or type 'back' to cancel): ").lower()

        if choice == "back":
            print("Returning to menu")
            return False
        
        elif choice in character.spells:
            spl_opt = character.spells[choice]
            mana_cost = spl_opt["mana_cost"]

            if character.mana < mana_cost:
                print("\nNot enough Mana")
                return False
            else:
                effect_func_name = spl_opt["spell_func"]
                effect_func = getattr(spell_func, effect_func_name)
                sig = inspect.signature(effect_func)
                num_params = len(sig.parameters)
                if num_params == 1:
                    clear()
                    effect_func(character)
                    input("\nPress Enter to continue")
                else:
                    clear()
                    effect_func(character, target)
                    input("\nPress Enter to continue")
                return True

        else:
            print("\nInvalid Spell")
            time.sleep(3)

# Function for player attacking
def player_attack(character, target):

    while True:
        clear()
        print(f"You fight {target.name} the {target.race.name} {target.en_class.name}, his health is {target.health}")
        print(f"Defeat the {target.name} to continue to next Level")
        open_attack_menu(character)
        choice = input("\nWhat attack would you like to use? (or type 'back' to cancel): ").lower()
        if choice == "back":
            print("Returning to menu")
            return False

        elif choice in character.phys_attacks:
            atk_opt = character.phys_attacks[choice]
            effect_func_name = atk_opt["attack_func"]
            effect_func = getattr(attack_func, effect_func_name)
            clear()
            effect_func(character, target)
            input("\nPress Enter to continue")
            return True

        else:
            print("Invalid Attack")
            time.sleep(3)

def handle_villian_turn_new(villian, hero):
    clear()
    atk_options = list(villian.attacks.keys())
    choice = random.choice(atk_options)
    choice_func_name = villian.attacks[choice]["atk func"]
    choice_func = getattr(enemy_atk, choice_func_name)
    choice_func(villian, hero)
    input("\nPress Enter to continue")

#Function that handles the players turn
def handle_player_turn(hero, villian):
    #Loop for heros turn
    while True:
        clear()
        print(f"You fight {villian.name} the {villian.race.name} {villian.en_class.name}, his health is {villian.health}")
        print(f"Defeat the {villian.name} to continue to next Level")
        print("\n ----Here are your Options----")
        print("1: Open Attack Menu")
        print("2: Open Spell Menu")
        print("3: Open Inventory")
        print("4: Show Stats")

        # Get option from player
        option = input("\nEnter your command: ")

        if option == "1": #---Sword attack
            if not player_attack(hero, villian):
                continue #Continues loop if 
            break
        
        elif option == "2":#---Fireball
            if not player_spells(hero, villian):
                continue
            break
        
        elif option == "3":#---Use inventory
            if not open_inventory_menu(hero, villian):
                continue
            break

        elif option == "4":#---Show Stats
            show_player_stats(hero)

        else:
            print("Invalid input!")
            time.sleep(3)

#Function that handles Level one
def game_loop(hero, enemy):

    if hero.level > 1:
        equip_menu(hero)
        hero.health += hero.max_health
        hero.mana += hero.max_mana

    while hero.is_alive() and enemy.is_alive():
        handle_player_turn(hero, enemy)
        hero.start_turn()
        if enemy.is_alive():
            handle_villian_turn_new(enemy, hero)
            if enemy.is_alive():
                enemy.start_turn()
    
    if hero.is_alive():
        if hero.status_effects:
            for effect in hero.status_effects:
                hero.clear_status_effect(effect)
        clear()
        print("\n----You Win----")
        hero.gain_gold(enemy.gold_reward)
        level_up(hero)
        

    else:
        print("\n----You Lose----")
        sys.exit("\nGame Over")

def generate_enemy(hero):
    rand_class = random.choice(enemy_character.available_enemy_classes)
    rand_race = random.choice(enemy_character.available_enemy_races)
    rand_name = random.choice(enemy_character.enemy_name)
    new_villian = enemy_character.enemy(rand_name, rand_class, rand_race, hero.level)
    return new_villian

def shop(character):
    item_option = random.sample(item_func.available_items, 2)
    equipment_option = random.sample(equipment.available_equipment, 1)
    
    while True:
        clear()
        print("\n---Item Shop---")
        for item in item_option:
            print(f"\n{item.name} / Cost: {item.cost}\n{item.description}")
        for equip in equipment_option:
            print(f"\n{equip.name} / Cost: {equip.cost}\n{equip.description}")

        choice = input("\nChoose items from the shop to buy(or type sell to sell items or type 'exit' to exit): ").lower()
        if choice == "exit":
            return
        
        if choice == "sell":
            sell(character)

        item_choice = next((item for item in item_option if item.name.lower() == choice), None)
        equipment_choice = next((equip for equip in equipment_option if equip.name.lower() == choice), None)

        if item_choice:
            if item_choice.cost > character.gold:
                print("\nNot enough gold")
                time.sleep(3)
            elif item_choice:
                character.add_item(item_choice)
                character.gold -= item_choice.cost
                item_option.remove(item_choice)
        
        if equipment_choice:
            if equipment_choice.cost > character.gold:
                print("\nNot enough gold")
                time.sleep(3)
            elif equipment_choice:
                character.add_equipment(equipment_choice)
                equipment_option.remove(equipment_choice)

        else:
            print("Invalid Input")
            time.sleep(3)

def roll_hit(character, target):
    print(f"\n{character.name} rolls to hit against {target.name}")
    roll = random.randint(1, 20)
    on_hit = roll + character.attack
    print(f"{character.name} rolls a {roll} + (ATK) {character.attack} = {on_hit}")
    return on_hit

def equip_menu(character):

    
    while True:
        print(f"{character.name} can change there equipment before the fight!")
        print(f"\n--{character.name}'s Equipped Equipment--")
        print("\nRing Slot")
        for ring in character.ring_slot:
            print(f"{ring.name}")
        print("\nArmour Slot")
        for armour in character.armour_slot:
            print(f"{armour.name}")
        print("\nWeapon Slot")
        for weapon in character.weapon_slot:
            print(f"{weapon.name}")
        print("\nNecklace Slot")
        for necklace in character.necklace_slot:
            print(f"{necklace.name}")

        print(f"\n--Equipment Inventory--")
        for items in character.equipment_inv:
            print(f"\n{items.name}\n{items.description}")
        
        choice = input(f"\nChoose items to equip to {character.name} (type exit when finished!): ").lower()
        if choice == "exit":
            return
        item_choice = next((item for item in character.equipment_inv if item.name.lower() == choice), None)
        if item_choice: 
            character.equip_item(item_choice)
        else:
            print("\nInvalid input")
            time.sleep(3)

def sell(character):
    character_inventory = character.inventory
    character_equipment_inv = character.equipment_inv

    while True:
        clear()
        print("---Sell Items---")
        print(f"\n{character.name}'s Gold is {character.gold}")
        print("\n---Item Inventory---")
        for item in character_inventory:
            value = int(item.cost // 1.2)
            print(f"\n{item.quanity}: {item.name} / value: {value}\n{item.description}")
        
        print("\n---Equipment Inventory---")
        for items in character_equipment_inv:
            e_value = int(items.cost // 1.2)
            print(f"\n{items.quanity}: {items.name} / Value: {e_value}\n{items.description}")
        
        choice = input("\nChoose items to sell (or type exit to exit): ").lower()

        if choice == "exit":
            return
        
        item_option = next((item for item in character.inventory if item.name.lower() == choice), None)
        equip_option = next((equip for equip in character.equipment_inv if equip.name.lower() == choice), None)
        
        if item_option:
            character.gold += int(item_option.cost // 1.2)
            item_option.quanity -= 1
            if item_option.quanity <= 0:
                character.remove_item(item_option)
            print(f"{character.name} sold a {item_option.name} their gold is now {character.gold}")
            time.sleep(3)
        
        if equip_option:
            character.gold += int(equip_option.cost // 1.2)
            equip_option.quanity -= 1
            if equip_option.quanity <= 0:
                character.remove_equipment(equip_option)
            print(f"{character.name} sold a {equip_option.name} their gold is now {character.gold}")
            time.sleep(3)
        
        else:
            print("Invalid Input")
            time.sleep(3)
