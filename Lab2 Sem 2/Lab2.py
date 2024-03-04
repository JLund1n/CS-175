import re #Python regex module, will be used to identify white spaces

def Input(): #Method to get the file of the encrypted text and key
    """
    function to get the filename
    """
    file_name = input("Enter the filename (with extension):") #Asks the user for the filename
    while not file_name.endswith("txt"): #Checks to see if the extension is valid, if not loop until it is
        file_name = ("Extension invalid, please re-enter:")
    return file_name #Returns the filename as an object

def decryption_algorythim(file_name): #Method to decrypt the file using the filename object from above
    """
    function to decrypt the file with its respective text and key
    """
    raw_data = open(file_name,'r') #Reads the files contents
    data_key = int(raw_data.readline().strip()) #Grabs the first line which is the key and strips it
    data_text = raw_data.readline().strip() #Grabs the second line and which is the ecryption and strips it

    alpha = re.split(r'\s+', data_text) #Using the regex module and the '\s+' function  the encrypted texts white spaces can be transferred to an array type
    decryted_text = [] #final decrypted text storage

    for letter in alpha: #Loop through the regex data 
        text = '' #Place holder for each word
        letter = letter.lower() #Converts each character to a lower case
    
        for _ in letter: #Loops through each character in letter
            ordinal = ord(_) - data_key #Converts the character to its respective unicode value and subtracts the encryption key from it
            if ordinal < 97: #As it is supposed to be lowercase, unicode 97-122, this if statement ensures the ordinal is of the correct case
                ordinal = ordinal + 26 #If the case is incorrect add 26, letters in the alphabet - 1, which in general loops over the alphabet
            char = chr(ordinal) #Converts the key back to a character
            text += char #Adds the key to the text place holder
        decryted_text.append(text) #Appends the place holder to the final decrypted text storage
    return " ".join(decryted_text) #Joins the storage unit together into one final string

def main():
    file = Input()
    print("The decrypted text is:")
    print(decryption_algorythim(file))
main()