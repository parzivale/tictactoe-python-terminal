from games import *
import games
import games_handeler

def main():
    print("Hi and welcome to zeus's terminal games which game would you like to play?")
    for n,i in enumerate(games.__all__):
        print(f"{n+1}. {i}")
    print("Type the number of the game you want to play!")
    
    userinput = games_handeler.input_handler()
    userinput.ask(regex = f"^[1-{len(games.__all__)}]$")

    getattr(games,games.__all__[int(userinput.input)-1]).main()

    while(input(f"press enter to continue, press any other key to stop\n") == ""):
        main()

if __name__ == "__main__":
    main()
        