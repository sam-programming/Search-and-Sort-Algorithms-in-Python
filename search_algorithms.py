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

Binary_Search('elfs', word_arr)
print(Linear_Search('seldom', word_arr))
print(Linear_Search_Min(word_arr))
print(Linear_Search_Max(word_arr))
        
        
