
def binary_search(ls, n):
    start = 0 
    end = len(ls)-1

    while start <= end:
        mid = (start+end) // 2  # Take the floor (round down to the nearest number)
        current = ls[mid]  # Get the element at the middle index
        if current < n:
            start = mid+1  # do -1 because we've already ruled out the middle element itself
        elif current > n:
            end = mid-1  # do +1 because we've already ruled out the middle element itself
        elif current == n:
            return mid  # The number was found so return the index of the number within the list/array
    
    return -1  # The number n does not exist in the list

if __name__=="__main__":
    sorted_array = [2, 4, 6, 8, 10]
    ls=[1, 135, 402, 677, 1012, 1489, 1773, 2201, 2540, 2894, 3255,
    3610, 4022, 4451, 4888, 5204, 5630, 5912, 6328, 6771, 7014,
    7450, 7899, 8201, 8644, 9022, 9455, 9877, 10234, 10588, 10920,
    11277, 11610, 11945, 12289, 12630, 13004, 13355, 13710, 14022, 14388,
    14701, 15044, 15402, 15777, 16090, 16455, 16788, 17144, 17502, 17890,
    18233, 18599, 18940, 19312, 19655, 20088, 20410, 20855, 21290, 21644,
    22080, 22455, 22899, 23244, 23688, 24022, 24390, 24755, 25120, 25499,
    25844, 26201, 26540, 26988, 27311, 27699, 28055, 28390, 28745, 29099,
    29440, 29888, 30210, 30577, 30940, 31322, 31655, 32011, 32390, 32755,
    33102, 33490, 33855, 34210, 34588, 34920, 35277, 35610, 35944, 36320, 5000]
    found = binary_search(sorted_array, 4)
    print(found)
    not_found = binary_search(sorted_array, 1)
    print(not_found)