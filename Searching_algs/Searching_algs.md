# Sorting Algorithms
Searching algorithms are methods to arrange elements in a specific order.

## Linear Search
With linear search, a list is passed to the algorithm. It looks at every individual element to check if it is equal to the target. 

Worst Case: O(n)
Best Case: O(1)

[See Example](linear_search.py)


## Binary Search
After inputing a sorted list, the algorithm returns the position of the element you're looking for if it exists in the list otherwise it returns null or -1. It begins from the middle of the list and determines if the number is higher or lower. From this criteria, half the list is eliminated. The remaining list is repeatedly cut in half by determining if the number is lower or higher than the middle element. 

Worst Case: O(log n)
Best Case: O(1)

[See Example](binary_search.py)

## Jump Search
Jump search is like binary search in that it must be passed a sorted array. The list is chunked down into smaller arrays of n elements. Until the algorithm finds out which subarray the target could be in, it only compares the last element in every subarray to the target. Once the potential subarray is found, linear search is applied to that array to determine if the target exists in it. 

Worst Case: O(log n)
Best Case: O(1)

[See Example](jump_search.py)

## Exponential Search
