# Function works to repeatedly find the next smallest number in the list
def find_smallest(arr):
    smallest_i = 0
    smallest = arr[0]
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_i = i
        
    return smallest_i

def selection_sort(arr):
    sorted = []
    copy = list(arr)
    while copy:
        smallest_index = find_smallest(copy)
        sorted.append(copy[smallest_index])
        copy.pop(smallest_index)
    return sorted

if __name__ == "__main__":
    arr = [1, 56, 23, 67, 34, 10, 11, 90]
    sorted_array = selection_sort(arr)
    print(f"sorted array: {sorted_array}")