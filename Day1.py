def day1(arr):

    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: 
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

if __name__ == "__main__":
    test_cases = [
        [0, 1, 2, 1, 0, 2, 1, 0],
        [2, 2, 2, 2],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 0, 1],
        []
    ]

    for i, case in enumerate(test_cases, start=1):
        day1(case)
        print(f"Test Case {i} Output:", case)
