def insertion_sort(arr):
    current = 0

    # The range begins from one because the first element is considered to be in the correct position
    for i in range(1, len(arr)):
        current  = arr[i]
        prev = i -1
        print(f"current element: {current}")
        print(f"arr's current state: {arr}")
        while current < arr[prev] and prev >= 0:
            arr[prev+1] = arr[prev]
            prev -= 1
            print(f"arr's current state: {arr}")
        arr[prev+1] = current 
        print(f"correct position for {current} found: {arr}")



if __name__ == "__main__":
    arr = [1, 56, 23, 67, 34, 10, 11, 90]
    insertion_sort(arr)