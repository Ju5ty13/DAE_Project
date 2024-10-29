import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.attributes = {'strength': 10, 'intelligence': 10, 'dexterity': 10}
        self.parried = False  # Tracks whether the next move is boosted
        print(f"Welcome, {self.name} the {self.character_class}!")

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.attributes['strength'] += 5
        self.attributes['intelligence'] += 3
        self.attributes['dexterity'] += 4
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"New attributes: {self.attributes}")

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

class Monster:
    def __init__(self, difficulty):
        self.name = random.choice(["Goblin", "Orc", "Troll", "Dragon"])
        self.health = random.randint(20, 30) + difficulty * 10
        self.attack_power = random.randint(5, 10) + difficulty * 2
        print(f"A wild {self.name} appears! Health: {self.health}, Attack Power: {self.attack_power}")

class Game:
    def __init__(self):
        self.characters = []
        self.difficulty = 1
        self.run_attempts = 0  # Counts consecutive run attempts

    def create_character(self):
        name = input("Enter your character's name: ")
        character_class = input("Enter your character's class (e.g., Warrior, Mage): ")
        new_character = Character(name, character_class)
        self.characters.append(new_character)
        return new_character

    def attack_monster(self, player, monster, attack_type):
        if attack_type == 1:
            hit_chance = 0.9
            damage = random.randint(5, 10)
        elif attack_type == 2:
            hit_chance = 0.7
            damage = random.randint(10, 20)
        elif attack_type == 3:
            hit_chance = 0.5
            damage = random.randint(20, 30)

        if player.parried:
            hit_chance += 0.2
            damage *= 2
            print("Your attack is boosted due to a successful parry!")

        if random.random() < hit_chance:
            monster.health -= damage
            print(f"You dealt {damage} damage to the {monster.name}. Monster's remaining health: {monster.health}")
        else:
            print("Your attack missed!")

        player.parried = False  # Reset parry boost after use

    def other_options(self, player):
        while True:
            other_action = input("Choose an option: 'dodge', 'parry', or 'run': ").lower()
            if other_action == "dodge":
                dodge_chance = 0.5
                if player.parried:
                    dodge_chance += 0.3
                    print("Dodge chance increased due to a successful parry!")
                if random.random() < dodge_chance:
                    print("You successfully dodged the attack!")
                else:
                    print("You tried to dodge but failed.")
                self.run_attempts = 0  # Reset run counter
                break
            elif other_action == "parry":
                if random.random() < 0.5:
                    print("Parry successful! Your next move will be boosted.")
                    player.parried = True
                else:
                    print("Parry failed!")
                self.run_attempts = 0  # Reset run counter
                break
            elif other_action == "run":
                encounter_chance = 0.3 + self.run_attempts * 0.2  # Base 30% chance, increased with each attempt
                if random.random() < encounter_chance:
                    print("You tried to run but encountered another monster!")
                    self.run_attempts += 1  # Increment run counter
                    return "new_monster"  # Trigger a new monster encounter
                else:
                    print("You successfully ran away!")
                    self.run_attempts = 0  # Reset run counter on successful escape
                    return "escape"  # Successful escape
            else:
                print("Invalid option. Please choose 'dodge', 'parry', or 'run'.")
        return None

    def fight_monster(self, player):
        monster = Monster(self.difficulty)
        while monster.health > 0 and player.health > 0:
            action = input("Choose your action: '1', '2', '3' (attack types) or 'other' for special options: ").lower()
            if action in ['1', '2', '3']:
                attack_type = int(action)
                self.attack_monster(player, monster, attack_type)
                
                if monster.health > 0:
                    retaliation = random.randint(1, monster.attack_power)
                    player.health -= retaliation
                    print(f"The {monster.name} dealt {retaliation} damage to you. Your remaining health: {player.health}")

            elif action == "other":
                result = self.other_options(player)
                if result == "new_monster":
                    monster = Monster(self.difficulty)  # Spawn a new monster
                elif result == "escape":
                    return  # End the fight if player successfully escapes

        if player.health > 0:
            print(f"You defeated the {monster.name}!")
            experience_gain = 50 + self.difficulty * 10
            player.gain_experience(experience_gain)
            print(f"You gained {experience_gain} experience.")
            self.difficulty += 1  # Increase difficulty for next monster
        else:
            print("You were defeated! Game over.")
            return False  # End the game

        return True  # Continue the game

    def play(self):
        player_character = self.create_character()
        print("Type 'fight' to encounter a monster or 'exit' to leave the game.")
        
        while True:
            action = input("What would you like to do? ").lower()
            if action == 'fight':
                if not self.fight_monster(player_character):
                    break  # End game if player is defeated
            elif action == 'exit':
                print(f"Thanks for playing, {player_character.name}!")
                break
            else:
                print("Unknown command. Please type 'fight' or 'exit'.")

# Example usage
if __name__ == "__main__":
    game = Game()
    game.play()
