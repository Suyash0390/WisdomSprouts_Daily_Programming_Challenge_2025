def find_leaders(arr):

    n = len(arr)
    if n == 0:
        return []
    
    leaders = []

    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    leaders.reverse()
    return leaders

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 0],
        [7, 10, 4, 10, 6, 5, 2],
        [5],
        [100, 50, 20, 10],
        list(range(1, 1000001)) 
    ]
    
    for arr in test_cases:
        result = find_leaders(arr)
        print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")
        print(f"Leaders: {result}\n")
