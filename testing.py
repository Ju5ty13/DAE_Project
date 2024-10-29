class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.attributes = {'strength': 10, 'intelligence': 10, 'dexterity': 10}
        print(f"Welcome, {self.name} the {self.character_class}!")
        print(f"Starting attributes: {self.attributes}")

    def level_up(self):
        self.level += 1
        self.attributes['strength'] += 5  # Example attribute increase
        self.attributes['intelligence'] += 3
        self.attributes['dexterity'] += 4
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"New attributes: {self.attributes}")

class Game:
    def __init__(self):
        self.characters = []

    def create_character(self):
        print("Welcome to the Game!")
        name = input("Enter your character's name: ")
        character_class = input("Welcome Enter your character's class (e.g., Warrior, Mage): ")
        new_character = Character(name, character_class)
        self.characters.append(new_character)
        return new_character

    def play(self):
        player_character = self.create_character()
        print("Type 'level up' to gain experience or 'exit' to leave the game.")
        
        while True:
            action = input("What would you like to do? ").lower()
            if action == 'level up':
                player_character.level_up()
            elif action == 'exit':
                print(f"Thanks for playing, {player_character.name}!")
                break
            else:
                print("Unknown command. Please type 'level up' or 'exit'.")
if __name__ == "__main__":
    game = Game()
    game.play()
