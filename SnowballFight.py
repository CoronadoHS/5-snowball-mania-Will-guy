import random
import time
''' 
    Name: Snowball-Mania
    Author: Will W 
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''
# switched to comp. 25
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = random.randint(10, 25)
        self.dodgeAbility = 0
        self.critChance = 0
        if(self.power > 17):
            self.dodgeAbility = float(random.randint(45, 60))/100
            self.critChance = float(random.randint(5, 20))/100
        else:

            self.dodgeAbility = float(random.randint(60, 75))/100
            self.critChance = float(random.randint(10, 25))/100
    def __str__(self):
        return f"{self.name} Stats: HP {self.health}, Power {self.power}, Agility {self.dodgeAbility}, Crit Chance {self.critChance}"

def main():
    players = []
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    time.sleep(3)

    name = input("What is your name?\n>")
    players.append(Player(name))
    time.sleep(.5)

    opponent = input(f"Welcome {name}! Who would you like to play against?\n>")
    players.append(Player(opponent))
    time.sleep(.5)

    add = input("Any more opponents? (Press 'ENTER' or type Done if finished)\n>")
    while(add != "" or add.lower() == "done"):
        players.append(Player(add))
        add = input("Any more opponents? (Press 'ENTER' to finish)\n>")
        time.sleep(.5)
        
    for p in players:
        print(p)
        time.sleep(1)

    gameplay(name, players, input("Would you like to play on auto or manual?\n>"))
    

def gameplay (name, players, manual):
    if(manual.lower().startswith("a") == True):

        print("auto mode")
        thrower = random.choice(players)
        target = random.choice(players)
        while(len(players) > 1):
            while (target == thrower):
                target = random.choice(players)
            print(f"{thrower.name} is THROWING at {target.name}!")
            
            if(hitResult(thrower, target) == True):
                print(f"{thrower.name} HIT {target.name}! {target.name} has {target.health}/100 HP left.")
            else:
                print(f"{thrower.name} missed!")
    else:
        p_dict = dict()
        for p in players:
            p_dict.update({p.name.lower() : p})
        print(p_dict.keys(), p_dict.values())

        print("manual mode")
        thrower = random.choice(players)
        target = random.choice(players)
        while(len(players) > 1):
            while (target == thrower):
                target = random.choice(players)
            if(thrower.name == name):
                target = p_dict[input("Who would you like to target?\n>").lower()]
            print(f"{thrower.name} is THROWING at {target.name}!")
            hitResult(thrower, target)
            displayHealth(players)
            thrower = random.choice(players)
            target = random.choice(players)
            
        
def coinFlip(thrower, target):
    if(random.random() <= .50):
        temp = target
        target = thrower
        thrower = temp
        time.sleep(1)
        print(f"{target.name}'s turn!")
        return target, thrower
    else:
        time.sleep(.5)
        print(f"{thrower.name}'s turn again!")

def hitResult(thrower, target):
    crit = 1
    if(thrower.critChance <= random.random()):
            time.sleep(2)
            print(f"{thrower.name} has a chance to deal DOUBLE DAMAGE!")
    if(target.dodgeAbility < random.random()):
            target.health -= crit*(thrower.power)
            time.sleep(1.5)
            print(f"{thrower.name} HIT {target.name}!")
            if(checkKO(target)):
                if(crit > 1):
                    time.sleep(1)
                    print(f"{thrower.name} KNOCKED OUT {target.name} with a CRITICAL HIT!")
                else:
                    time.sleep(1)
                    print(f"{thrower.name} KNOCKED OUT {target.name}!")
    else:
        time.sleep(2)
        print(f"{thrower.name} missed!")

def checkKO(target):
    '''Checks if health is 0 or less. If it is then it is a KO and returns True.'''
    if(target.health <= 0):
        return True
    return False

def displayHealth(players):
    display = ""
    for p in players:
        display += f"{p.name} HEALTH:" 
        x = p.health
        while(x > 0):
            display += "|"
            x-=1
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss

main()
