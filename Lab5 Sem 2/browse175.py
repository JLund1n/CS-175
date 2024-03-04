import os
from time import sleep
import stack

#----------------------------------------------------
# Lab 5 Problem B: BROWSE-175
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

os.system("")  # enables ANSI characters in terminal

def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def display_error(error):
    '''
    Displays an error message under the current site as specificed by "error".
    Input:
        - error (str): error message to display
    Returns: N/A
    '''
    move_cursor(0, 3)
    print("\033[6;31;40m{:^80}\033[0m".format(error))
    sleep(0.6)
    clear_screen()

def print_header():
    '''
    Prints the BROWSE-175 header.
    Input: N/A
    Returns: N/A 
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[ BROWSE-175 ]"))

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def display_current_site(current):
    '''
    Displays the current site underneath the header.
    Input:
        - current (str): current site
    Returns: N/A
    '''
    print("\033[2;32;40m{:^80}\033[0m".format("Currently viewing: " + current))
    print("\033[4;30;40m{:^80}\033[0m".format(""))

def display_hint(message):
    '''
    Displays navigation hint message in the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def display_buttons(back, fwd):
    '''
    Displays the navigational buttons at the top of the terminal.
    "(<) BACK" and "FORWARD (>)" labels should only be displayed
    if there are sites to go back or forward to.
    Input: 
        - back: stack of previous sites
        - fwd: stack of forward sites
    Returns: N/A
    '''
    if not back.isEmpty() and fwd.isEmpty(): #If the back stack is not empty, but the forward stack is
        print('(<)BACK')
    if not back.isEmpty() and not fwd.isEmpty(): #If they are both not empty
        print(f"{'(<)BACK'}  {'FORWARD(>)':>71}")
    if back.isEmpty() and not fwd.isEmpty(): #If the back stack is empty, but the forward stack is not
        print(f"{'FORWARD(>)':>80}")

    

def goToNewSite(current, back, fwd):
    '''
    Prompts user for a new webaddress
    Inputs: (current), current webaddress (back), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), new webaddress to be added to the stack
    '''   
    newsite = input('URL: ') #Asks the user to input the new webaddress
    back.push(current) #Pushes the current address to the back stack
    fwd.clear() #Clears the forward stack
    return newsite #Returns the new webaddress
    
def goBack(current, back, fwd):
    '''
    Go back to the previous webaddress
    Inputs: (current), current webaddress (back), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), updated newsite of the previous webaddress or (current), current webaddress
    '''    
    try:
        newsite = back.pop() #Pops the webaddress from the back stack
        fwd.push(current) #Pushes the current address to the forward stack
        return newsite #Returns the new webaddress
    except Exception: #Exception for error
        display_error('Unable to move backwards') #Calls the error message function to tell the user they cant move backwards
        return current #Returns the current address

def goForward(current, back, fwd):
    '''
    Go forward to the next webaddress
    Inputs: (current), current webaddress (back), stack for moving backwards (fwd), stack for moving forward
    Returns: (newsite), updated newsite of the next webaddress or (current), current webaddress
    '''    
    try:
        newsite = fwd.pop() #Pops the webaddress from the forward stack
        back.push(current) #Pushes the current address to the back stack
        return newsite #Returns the new webaddress
    except Exception: #Exception for error
        display_error('Unable to move forwards') #Calls the error message function to tell the user they cant move forwards
        return current #Returns the current address

def main():
    HOME = 'www.cs.ualberta.ca'
    back = stack.Stack()
    fwd = stack.Stack()
    current = HOME
    quit = False

    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)
        display_buttons(back, fwd)

        move_cursor(0, 20)
        display_hint("Use <, > to navigate, = to enter a URL, q to quit")
        print_location(5, 5, "Action: ")
        move_cursor(13, 5)
        action = input()
        if action == '=':
            current = goToNewSite(current, back, fwd)
        elif action == '<':
            current = goBack(current, back, fwd)
        elif action == '>':
            current = goForward(current, back, fwd)
        elif action == 'q':
            clear_screen()
            quit = True
        else:
            display_error('Invalid action!')
  

if __name__ == "__main__":
    main()