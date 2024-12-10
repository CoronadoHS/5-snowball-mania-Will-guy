import random
import time
import colorama
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
        self.hitsLanded = 0
        self.shotsFired = 0
        if(self.power > 17):
            self.dodgeAbility = float(random.randint(20, 35))/100
            self.critChance = float(random.randint(5, 15))/100
        else:
            self.dodgeAbility = float(random.randint(35, 50))/100
            self.critChance = float(random.randint(10, 20))/100
    def __str__(self):
        return f"STATS = HP : {self.health} - Power : {self.power} - Landed : {self.hitsLanded}"

players = []
KOd = []
def main():
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
        time.sleep(.1)
    p_dict = dict()
    for p in players:
        p_dict.update({p.name.lower() : p})
    gameplay(name, players, input("Would you like to play on auto or manual?\n>"))
    

def gameplay (name, players, manual):
    if(manual.lower().startswith("a") == True):

        print("***AUTOMATIC MODE SELECTED***")
        thrower = random.choice(players)
        target = random.choice(players)
        while(len(players) > 1):
            while (target == thrower):
                target = random.choice(players)
            time.sleep(1.25)
            hitResult(thrower, target, players)
            thrower = random.choice(players)
            target = random.choice(players)
    else:

        print("***MANUAL MODE SELECTED***")
        thrower = random.choice(players)
        target = random.choice(players)
        while(len(players) > 1):
            while (target == thrower):
                target = random.choice(players)
            if(thrower.name == name):
                target = main.p_dict[input("Who would you like to target?\n>").lower()]
            time.sleep(1.25)
            hitResult(thrower, target, players)
            thrower = random.choice(players)
            target = random.choice(players)
        endgame()
            
# could be used for a duel mode, but not super applicable right now.
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

def hitResult(thrower, target, players):
    crit = 1
    print(f"{thrower.name} is THROWING at {target.name}!")
    if(thrower.critChance <= random.random()):
            time.sleep(2)
            crit = 2
            print(f"{thrower.name} has a chance to deal DOUBLE DAMAGE!")
    if(target.dodgeAbility < random.random()):
            thrower.hitsLanded += 1
            thrower.shotsFired += 1
            target.health -= crit*(thrower.power)
            time.sleep(1.5)
            print(f"{thrower.name} HIT {target.name}!")
            displayHealth(players)
            if(checkKO(target)):
                if(crit > 1):
                    time.sleep(1)
                    print(f"{thrower.name} KNOCKED OUT {target.name} with a CRITICAL HIT!")
                    KOd.append(target)
                    players.pop(players.index(target))
                else:
                    time.sleep(1)
                    print(f"{thrower.name} KNOCKED OUT {target.name}!")
                    players.pop(players.index(target))
    else:
        time.sleep(2)
        thrower.shotsFired += 1
        print(f"{target.name} DODGED {thrower.name}'s snowball!")

def checkKO(target):
    '''Checks if health is 0 or less. If it is then it is a KO and returns True.'''
    if(target.health <= 0):
        return True
    return False

def displayHealth(players):
    time.sleep(2)
    print("\n***HEALTHBOARD***\n")
    time.sleep(1)
    display = ""
    longest = findLongestName(players)
    for p in players:
        display += makeSameLength(longest, p.name) + "...HEALTH "
        x = p.health
        while(x > 0):
            if(x <= 33):
                display += "|"
            elif(x <= 66):
                display += "|"
            else:
                display += (Style.BRIGHT"|")

            x-=1
        display += "\n"
    print(display)
    time.sleep(2)
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss

def findLongestName(players):
    longest = 0
    for p in players:
        if(len(p.name) > longest):
            longest = len(p.name)
    return longest

def makeSameLength(stanLen, strAdjust):
    while(stanLen > len(strAdjust)):
        strAdjust += "."
    return strAdjust

def endgame():
    time.sleep(3)
    print(f"{players[0].name} WINS")
    print(f"#1 - {players[0].name} {players[0]} - Accuracy : {int((players[0].hitsLanded/players[0].shotsFired)*100)}%")
    KOd.reverse()
    place = 2
    for p in KOd:
        time.sleep(3)
        print(f"#{place} - {p.name} {p} - Accuracy : {int((p.hitsLanded/p.shotsFired)*100)}%")
        place += 1
        
main()
