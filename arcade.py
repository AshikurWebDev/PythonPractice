import sys
from rps import rps
from guess_number import gs

def run_arcade(name='PlayerOne'):
    playerChoice = input(f"\n{name}, welcome to Arcade! \nPlease choose a game: \n1 = Rock Paper Scissor\n2 = Guess My Number \nOr press 'x' to exit the Arcade\nEnter your coice: ")
    if playerChoice not in ['1', '2', 'x']:
        print(f"{name}, please Enter 1,2 or 'x'.")
        return run_arcade()
    
    def game_selector(player):
        if player == '1':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player == '2':
            guess_number = gs(name)
            guess_number()
        else :
            sys.exit()
    chosed_game = game_selector(playerChoice)
    print(chosed_game)
    
    while True:
        print(f"{name}, welcome back to the Arcade menu.")
        return run_arcade()

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
    run_arcade = run_arcade(args.name)
    run_arcade()