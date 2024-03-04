#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Asks the user for an action from the selection available
    Inputs: None
    Returns: 'userinput' The action to which the user selects
    '''
    ValidEntry = False #Initalizes the userinput validity as false
    while not ValidEntry: #While the validity of the user entry is false keep prompting
        userinput = input('Please enter = to enter a URL, < to go back, > to go forward, or q to quit\n') #Grabs the userinput with 3 seprate cases
        if userinput == '=' or userinput == '<' or userinput == '>' or userinput == 'q': #Checks to see if the user input is one of the 3 cases
            ValidEntry = True #If it is the entry is now valid and the loop is broken
        else: #If not
            print('Entry invalid, please try again') #Let the user know and reprompt
    return userinput #Return the selection of the userinput


def goToNewSite(current, pages):
    '''
    Gets a new site from the user and adds it to the pages list
    Inputs: 'current', index of the current site within the list of pages, 'pages', list of sites
    Returns: index of the new site into the pages list
    '''   
    site = input('URL: ') #Prompts the user for a new site URL
    pages.append(site) #Appends the new URL to the pages list 
    return len(pages) - 1 #Returns the index of the new site from the pages list

    
def goBack(current, pages):
    '''
    Go back to the previous site
    Inputs: 'current', index of the current site within the list of pages, 'pages', list of sites
    Returns: previous site index from the list of sites
    '''    
    if current > 0: #To go backwards the current site index must be the greater than the first, 0
        return current - 1 #If it is take the current site index and subtract 1
    else: #Otherwise
        print('Unable to go back') #Tell the user they are unable to move backwards
        return current #Return the site index


def goForward(current, pages):
    '''
    Go forward to the next site
    Inputs: 'current', index of the current site within the list of pages, 'pages', list of sites
    Returns: Next site index from the list of sites
    '''    
    if current < len(pages) - 1: #To go forwards the current site index must be less than the last site index
        return current + 1 #If the case above is valid take the current site index and add 1
    else: #Otherwise
        print('unable to go forward') #Tell the user they are unable to move forwards
        return current #Return the site index
 

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    