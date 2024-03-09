class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def add(self, item):
        temp = DLinkedListNode(item, self.__head, None) #Temp node
        if self.__head is not None: #If the head of the list is not a None type
            self.__head.setPrevious(temp) #Set the previous nodes head to the temp node
        else: #Otherwise
            self.__tail = temp #The tail is now the temp node
        self.__head = temp 
        self.__size += 1 #Increase the list size by 1


    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        if self.search(item): #Search for the item in the list
            while not found: #If it is not found
                if current.getData() == item: #If current data contains the item
                    found = True #Item found
                else: #Otherwise move through the list
                    previous = current
                    current = current.getNext()
            if previous is None: #Checks to see if the previous node is still None type
                self.__head = current.getNext() #If so move through the list
            else:
                previous.setNext(current.getNext())
            if current.getNext() is not None: #if the current node is not of None type
                current.getNext().setPrevious(previous) #Set the previous node to that of the none type
            else:
                self.__tail = previous
            self.__size -= 1 
        else:
            pass

    def append(self, item):
        temp = DLinkedListNode(item, None, None) #Temp node
        if self.__head is None: #If the head is of the none type
            self.__head = temp #Set it to the temp node
        else:
            self.__tail.setNext(temp) #Set the next node to the temp node
            temp.setPrevious(self.__tail)
        self.__tail = temp
        self.__size += 1

    def insert(self, pos, item):
        if self.__size == 0 or pos == 0: #If the size of the list or position is 0
            self.add(item) #Add the item
        elif pos == self.__size: #If the position is the same as the size
            self.append(item) #Append the item
        else:
            pastnode = self.__head
            i = 1
            while i < pos: #Loop through the list positions
                pastnode = pastnode.getNext()
                i += 1
            nextnode = pastnode.getNext()
            newnode = DLinkedListNode(item, nextnode, pastnode)
            pastnode.setNext(newnode)
            newnode.setPrevious(newnode)
            self.__size += 1

    def pop1(self):
        if self.__size < 0: #Checks to see if the list is empty
            raise Exception('Empty List')
        current = self.__head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        if previous is None:
            self.__head = None
        else:
            previous.setNext(None)
        self.__size = self.__size - 1
        return current.getData()

    def pop(self, pos=None):
        if pos is not None: #If the position is that of a None type
            assert pos >= 0, "Error: can't be negative"
        if self.__size < 0: #If the size is less than 0
            raise Exception("List is Empty")
        current = self.__head
        next_node = current.getNext()
        removed = None
        if pos == self.__size or pos is None:
            removed = self.pop1()
        elif pos == 0:
            removed = current
            next_node.setPrevious(None)
            self.__head = next_node
        else:
            i = 0
            while i < pos:
                current = current.getNext()
                i += 1
            removed = current.getData()
            self.remove(current.getData())
        self.__size -= 1
        return removed

    def searchLarger(self, item):
        assert type(item) == int, "Error not an integer"
        current = self.__head
        found = False
        value = None
        while current is not None and not found:
            if current.getData() > item:
                found = True
                value = self.index(current.getData())
            else:
                current = current.getNext()
        return value

    def getSize(self):
        i = 0
        current = self.__head
        while current is not None:
                current = current.getNext()
                i += 1
        return i

    def getItem(self, pos):
        assert type(pos) == int, "Not an integer"
        assert -self.getSize() <= pos <= self.getSize(), "Error: Out of range"
        current = self.__head
        if pos == 0:
            pass
        elif pos > 0:
            for i in range(pos):
                current = current.getNext()
        else:
            return self.getItem(self.getSize() + pos)
        return current.getData()

    def __str__(self):
        current = self.__head
        string = ''
        while current is not None:
            if current.getNext() is None:
                string = string + str(current.getData())
            else:
                string = string + str(current.getData()) + ' '
            current = current.getNext()
        return string

def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) ==
               "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
    x = linked_list.pop(1)
    is_pass = (x == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
    x = int_list2.getSize()
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)
    x = int_list.searchLarger(800)
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    x = int_list.getItem(-1)
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()
