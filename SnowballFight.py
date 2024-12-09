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
    time.sleep(1)
    opponent = input(f"Welcome {name}! Who would you like to play against?\n>")
    players.append(Player(opponent))
    time.sleep(1)
    add = input("Any more opponents? (Press 'ENTER' to finish)\n>")
    while(add != ""):
        time.sleep(.5)
        players.append(Player(add))
        add = input("Any more opponents? (Press 'ENTER' to finish)\n>")
    
    gameplay(name, players, input("Would you like to play on auto or manual?\n>"))
        


    

def gameplay (name, players, manual):
    if(manual.lower().startswith("a") == True):
        # automatic mode
        while(len(players) > 1):
            thrower = random.choice(players)
            target = random.choice(players)
            if(target == thrower):
                while(target == thrower):
                    target = random.choice(players)
            print(f"{thrower.name} is THROWING at {target.name}!")
            time.sleep(1.75)
            if(hitResult(thrower, target) == True):
                print(f"{thrower.name} HIT {target.name}!")
                if(target.health <= 0):
                    print(f"{target.name} is OUT!!!")
                    players.pop(players.index(target))

            else:
                print(f"{thrower.name} missed!")
            displayHealth(players)
            # coinFlip(thrower, target)
    else:
        while(len(players) > 1):
            # manual mode
            thrower = random.choice(players)
            if(thrower.name == name):
                print("Your turn to throw!")
                time.sleep(.5)
                target = input("Who would you like to target?\n>")
            else:
                target = random.choice(players)

            while(target == thrower):
                target = random.choice(players)
            time.sleep(1.75)
            if(thrower.name == name):
                print(f"You are throwing at {target.name}!")
            else:
                print(f"{thrower.name} is throwing at {target.name}!")
            
            if(hitResult(thrower, target) == True):
                if(thrower.name == name):
                    print(f"You HIT {target.name}!")
                else:
                    print(f"{thrower.name} HIT {target.name}!")
                time.sleep(1)
                if(target.health <= 0):
                    print(f"{target.name} is OUT!!!")
                    players.pop(players.index(target))

            else:
                print(f"{thrower.name} missed!")
            displayHealth(players)
            # coinFlip(thrower, target)
        
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
    

def displayHealth(players):
    display = ""
    for p in players:
        display += f"{p.name} HEALTH:" 
        x = p.health
        while(x > 0):
            display += "|"
            x -= 1
        display += "\n"
    print(display)

    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss

main()
