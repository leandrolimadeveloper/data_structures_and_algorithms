import random

def binary_search(lst, target):
    low = 0  
    high = len(lst) - 1  

    while low <= high:  
        mid = (low + high) // 2  
        guess = lst[mid]

        if guess == target:  
            return mid
        if guess > target:  
            high = mid - 1
        else:  
            low = mid + 1

    return None  

my_list = [1, 3, 5, 7, 9, 10, 15, 20, 24, 25, 28]
my_list_up_to_100 = sorted(random.sample(range(1, 101), 100))  

print(binary_search(my_list, 1)) 
print(binary_search(my_list, -1))  # return none 
print(binary_search(my_list_up_to_100, 50))
