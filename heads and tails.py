import random

print("Let's Toss!!!")

while True :
    choices = ["heads","tails"]

    computer = random.choice(choices)
    player = None


    while player not in choices:
        player=input("Heads or Tails : ").lower()
    if player==computer:
        print("player : ",player)
        print("computer : ",computer)
        print("You win")
    else:
        print("player : ",player)
        print("computer : ",computer)
        print("You lose!!")
    
    play_again = input("play again ? (yes/no): ").lower()
    if play_again != "yes" :
        break

print("bye !")