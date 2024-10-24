class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.attributes = {'strength': 10,'intelligence': 10,'dexterity': 10}
        print (self, name, character_class)
        #Create character name, class, level, experience, & attributes.

    
    def level_up(self):
        self.level += 1
        # Increase attributes and give new abilities
        print(f"{self.name} leveled up to {self.level}!")

class Game:
    def __init__(self):
        self.characters = []

    def create_character(self, name, character_class):
        new_character = Character(name, character_class)
        self.characters.append(new_character)
    
    def save_game(self):
        # Implement save logic here
        pass

    def load_game(self):
        # Implement load logic here
        pass

# Example usage
game = Game()
game.create_character("Thorin", "Warrior")

