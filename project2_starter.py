"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Madison Wilkins
Date: November 8th (Post Hackathon Sadly.)

AI Usage: AI was used for general debugging assistance (ChatGPT) and code optimization suggestions (Copilot). 
It also changed the testing code so it would run automatically.
"""
import random
# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ================================================================================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ================================================================================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic, weapon=None):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = weapon
        
    def attack(self, target):

        damage = random.randint(1 , round(self.strength * 1.5))
        target.take_damage(damage)
        if damage > self.strength:
            print(f"[BASIC ATTACK] {self.name} attacks {target.name}, dealing {damage} damage!")
        else:
            print(f"[CHARGED BASIC ATTACK] {self.name} attacks {target.name}, dealing {damage} damage!")
    
    def take_damage(self, damage):
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage
        pass
        
    def display_stats(self):
        print(f"╰┈➤ˎˊ˗ {self.name.upper()}'S BATTLE STATS !")
        print(f" Strength: {self.strength}")
        print(f" Magic: {self.magic}")
        print(f" Health: {self.health}")
        print("╰┈➤ˎˊ˗ -----------------------------")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    def __init__(self, name, character_class, health, strength, magic):
        """Initialize a player character."""
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Show everything from Character + player-specific info."""
        super().display_stats()
        print(f" Class: {self.character_class}")
        print(f" Level: {self.level}")
        print(f" Experience: {self.experience}")
        print("╰┈➤ˎˊ˗ -----------------------------")
        print()
# ================================================================================================================================
class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        self.level = 1
        super().__init__(name, character_class="Warrior", health = (100 + (self.level - 1) * 5), strength = (12 + (self.level - 1) * 5), magic = (2 + (self.level - 1) * 1))
      
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        damage = random.randint(round(self.strength * 0.5), round((self.strength * 1.5) * 1.5))
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        if damage > (self.strength * 1.5) :
            print(f"[SUPER-CHARGED WARRIOR ATTACK] {self.name} slashes {target.name}, dealing {damage} damage!")
        elif damage <= (self.strength * 1.5) and damage > self.strength:
            print(f"[CHARGED WARRIOR ATTACK] {self.name} slashes {target.name}, dealing {damage} damage!")
        else:
            print(f"[WARRIOR ATTACK] {self.name} slashes {target.name}, dealing {damage} damage!")

        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = random.randint(10, round((self.strength * 2.5) * 2.5))
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        if damage > (self.strength * 2.5) :
            print(f"[SUPER-CHARGED HEFTY STRIKE] {self.name} strikes {target.name}, dealing {damage} damage!")
        elif damage <= (self.strength * 2.5) and damage > self.strength:
            print(f"[CHARGED HEFTY STRIKE] {self.name} strikes {target.name}, dealing {damage} damage!")
        else:
            print(f"[HEFTY STRIKE] {self.name} strikes {target.name}, dealing {damage} damage!")

# ================================================================================================================================

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        self.level = 1
        super().__init__(name, character_class="Mage", health = (80 + (self.level - 1) * 3), strength = (5 + (self.level - 1) * 2), magic = (15 + (self.level - 1) * 5))

        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = random.randint(1, round((self.magic * 1.5) * 1.5))
        if self.weapon:
            damage += self.weapon.damage_bonus

        target.take_damage(damage)
        if damage > (self.magic * 1.5) :
            print(f"[SUPER-CHARGED MAGE ATTACK] {self.name} casts a spell on {target.name}, dealing {damage} damage!")
        elif damage <= (self.magic * 1.5) and damage > self.magic:
            print(f"[CHARGED MAGE ATTACK] {self.name} casts a spell on {target.name}, dealing {damage} damage!")
        else:
            print(f"[MAGE ATTACK] {self.name} casts a spell on {target.name}, dealing {damage} damage!")
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = random.randint(round(self.magic), round((self.magic * 2.5) * 2))
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        if damage > (self.magic * 2.5) :
            print(f"[SUPER-CHARGED FIREBALL] {self.name} hurls a fireball at {target.name}, dealing {damage} damage!")
        elif damage <= (self.magic * 2.5) and damage > self.magic:
            print(f"[CHARGED FIREBALL] {self.name} hurls a fireball at {target.name}, dealing {damage} damage!")
        else:
            print(f"[FIREBALL] {self.name} hurls a fireball at {target.name}, dealing {damage} damage!")
# ================================================================================================================================

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        self.level = 1
        super().__init__(name, character_class="Rogue", health = (90 + (self.level - 1) * 3), strength = (7 + (self.level - 1) * 3), magic = (5 + (self.level - 1) * 3))
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        damage = random.randint(1, round((self.strength * 1.5) * 3))
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        if damage > (self.strength * 1.5) :
            print(f"[SUPER-CHARGED ROGUE ATTACK] {self.name} swiftly strikes {target.name}, dealing {damage} damage!")
        elif damage <= (self.strength * 1.5) and damage > self.strength:
            print(f"[CHARGED ROGUE ATTACK] {self.name} swiftly strikes {target.name}, dealing {damage} damage!")
        else:
            print(f"[ROGUE ATTACK] {self.name} swiftly strikes {target.name}, dealing {damage} damage!")
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = random.randint(round(self.strength * 2.5), round(self.strength * 6.5))
        if self.weapon:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        print(f"[SNEAK ATTACK] {self.name} performs a sneak attack on {target.name}, dealing {damage} damage!")

# ================================================================================================================================

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print("╰┈➤ˎˊ˗ -----------------------------")
        print(f"CURRENT WEAPON: {self.name} | DAMAGE BONUS : {self.damage_bonus}")
        print("DESCRIPTION: A trusty weapon to aid in your battles.")
        print("╰┈➤ˎˊ˗ -----------------------------")
        print()


# ========================================================================================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ========================================================================================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Assign weapons to characters
    warrior.weapon = sword
    mage.weapon = staff
    rogue.weapon = dagger
    
    # Demonstrate attack with weapons
    print("\n⚔️ Testing Attacks With Weapons:")
    enemy = Character("Orc", 100, 5, 5)
    warrior.attack(enemy)
    enemy.health = 100
    mage.attack(enemy)
    enemy.health = 100
    rogue.attack(enemy)
    
    # Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
