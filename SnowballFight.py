import random
import time
''' 
    Name: Snowball-Mania
    Author: Will W 
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = random.randint(10, 25)
        self.dodgeAbility = 0
        if(self.power > 17):
            self.dodgeAbility = float(random.randint(45, 60))/100
        else:

            self.dodgeAbility = float(random.randint(60, 75))/100
    def __str__(self):
        return f"{self.name}: HP {self.health}, Power {self.power}, Agility {self.dodgeAbility}"

def main():
    players = []
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?\n>")
    players.append(Player(name))
    opponent = input(f"Welcome {name}! Who would you like to play against?\n>")
    players.append(Player(opponent))

    add = input("Any more opponents? (Press 'ENTER' to finish)\n>")
    while(add != ""):
        players.append(Player(add))
        add = input("Any more opponents? (Press 'ENTER' to finish)\n>")
        
    for p in players:
        print(p)

    gameplay(name, players, input("Would you like to play on auto or manual?\n>"))
        


    

def gameplay (name, players, manual):
    if(manual.lower().startswith("a") == True):
        while(len(players) > 1):
            thrower = random.choice(players)
            target = random.choice(players)
            while (target == thrower):
                target = random.choice(players)
            print(f"{thrower} is THROWING at {target}!")
            
            if(hitResult(thrower, target) == True):
                print(f"{thrower.name} HIT {target.name}! {target.name} has {target.health}/100 HP left.")
            else:
                print(f"{thrower.name} missed!")
            coinFlip(thrower, target)
    else:
        while(len(players) > 1):
            thrower = random.choice(players)
            target = players.index()
            while (target == thrower):
                target = random.choice(players)
            print(f"{thrower} is THROWING at {target}!")
            if(hitResult(thrower, target) == True):
                print(f"{thrower.name} HIT {target.name}! {target.name} has {target.health}/100 HP left.")
            else:
                print(f"{thrower.name} missed!")
            coinFlip(thrower, target)
        
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
    if(target.dodgeAbility <= random.random()):
        target.health -= thrower.power
        return True
    else:
        return False
    

def displayHealth():
    display = ""
    for p in players:
        display += f"{p.name} HEALTH:" 
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss

main()
