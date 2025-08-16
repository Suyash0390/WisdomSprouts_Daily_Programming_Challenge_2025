def find_missing_number(arr):
   
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    
    return total_sum - actual_sum

if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 5],
        [2, 3, 4, 5],
        [1, 2, 3, 4],
        [1],
        list(range(1, 1000000)) 
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input: {case[:10]}{'...' if len(case) > 10 else ''}")
        print(f"Missing number: {find_missing_number(case)}\n")
