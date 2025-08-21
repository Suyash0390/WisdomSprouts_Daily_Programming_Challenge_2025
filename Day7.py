def trap(height):

    if not height or len(height) < 3:
        return 0 
    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    water = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            water += max_right - height[right]

    return water

if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 1, 1],
        [5],
        [2, 0, 2],
    ]

    for i, arr in enumerate(test_cases, 1):
        result = trap(arr)
        print(f"Test Case {i}: Input = {arr}")
        print(f"Output = {result}\n")
