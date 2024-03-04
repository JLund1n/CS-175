#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Prompts user for an action
    Inputs: N/A
    Returns: (useraction), action to enter URL, go backwards or forward, and quit the program
    '''
    while True: #Loop to ask for valid user input
        useraction = input('Enter = to enter a URL, < to go back, > to go forward, q to quit') #Asks the user for 1 of 4 prompts
        if useraction in ['=','<','>','q']: #Checks to see if the user gave a valid input
            return useraction #If so return the input
        else:
            raise Exception('Invalid entry, please reinput') #Otherwise raise an exception

def goToNewSite(current, bck, fwd):
    '''
    Prompts user for a new webaddress
    Inputs: (current), current webaddress (bck), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), new webaddress to be added to the stack
    '''   
    newsite = input('URL: ') #Prompt for a new webaddress
    bck.push(current) #Pushes the current address to the back stack
    fwd.clear() #Clears the forward stack
    return newsite #Returns the new webaddress
    
def goBack(current, bck, fwd):
    '''
    Go back to the previous webaddress
    Inputs: (current), current webaddress (bck), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), updated newsite of the previous webaddress or (current), current webaddress
    '''    
    try:
        newsite = bck.pop() #Pops the webaddress from the back stack
        fwd.push(current) #Pushes the current address to the forward stack
        return newsite #Returns the new webaddress
    except Exception: #Exception if an error occurs
        print('Unable to move backwards') #Tell the user they cannot move backwards
        return current #Returns the current address

def goForward(current, bck, fwd):
    '''
    Go forward to the next webaddress
    Inputs: (current), current webaddress (bck), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), updated newsite of the next webaddress or (current), current webaddress
    '''    
    try:
        newsite = fwd.pop() #Pops the webaddress from the forward stack
        bck.push(current) #Pushes the current address to the back stack
        return newsite #Returns the new webaddress
    except Exception: #Exception if an error occurs
        print('Unable to move forwards') #Tell the user they cannot move forwards
        return current #Returns the current address



def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit: #While the user does not want to quit
        print('\nCurrently viewing', current)
        try:
            action = getAction() #Get an action from the user
        except Exception as action_Exception: #Exception for error handling
            print(action_Exception.args[0]) #Prints the error handled in the functions

        else: #If the user input a valid entry
            if action == '=': 
                current = goToNewSite(current, back, forward)
            elif action == "<":
                current = goBack(current, back, forward)
            elif action == ">":
                current = goForward(current, back, forward)
            else:
                quit = True

    print('Browser closing...goodbye.')   

        
if __name__ == "__main__":
    main()
    