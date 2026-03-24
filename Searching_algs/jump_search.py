import math

def jump_search(arr, target):
    
    # While the optimal step size is √n, it can be changed to any step size
    n = len(arr) 
    step = int(math.sqrt(n))
    prev = 0

    # Jump until we find the block
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        
        if prev >= n:
            return -1  # Not found

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1  


if __name__=="__main__":
    ls = [1, 135, 402, 677, 1012, 1489, 1773, 2201, 2540, 2894, 3255,
    3610, 4022, 4451, 4888, 5204, 5630, 5912, 6328, 6771, 7014,
    7450, 7899, 8201, 8644, 9022, 9455, 9877, 10234, 10588, 10920,
    11277, 11610, 11945, 12289, 12630, 13004, 13355, 13710, 14022, 14388,
    14701, 15044, 15402, 15777, 16090, 16455, 16788, 17144, 17502, 17890,
    18233, 18599, 18940, 20088, 20410, 20855, 21290, 21644,
    22080, 22455, 22899, 23244, 23688, 24022, 24390]
    t = 24390
    y = jump_search(ls, t)
    print(y)

