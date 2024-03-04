#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        Display = [] #Empty array of board rows and columns to be populated
        for row in self.board: #Loop through each row in the board element which is populated from the __init__ function
            for val in row: #Loop through each value in the row or in otherwords the columns value
                if val == 0: #Check to see if the square should be empty and if so append a blank space
                    Display.append(' ')
                else: #Otherwise append the number that is being inputed
                    Display.append(str(val))
        
        print('  0  1  2') #Print the column values
        print(' 0 '+ Display[0] + ' | ' + Display[1] + ' | ' + Display[2] + ' ') #Print the row alongside the box values
        print('   -----------') #Print the dividers in the x-axis
        print(' 1 '+ Display[3] + ' | ' + Display[4] + ' | ' + Display[5] + ' ') 
        print('   -----------')
        print(' 2 '+ Display[6] + ' | ' + Display[7] + ' | ' + Display[8] + ' ')
        print('   -----------')



        
        


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        try: #Try method
            if self.board[row][col] == 0: #Checks to see if the square value is empyt
                return True #If the square is empty return true
            else: #Otherwise if the square has a value in it
                return False #Return false
        except IndexError: #If there is an error with the inputting of values
            return False #Return false
    
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col): #Checks to see if the square is empty by calling the squareIsEmpty method
            self.board[row][col] = num #Sets the square value to the number to be updated
            return True #Returns true if the update worked
        else: #Otherwise if the update did not go through
            return False #Return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        BoardIsFull = True #Initialize the board as always full
        for row in self.board: #Loop through the rows of the board
            for val in row: #Loop through the vals of the rows or in other words the columns
                if val == 0: #If a square is empty
                    BoardIsFull = False #The board is not full, so False
        return BoardIsFull #Returns the boardIsFull boolean
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        x = [] #Test value 1
        y = [] #Test value 2
        z = [] #Test value 3
        
        for row in self.board: #Loops through the rows in the board
            if sum(row) == 15: #First checks to see if the sum of a horizontal line is 15
                if not 0 in row: #Then checks if there isn't a zero in the row
                    return True #If both conditions pass the person is a winner and return true
            x.append(row[0]) #Append the first row
            y.append(row[1]) #Append the second row
            z.append(row[2]) #Append the third row

        TestVar = [x, y ,z] #List of the appended test value
        for row in TestVar: #Loop throw the rows in the test value list
            if sum(row) == 15: #Checks to see if the sum is 15 in a vertical line
                if not 0 in row: #Ensures no value or square is empty
                    return True #Return true if both cases are true
        if (self.board[0][0] + self.board[1][1] + self.board [2][2] == 15 #Checks to see if the sum of the vals is 15 in both diagonals and none of the values are empty
        and (not self.board[0][0] == 0 and not self.board[1][1] == 0 and not self.board[2][2] == 0)) or (self.board[0][2] + self.board[1][1] + self.board [2][0] == 15 
        and (not self.board[0][2] == 0 and not self.board[1][1] == 0 and not self.board[2][0] == 0)):
            return True #If the cases pass return True
        else: #Otherwise if they fail
            return False #Return False
     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe() #Intialize the board as the class
    print('Contents of board attribute when object first created:')
    print(myBoard.board) #Print and empty board
    
    # does the empty board display properly?
    myBoard.drawBoard() #Draw the board by calling the drawBoard function

    # assign a number to an empty square and display
    myBoard.update(1, 0,7) #Update the second row and first column with the number 7
    myBoard.drawBoard() #Draws the new board

    # try to assign a number to a non-empty square. What happens?
    myBoard.update(1, 0 ,2)
    myBoard.drawBoard() #Tries to draw the board with an overlapping update
    print("Not an empty square thus no update")
    
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print(myBoard.isWinner(), "| True if a valid winner and false otherwise") #Checks to see if the board is a winner with the isWinner() function
    
    # check if the board is full. Should it be full after only 1 entry?
    print(myBoard.boardFull(),"| True if all squares are full and false otherwise") #Checks to see if the board is full by calling the boardFull() function
    
    # add values to the board so that any line adds up to 15. Display
    myBoard.update(0, 0, 1) #Updates the first row and column with 0
    myBoard.update(2, 0, 7) #Updates the third row and first column with 7
    myBoard.drawBoard() #Draws the updated board
    
    # check if the board has a winner
    print(myBoard.isWinner(),"| True if a winning condition is met and false otherwise") #Checks to see if someone has won
    
    # check if the board is full
    print(myBoard.boardFull(),"| True if the board is full and false otherwise") #Checks to see if the board is full
    
    # write additional tests, as needed
    print('Test for a diagonal winning condition')
    for x in range(len(myBoard.board)): #Loops throw the rows
        for y in range(len(myBoard.board[x])): #Loops through the columns
            if x == y: #If the row and column value are equal
                myBoard.board[x][y] = 3 #Update to the space to be 3
            else: #Otherwise if the condition is not met
                myBoard.board[x][y] = 2 #Update the other spaces with 2
    myBoard.drawBoard() #Draw the updated board
    print(myBoard.isWinner(), "| True if a winner and false otherwise")
    print(myBoard.boardFull(), "| True if the board is full and false otherwise")

    