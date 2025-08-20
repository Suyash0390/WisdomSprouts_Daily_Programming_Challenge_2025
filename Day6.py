def find_zero_sum_subarrays(arr):
    
    prefix_sum = 0
    prefix_map = {0: [-1]}   
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in prefix_map:
            for start in prefix_map[prefix_sum]:
                result.append((start + 1, i))

        prefix_map.setdefault(prefix_sum, []).append(i)

    return result

print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1])) 
print(find_zero_sum_subarrays([1, 2, 3, 4]))          
print(find_zero_sum_subarrays([0, 0, 0]))             
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))  
print(find_zero_sum_subarrays([1, -1, 2, -2, 3, -3] * 10000))  
