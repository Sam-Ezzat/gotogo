import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generate a list of 1000 random numbers
numbers = [random.randint(0, 10000) for _ in range(1000)]

print("Unsorted Numbers is : " , numbers)
# Sort the list using quick sort
sorted_numbers = quick_sort(numbers)

print("Sorted Numbers: " , sorted_numbers)
print("this is the quick sort algorithm , need to know how to work")
