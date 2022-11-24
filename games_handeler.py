import re

class input_handler:
    def __init__(this):
        this.input = None

    def ask(this,message = None, regex = None, errorMessage = None):
        """checks if the input matches a given regex scheme, if not will query the user till it passes"""
        if message == None:
            message = ""
        this.input = input(message)
        this.checkIfValidInput(regex, errorMessage)

    def checkIfValidInput(this, regex = None, errorMessage = None):
        """checks if the input given by INPUTHANDLER.ask() matches a given regex scheme, if not will query the user till it passes"""
       
        if(errorMessage == None):
            errorMessage = "oops i think you inputed sometihng wrong try again\n"
        
        while(not re.search(regex, this.input.lower())):
            this.input = input(errorMessage) 

class game(input_handler):
    def __init__(this,size):
        super().__init__()
        this.turn = 0
        this.won = False
        this.grid = this.generateGrid(size)
        this.size = size
    
    def getColumns(this):
        """converts the grid matrix so that the sub lists are stored together and can be easily checked for copies"""
        return [[this.grid[i][n] for i in range(len(this.grid[n]))] for n in range(len(this.grid))]

    def getRows(this):
        """Returns the grid matrix using the same naming sceme as GETCOLUMNS for asthetic purposes"""
        return this.grid
        
    def checkIfTie(this):
        """checks for a tie by checking every cell in the grid for an empty cell"""
        for i in this.grid:
            if(" "in i):
                    return False
        return True
     
       
    def checkInput(this,regex):
        """checks if the input is valid for the given grid"""
        this.ask(regex=regex)
        inputCoords = this.inputToCoordinate(this.input)

        
        this.checkIfCellEmpty(inputCoords)

        while not this.checkIfCellEmpty(inputCoords):
            this.ask("nice try but you take cant use that square try again\n",regex=regex)
            inputCoords = this.inputToCoordinate(this.input)
        return inputCoords

    def checkIfCellEmpty(this,Coords):
        """checks if the cell is empty"""
        y,x = Coords
        return True if this.grid[y][x] == " " else False   

    def generateGrid(this, size):
        return [[" " for i in range(size)] for i in range(size)]


    def inputToCoordinate(this,playerInput):
        """converts the user input into a list of indexes for accsessing the grid"""
        if(len(playerInput) > 1):    
            splitplayerinput = playerInput.lower().split(" ")
        else:
            splitplayerinput = [playerInput,"1"]

        return[int(splitplayerinput[1])-1,int(ord(splitplayerinput[0]))-97]
        
    def boardString(this,top=None,side=None):
        """generates a 2by2 grid to be displayed    """
        if(top == None):
            top = True
        if(side == None):
            side = False
        
        # variable setup and top character generation
        boardstring = ""
        letters = "abcdefghijklmnopqrstuvwxyz"
        if(top):
            for i in range(this.size):
                    boardstring = f"{boardstring}     {letters[i]}"
            
            boardstring = boardstring + "\n"
            
        # first row of bars 
        if(side):
            boardstring = f"{boardstring} "
        else:
            boardstring = f"{boardstring}   "
        for i in range(this.size-1):
            if(side and i == 0):
                boardstring = f"{boardstring}       |"
            else:
                boardstring = f"{boardstring}     |"

        boardstring = f"{boardstring}\n"

        # main loop for the grid
        for integer in range(this.size):
            # loop for inserting the grid values into the string as well as bar seperators
            if(not side):
                boardstring = f"{boardstring}   "
            for n in range(this.size):
                if(n + 1 == this.size):
                    boardstring = f"{boardstring}  {this.grid[integer][n]}"
                elif(side and n == 0):
                    boardstring =f"{boardstring}{str(integer+1) + ' '}   {this.grid[integer][n]}  |"
                else:
                    boardstring = f"{boardstring}  {this.grid[integer][n]}  |"

            boardstring = f"{boardstring}\n"
            # this is the seperator at the bottom of each row the lodashes and the bars, but on the last iteration it needs to be invisible as the grid ends without a line of lobars
            if(not integer+1 == this.size):
                boardstring = f"{boardstring}   "
            for i in range(this.size):
                if(not integer+1 == this.size):
                    if(i + 1 == this.size):
                        boardstring = f"{boardstring}_____"
                    else:
                        boardstring = f"{boardstring}_____|"


            if(not integer+1 == this.size):
                boardstring = f"{boardstring}\n" 
            # this is the line of bars the goes at the begining of each new cell line, but at the end we need to mess with the white sapce for some reason
            boardstring = f"{boardstring}   "
            for i in range(this.size-1):
                boardstring = f"{boardstring}     |"
    
            boardstring = f"{boardstring}\n"

            
        return(boardstring)