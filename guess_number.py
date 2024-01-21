import sys
import random

def gs(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_rsp():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess which number I'm thinking of ... 1,2, or 3 \n\n")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please, enter... 1,2, or 3.")
            return play_rsp()
        player = int(playerchoice)
        if player < 1 or player > 3 :
            sys.exit()

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}")
        print(f"Computer chose {computer}\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if computer == player:
                player_wins +=1
                return f"{name}, you win!"
            else:
                return f"Sorry, {name}. Beter luck next time"

        game_result = decide_winner(player, computer)

        print(game_result)
            
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: { game_count}")
        print(f"\n{name} wins : { player_wins}")
        percentage = 0
        if(player_wins != 0):
            percentage = format((player_wins/game_count)*100, ".2f")
            print(f"\nYour winning percentage: {percentage}%")
        elif percentage != 0:
            print(f"\nYour winning percentage: {percentage}%")
        else:
            print("\nYour winning percentage: 00.00%")
        
        print(f"\nPlay again, {name}?")
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
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👏")
            else:
                return
    return play_rsp


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experiences."
    )

    parser.add_argument(
        "-n", "--name", metavar= "name", 
        required=True, help = "The name of the person playing the game."
    )


    args = parser.parse_args()
    guess_number = gs(args.name)
    guess_number()