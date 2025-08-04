import utils
import time
import pygame
hero = utils.hero
# Main function for game
def main():
    #pygame.mixer.init()
    #pygame.mixer.music.load("Coding_stuff/Python/Text Game/music/19 Hyrule Field Main Theme.mp3")
    #pygame.mixer.music.play(-1)
    utils.clear()
    print(f"Welcome to the game!")
    hero.name = input("What is your name: ")
    print(f"{hero.name}! Your health is {hero.health}. Your mana is {hero.mana}")
    print("Defeat the monster in each level to proceed to the next level")
    time.sleep(3)
    game_level = 1
    while hero.level < 10:
        
        villian = utils.generate_enemy(hero)
        utils.clear()
        print(f"----Welcome to Level {game_level}----")
        time.sleep(3)
        utils.game_loop(hero, villian)
        game_level += 1

    print("\n Congrates you Won the game!")


if __name__ == "__main__":
    main()