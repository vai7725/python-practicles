# Function to perform sequential search
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
        
    return -1

arr = [3, 10, 4, 7, 2, 8]
target = 7

result = sequential_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
