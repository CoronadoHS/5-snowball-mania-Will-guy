import random
''' 
    Name: Snowball-Mania
    Author: Will W 
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

players = []

def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?\n>")
    players.append(createPlayer(name))
    opponent = input(f"Welcome {name}! Who would you like to play against?\n>")
    players.append(createPlayer(opponent))
    for p in players:
        print(p)
    print(name + " v.s. " + opponent)
    thrower = random.choice(players)
    print(thrower.name)
    target = random.choice(players)
    while (target == thrower):
        target = random.choice(players)
    print(target.name)
    while(target.health > 0 and thrower.health > 0):
        currGame = hitResult(thrower, target)
        if(currGame == True):
            print(f"{thrower.name} hit {target.name}! {target.name} has {target.health}/100 HP left.")
        else:
            print(f"{thrower.name} missed!")
        coinFlip(thrower, target)
        

def coinFlip(thrower, target):
    if(random.random(1, 0) <= .50):
        print(f"{target.name}'s turn!")
        temp = target
        target = thrower
        thrower = temp
        return target, thrower
    else:
        print(f"{thrower.name}'s turn again!")

class Player:
    def __init__(Name):
        name = Name
        health = 100
        power = random.randint(10, 25)
        dodgeAbility = 0
        if(power > 17):
            dodgeAbility = float(random.randint(45, 60))/100
        else:
            dodgeAbility = float(random.randint(60, 75))/100

        return [name, health, power, dodgeAbility]
    

def hitResult(thrower, target):
    if(target.dodgeAbility <= random.random(0, 1)):
        target.health - thrower.power
        return True
    else:
        return False
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss

main()
