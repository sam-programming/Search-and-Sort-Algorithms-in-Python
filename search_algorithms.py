#Search Algorithms from Data Structures

def Binary_Search(word, word_arr) :
    left = 0
    right = len(word_arr) - 1
    iterations = 0
    
    while left <= right:
        mid = (left + right) // 2
        if word_arr[mid] == word:
            print(word, "found at index:", mid, "after", iterations,
                  "iterations")
            return
        else:
            if word < word_arr[mid]:
                right = mid - 1
            if word > word_arr[mid]:
                left = mid + 1
        iterations+=1
    print(word, "not found after", iterations, "iterations")

   
word_arr = ['arch', 'beach', 'celtic', 'dog', 'elf', 'fierce', 'guess',
            'high', 'ilk', 'jest', 'kilt', 'loose', 'moist', 'noise',
            'oath', 'peace', 'quell', 'rain', 'seldom', 'tutor', 'unlit',
            'velvet', 'wired', 'xylophone', 'yield', 'zine']


def Linear_Search(word, word_list):
    for wrd in word_list:
        if wrd == word:
            return True
    return False

def Linear_Search_Max(word_list):
    max_val = word_list[0]
    for wrd in word_list:
        if wrd > max_val:
            max_val = wrd
    return max_val

def Linear_Search_Min(word_list):
    min_val = word_list[-1]
    for wrd in word_list:
        if wrd < min_val:
            min_val = wrd
    return min_val

#find the min and max of an array
arr = [44, 5, 4, 2, 6, 8, 6, 7, 8, 44, 324, 645, 3, 2]

minimum = arr[0]
maximum = arr[0]
min_index = max_index = 0;

for i in range(len(arr)) :
    if arr[i] > maximum:
        maximum = arr[i]
        max_index = i
    if arr[i] < minimum:
        minimum = arr[i]
        min_index = i

print("Min = ", arr[min_index], " Max = ", arr[max_index])

#test wether an array is sorted in ascending order

def Is_Ascending(array):               # O(1)
    for i in range(len(array)-1):      # O(1)#e
        if array[i] > array[i+1]:      # O(1)#e
            return False               # O(1)
    return True                        # O(1)

# Maximum number of comparisons = n - 1
# Time complexity max{ O(n - 1), O(n - 1) }, O(n)

# Sort and Merge arrays where array 1 and array 2 are
# already sorted

def Merge(arr1, arr2):
    i = 0 # loop control for array 1
    j = 0 # loop control for array 2
    arr3 = []
    while i < len(arr1) and j < len(arr2): #will terminate when 1 condition fails
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
    #at this point 1 of the arrays should have elements that have not been merged
    #here we find which array that is and add the remaining elements to arr3    
    while i <= len(arr1)-1:   
        arr3.append(arr1[i])
        i += 1
    while j <= len(arr2)-1:
        arr3.append(arr2[j])
        j += 1    
    return arr3

#Need a function to split the arrays??
def Split(array):
    left = 0
    right = len(array)-1
    left_arr = []
    right_arr = []
    #if the array length is greater than two, split it like so
    if len(array) > 2: 
        mid = (left + right) // 2
        left_arr = array[left:mid-1]
        right_arr = array[mid:right]
    else : #if only two elements, split them easy like
        left_arr = array[left]
        right_arr = array[right]
    return left_arr, right_arr #can i return two arrays?
# Swap two values in an array
def Swap(arr, i1, i2): #array, index 1, index 2
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

#Selection Sort -  not hitting last element
#O(n^2)
def Selection_Sort(arr):
    for i in range(len(arr)): # set the left side of the array
        min_index = i #initialise the minimum
        for x in range(i+1, len(arr)): #iterate over array starting at left
            if arr[min_index] > arr[x]: #compare current min value with the rest of the array
                min_index = x  #if less, new min_index
        if min_index != i:  #if the min is not the current value of arr[i]
            arr[i], arr[min_index] = arr[min_index], arr[i] #swap that shit
                


#Insertion Sort
def Insertion_Sort(arr):
    left = 0
    for index in range(len(arr)-1):
        right = index + 1 # set right boundary
        val = arr[right]  # get value at right boundary
        x = left # loop control
        while x < right:  #starting at 0th index
            if val < arr[x]:  #if the index is ever less than the array
                arr.remove(val) #remove the value at index
                arr.insert(x, val) #insert the value at new index
                x = right          #terminate while loop
            x += 1  #otherwise, iterate while loop
            

def Is_Palindrome(word):
    reverse = ""
    for letter in word:
        reverse
        

#RUN THE FUNCTIONS!!!
                    
s_arr1 = ['cow', 'goat']
s_arr2 = ['cat', 'dog', 'fox', 'lion', 'tiger']
arr1 = ['milk']
arr2 = ['kitten']
us_arr = ['fox', 'cow', 'pig', 'cat', 'rat', 'lion', 'tiger', 'goat', 'dog']
us_int_arr = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 88, 1, 12]
merged_arr = Merge(arr1, arr2)
#print(merged_arr)

#Selection_Sort(us_int_arr)
#Insertion_Sort(us_int_arr)
#print(us_int_arr)
#print(Is_Ascending(word_arr))
#Binary_Search('elfs', word_arr)
#print(Linear_Search('seldom', word_arr))
#print(Linear_Search_Min(word_arr))
#print(Linear_Search_Max(word_arr))
      
        
