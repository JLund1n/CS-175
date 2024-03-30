import random
import time
def recursive_selection_sort(data, data_len, index = 0): 
    if index >= data_len - 1: #Checks to see if the Index is valid
        return

    minindex = index #Setting the mininmal index to the current which is 0
    while index < data_len:
        if data[minindex] > data[index]: #If the minimal index is greater than the current
            minindex = index #Set the min index to the index
        index += 1 #Else add 1 to the index

    temp = data[data_len - 1] #Temp var
    data[data_len - 1] = data[minindex] #Data of max indicy is set to the minimal
    data[minindex] = temp #Minimal index is now the temp var

    recursive_selection_sort(data, data_len - 1) #Using the new data vals run the recursion function
def recursive_merge_sort(data): 
    if len(data) <= 1: #If the length of the list is 0 or 1
        return data

    mid = len(data) // 2 #Midpoint
    left = recursive_merge_sort(data[:mid]) #Left boundry
    right = recursive_merge_sort(data[mid:]) #Right boundry

    return merge(left, right) #Return the merged list of the left and righ boundry    

def merge(left, right):
    temp = [] #Temp list with temp vals
    i = 0
    j = 0
    n1 = len(left)
    n2 = len(right)

    while i < n1 and j < n2: #While both temp vals are less than the boundry lengths
        if left[i] >= right[j]: #Checking to see which number is larger
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    while i < n1:
        temp.append(left[i])
        i += 1

    while j < n2:
        temp.append(right[j])
        j += 1

    return temp

data = [3, 5, 2, 7, 2, 8, 4, 3, 0, 9]

print("Original", data)

# Sorted using selection sort method
selection_sort_data = data.copy()
recursive_selection_sort(selection_sort_data, len(selection_sort_data))
print("Selection Sort", selection_sort_data)

# Sorted using merge sort method
merge_sort_data = data.copy()
merge_sort_result = recursive_merge_sort(merge_sort_data)
print("Merge Sort", merge_sort_result)    

if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
