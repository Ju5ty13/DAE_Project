import random  # Importing random for generating unpredictable monster selection and attack outcomes

class Character:
    """Represents the player character with a name and health."""

    def __init__(self, name):
        """Initializes the character with a name and full health."""
        self.name = name
        self.health = 100
        print(f"Welcome, {self.name}!")

    def take_damage(self, damage):
        """Reduces character's health by the specified damage amount."""
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")


class Monster:
    """Represents a monster with a name, health, and attack power."""

    def __init__(self, name, health, attack_power):
        """Initializes the monster with given name, health, and attack power."""
        self.name = name
        self.health = health
        self.attack_power = attack_power
        print(f"A wild {self.name} appears! Health: {self.health}")

    def take_damage(self, damage):
        """Reduces monster's health by the specified damage amount."""
        self.health -= damage
        print(f"The {self.name} took {damage} damage. Remaining health: {self.health}")


class Game:
    """Main game class that controls gameplay flow, monster generation, and combat."""

    def __init__(self):
        """Initializes the game with a list of potential monsters."""
        self.monster_pool = [
            {"name": "Goblin", "health": 30, "attack_power": 5},
            {"name": "Orc", "health": 50, "attack_power": 10},
        ]

    def create_character(self):
        """Prompts the player to enter a character name and creates the player character."""
        name = input("Enter your character's name: ")
        return Character(name)

    def get_random_monster(self):
        """Selects a random monster from the monster pool and returns an instance of Monster."""
        monster_info = random.choice(self.monster_pool)
        return Monster(monster_info["name"], monster_info["health"], monster_info["attack_power"])

    def play_turn(self, player, monster):
        """Executes a single turn in combat where the player can attack or attempt to dodge."""
        action = input("Choose your action: 'attack' or 'dodge': ").lower()
        if action == 'attack':
            damage = random.randint(5, 15)  # Random damage dealt by the player
            monster.take_damage(damage)
            if monster.health > 0:
                player.take_damage(monster.attack_power)  # Monster counter-attacks if still alive
        elif action == 'dodge':
            if random.random() < 0.5:  # 50% chance of successfully dodging
                print("You dodged the attack!")
            else:
                print("Dodge failed!")
                player.take_damage(monster.attack_power)  # Player takes damage if dodge fails
        else:
            print("Invalid action. Please choose 'attack' or 'dodge'.")

    def fight_monster(self, player):
        """Manages a combat encounter between the player and a randomly selected monster."""
        monster = self.get_random_monster()
        while monster.health > 0 and player.health > 0:
            self.play_turn(player, monster)
        
        if player.health > 0:
            print(f"You defeated the {monster.name}!")
        else:
            print("You were defeated! Game over.")

    def play(self):
        """Starts the game loop, allowing the player to fight consecutive monsters until defeated."""
        player_character = self.create_character()
        while player_character.health > 0:
            self.fight_monster(player_character)
            if player_character.health <= 0:
                print(f"Game over, {player_character.name}!")
                break
            else:
                print("Prepare for the next monster!")


# Entry point for running the game
if __name__ == "__main__":
    game = Game()
    game.play()
