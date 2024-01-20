import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rsp():
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        
        playerchoice = input("\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissor: \n\n")
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1,2, or 3.")
            return play_rsp()
        player = int(playerchoice)
        if player < 1 or player > 3 :
            sys.exit()

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS','').title()}")
        print(f"Python chose {str(RPS(computer)).replace('RPS','').title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins +=1 
                return "Your win!"
            elif player == 2 and computer == 1:
                player_wins +=1 
                return "You win!"
            elif player == 3 and computer == 2:
                player_wins +=1 
                return "You win!"
            elif player == computer:
                return "Tie game"
            else:
                python_wins
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)
            
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: { str(game_count)}")
        print(f"\nPlayer wins : { str(player_wins)}")
        print(f"\nPython wins : { str(python_wins)}")
        print("\nPlay again?")
        while True:
            playagain = input("\nPlay again? \nY for Yes \nN for Quit \n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rsp()
        else:
            print("🥳🥳")
            print("Thank you for playing! \n")
            sys.exit("Bye! 👋")
    return play_rsp

play = rps()
play()