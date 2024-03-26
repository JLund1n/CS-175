def mylen(alist):
    if alist == []: #Checks to see if the list is empty
        return 0 
    else:
        return 1 + mylen(alist[1:]) #Gets the max indicy of the list and adds 1 to it to get the length

def intDivision(a,b):
    if b <= 0: #Checks to see if the divisor is less than or equat to 0
        raise Exception
    if a < 0: #Checks to see if the dividend is less than 0
        raise Exception
    x = 0 #Place holder var
    while (a >= b): #While the dividend is greater than the divisor
        a -= b #Subtract b from a
        x += 1 #Add 1 to x
    return x #Returns the place holder val
    
def sumdigits(n):
    if n < 0: #Checks to see if the number is less than 0
        raise Exception
    if n < 10: #Checks to see if the number is less than 10
        return n
    else:
        return (n%10) + sumdigits(n//10) #Gets the modulus of the num and 10 then adds the sumdigits factor of 10

def reverseDisplay(n):
    if n < 0: #Checks to see if the number is less than 0
        raise Exception
    if n == 0: #If the number is 0
        return n
    print(n%10, end='') #Get the modulus of the number
    reverseDisplay(int(n/10)) #Take the number and divide by 10

def binary_search(key, alist, low, high):
    if high < low: #If the high is less than the low
        return -1
    middle = (high + low) // 2 #Takes the average of the two
    if key == alist[middle]: #If the key is the middle val
        return middle
    elif key < alist[middle]: #If the key is less than the middle search the lower half of the list
        passed = binary_search(key, alist, low, middle-1)
        if passed == -1:
            return 'The item is not in the list'
        return passed
    else:
        passed = binary_search(key, alist, middle + 1, high) #Else search the upperhalf of the list
        if passed == -1:
            return 'The item is not in the list'
        return passed
    
def main():
    alist = [43, 76, 97, 86]
    print(mylen(alist))
    a = int(input('Input an int dividend: '))
    b = int(input('Input an int divisor: '))
    x = a // b
    print('Int division ' + str(a) + ' // ' + str(b) + ' = ' + str(intDivision(a,b)))
    num = int(input('Please input a number: '))
    print(sumdigits(num))
    num1 = int(input('Please input a number: '))
    reverseDisplay(num1)
    somelist = [-8,-2,1,3,5,7,9]
    print('\n')
    print(binary_search(9,somelist,0,len(somelist)-1))
    print(binary_search(-8,somelist,0,len(somelist)-1))
    print(binary_search(4,somelist,0,len(somelist)-1))

if __name__ == '__main__':
    main()
