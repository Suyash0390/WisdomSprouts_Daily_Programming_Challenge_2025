def find_duplicate(arr):

    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

if __name__ == "__main__":
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
        [1, 4, 4, 2, 3],
        list(range(1, 100000)) + [50000]
    ]
    
    for arr in test_cases:
        print(find_duplicate(arr))
