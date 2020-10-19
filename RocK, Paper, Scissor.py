# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

from random import randint
# create a list of play options
t = ["Rock", "Paper", "Scissor"]

#Assign a random paly to computer
computer = t[randint(0, 2)]

# set player to false
player = False

while player == False:
# set player to true
    player = input("Rock, Paper, Scissor? ")
    if player == computer:
        print(" It is a Tie! ")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose! ", computer, "Covers ", player)
        else:
            print(" you Win! ", player, "smashes ", computer )
    elif player == "Paper":
        if computer == "Scissor":
            print(" you Lose! ", computer, "cuts ", player)
        else:
            print(" you Win! ", player, "covers ", computer)
    elif player == "Scissor":
        if computer == "Rock":
            print(" you Lose! ", computer, "smashes ", player)
        else:
            print(" you Win! ", player, "cuts ", computer)
    else:
        print(" Wrong Input! ")
# player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]













