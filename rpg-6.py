"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        r1 = random.randint(1,5)
        if r1 == 2:
            damage_output = self.power*2
        else:
            damage_output = self.power
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(damage_output)
        time.sleep(1.5)
        
    def receive_damage(self, points):
        
        if 

        else:
            if (points - self.armor) <= 0:
                print("%s received no damage." % self.name)
            else:
                self.health -= points - self.armor
                print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def collect_bounty(self, enemy):
        self.coins += enemy.bounty

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 6

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 2

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 2
        self.bounty = 0

     def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)
        r2 = random.randint(1,5)
        if r2 == 4:
            self.health += 2
            print("%s healed itself!" % self.name)
            
class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2
        self.bounty = 2

     def receive_damage(self, points):
        r3 = random.randint(1, 10)
        if r3 == 8:
            self.health -= points
            print("%s received %d damage." % (self.name, points))
        else:
            print("%s did not take damage." % self.name)
        if self.health <= 0:
            print("%s is dead." % self.name) 

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 5
        self.power = 2
        self.bounty = 1000

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))

    def alive(self):
        return True  

class Barbarian(Character):
    def __init__(self):
        self.name = 'conan'
        self.health = 10
        self.power = 7
        self.bounty = 10

class Vulture(Character):
    def __init__(self):
        self.name = 'bob the vulture'
        self.health = 2
        self.power = 1
        self.bounty = 0

    def receive_damage(self, points):
        r4= random.randint(1, 3)
        if r4 == 1:
            self.health -= points
            print("%s received %d damage." % (self.name, points))
        else:
            print("%s evaded the attack." % self.name)
        if self.health <= 0:
            print("%s is dead." % self.name) 

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.alive():
            hero.collect_bounty(enemy)
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, hero):
        hero.health += 2
        print("%s's health increased to %d." % (hero.name, hero.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class SuperTonic(object):
    cost = 10
    name = 'supertonic'
    def apply(self, hero);
        hero.health = 10
        print("%s's health has been restored!" % hero.name)

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self,hero):
        hero.armor = 2
        print("%s's armor is now %d" % (hero.name, hero.armor))

class Evade(object):
    cost = 10
    name = 'evade'
    def apply(self, hero)
        hero.evade += 2
        print("%s's evade points increased to %d." % (hero.name, hero.evade))
    

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword, SuperTonic, Armor, Evade]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Vulture(), Goblin(), Wizard(), Medic(), Shadow(), Barbarian(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
