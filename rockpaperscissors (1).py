#Eva Deng
#P1. 01/06/25

#init
import random
wins = 0
losses = 0
ties = 0
print("Welcome to Rock, Paper, Scissors!")
#functions
def display():
    print(f"wins: {wins}")
    print(f"losses: {losses}")
    print(f"ties: {ties}")

def rps():
    global wins
    global losses
    global ties
while True: #infinite loop
    #Player making selection
    print("Please select either rock, paper, or scissors: ")
    player = input("Selection: ")
    #Computer making selection
    computer = random.randint(1,3)
    print(computer)
    if computer == 1:
        computer = "rock"
        print("Computer selected Rock")
    elif computer == 2:
        computer = "paper"
        print("Computer selected Paper")
    else:
        computer = "scissors"
        print("Computer selected Scissors")

    #== is equal to
    #= gets the value of
    #the outcome
    if player == "rock" and computer == "scissors":
        print("Congrats you win this round!")
        wins = wins + 1
    elif player == "rock" and computer == "paper":
        print("You lose this round!")
        losses = losses + 1
    elif player == "rock" and computer == "rock":
        print("You are tied this round")
        ties = ties + 1

    if player == "scissors" and computer == "paper":
        print("Congrats you win this round!")
        wins = wins + 1
    if player == "scissors" and computer == "rock":
        print("You lose this round!")
        losses = losses + 1
    if player == "scissors" and computer == "scissors":
        print("You are tied this round")
        ties = ties + 1

    if player == "paper" and computer == "rock":
        print("Congrats you win this round!")
        wins = wins + 1
    if player == "paper" and computer == "scissors":
        print("You lose this round!")
        losses = losses + 1
    if player == "paper" and computer == "paper":
        print("You are tied this round")
        ties = ties + 1
    display()
    #Play again?
    again = input("Would you like to play again?: ") #string
    if again == "yes":
        print("restarting")
    if again == "no":
        print("Thanks for playing!")
        break



#main
rps()

