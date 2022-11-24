import games_handeler



class connect4(games_handeler.game):
    
    def __init__(this):
        this.size = 25
        super().__init__(this.size)

    def wincons(this):
        """Generates a list of all possible winconditions which CHECKWINNER can reference"""
        for i in range(this.size):
            for n in range(i):
                pass

        for i in range(this.size,0,-1):
            for n in range(i):
                pass
        diagonals = [[this.grid[i-n-1][n] for n in range(0,i)] for i in range(0,this.size)] + [[[this.grid[i+n+1][n] for n in range(i,0,-1)] for i in range(this.size,0,-1)]]
        print(diagonals)

    def movetobottom(this,input,character):
        for n,i in enumerate(this.getColumns()[input]):
            if not i == " ":
                print(n,input)
                this.grid[n-1][input] = character
                return None
            
        this.grid[len(this.getColumns()[input])-1][input] = character

                
    def checkWinner(this):
        # for i in this.wincons():
            # for n in i:
                # for index,e in enumerate(n):
                    # if(e in ("O", "X")):
                        # for o in range(3):
                            # if(not n[index + o] == e):
                                # return False
        # return True

        pass                  
                                

def main():
    game = connect4()

    print("""
    --------------------------------------------------------------------
                        connect4(so fun)
    --------------------------------------------------------------------                                
    """)
    print("hi and welcome to this terminal connect4 game!")
    while not game.won:
        print("this is what the board looks like!")
        print(game.grid)
        print(game.boardString())
        print(f"player {game.turn+1} your turn!\n")
        x = game.checkInput(regex=f"^[a-{chr(game.size+96)}]$")[1]
        character = "X" if(game.turn) else "O"
        game.movetobottom(x,character)
        game.won = game.checkWinner() if game.checkWinner() else game.won
        game.turn = not game.turn
        if(game.checkIfTie()):
            break
    
    print(game.boardString())
    if(game.checkIfTie()):
        print("its a tie!")
    else:
        print(f"well done player {int(not(game.turn))+1} you won")