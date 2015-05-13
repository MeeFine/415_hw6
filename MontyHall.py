"""PartII.py
Ziming Guo, CSE 415, Spring 2015, University of Wahsington
Instructor:  S. Tanimoto
HW6 -- Monty Hall

This program will simulate the Monty Hall problem.
Generally, Monty Hall problem ask a player to choose
a door in three. One of the door hides a car and two
others hide goats. Player's goal is to get the car. The host
will open a goat's door after our first choice, then
player will be given chance to change his/her choice.
Surprisingly to most people, changing decision will increase
the chance to get the car.

My program is designed to test the case. My program
will be given the number of games to be played and game
strategy(stay / switch) and print each game it simulated
and formulate a report of statistics of games played.
"""

import sys
from random import randint, choice

if len(sys.argv) < 3:
    raise Exception("Insufficient arguments") # Exit the program if arguments are insufficient
else:
    try:
        NGAMES = int(sys.argv[1])
    except:
        raise Exception("Illegal argument") # Handle the illegal argument
    if sys.argv[2].lower() == "stay":
        STAY = True
    elif sys.argv[2].lower() == "switch":
        STAY = False
    else:
        raise Exception("Illegal argument") # Handle the illegal argument

WON = 0 # Keep track of games won in all time


# The function to simulate the games
def game_start():
    global WON
    for i in range(NGAMES):
        result = ""
        doors = []  # List that simulate the doors
        car = randint(0, 2)
        # Adding car/goats randomly to list
        for j in range(3):
            if j == car:
                doors.append('c')
            else:
                doors.append('g')
        result += str(doors) + ", "
        choose = randint(0, 2)
        doors[choose] = ">" + doors[choose] # Choose a door randomly
        result += str(doors) + ", "
        goats = []
        for j in range(len(doors)):
            if doors[j] == "g":
                goats.append(j)
        host = choice(goats)
        doors[host] = "G"  # Open a door of goat
        result += str(doors) + ", "
        # Handle the case of stay
        if STAY:
            doors[choose] = doors[choose].upper()
            if doors[choose] == ">C":
                WON += 1
        # Handle the case of switch
        else:
            for j in range(len(doors)):
                if j != host and j != choose:
                    doors[j] = ">" + doors[j].upper()
                    if doors[j] == ">C":
                        WON += 1
                elif j == choose:
                    doors[j] = doors[j][1:]
        result += str(doors)
        print(result)
    report()


# Function to make report given the data of won games and total games
def report():
    global WON
    global NGAMES
    global STAY
    f = lambda s: "STAY" if s else "SWITCH"
    print()
    print("Number of games played: " + str(NGAMES))
    print("Player policy: " + f(STAY))
    print("Number of games won (cars revealed): " + str(WON))
    print("Number of games lost: " + str(NGAMES - WON))
    print("Percentage of games won: " + str(WON / NGAMES))
    print("Percentage of games lost: " + str((NGAMES - WON) / NGAMES))


if __name__ == '__main__':
    game_start()