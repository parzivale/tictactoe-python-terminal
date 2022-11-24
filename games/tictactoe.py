import games_handeler

class ticTacToe(games_handeler.game):

    def __init__(this):
        super().__init__(3)


    def wincons(this):
        """Generates a list of all possible winconditions which CHECKWINNER can reference"""
        diagonals = [
            [this.grid[i][i] for i in range(0,3)],
            [this.grid[2-i][i] for i in range(0,3)]
        ]

        return diagonals + this.getRows() + this.getColumns()
    
    
    def checkWinner(this):
        """checks whether a wincondition has been met based off of the WINCONS list"""
        for i in this.wincons():
            if(" " not in i):
                i = set(i)
                if(len(i) == 1):
                    return True
    
def main():
    game = ticTacToe()

    print("""
    --------------------------------------------------------------------
                        tic tac toe(so fun)
    --------------------------------------------------------------------                                
    """)
    print("hi and welcome to this terminal tictactoe game!")
    while not game.won:
        print("this is what the board looks like!")
        print(game.boardString(top = True, side = True))
        print(f"player {game.turn+1} your turn!\n")
        y,x = game.checkInput(regex="^[a-c][ ][1-3]$")
        character = "X" if(game.turn) else "O"
        game.grid[y][x] = character
        game.won = game.checkWinner() if game.checkWinner() else game.won
        game.turn = not game.turn
        if(game.checkIfTie()):
            break
    print(game.boardString(top = True, side = True))
    if(game.checkIfTie()):
        print("its a tie!")
    else:
        print(f"well done player {int(not(game.turn))+1} you won")