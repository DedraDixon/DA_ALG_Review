def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

if __name__=="__main__":
    ls = [1, 100, 233, 90, 4, 52, 81, 10]
    target_found = linear_search(ls, 81)
    not_found = linear_search(ls, 91)
    print(f"First target found at index {target_found}")
    print(f"Second target not found. Value is {not_found}")
