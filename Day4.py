def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge(arr1, arr2):

    m, n = len(arr1), len(arr2)
    gap = next_gap(m + n)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):

            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        gap = next_gap(gap)


if __name__ == "__main__":
    arr1, arr2 = [1, 3, 5, 7], [2, 4, 6, 8]
    merge(arr1, arr2)
    print("arr1:", arr1)
    print("arr2:", arr2)

    arr1, arr2 = [10, 12, 14], [1, 3, 5]
    merge(arr1, arr2)
    print("arr1:", arr1)
    print("arr2:", arr2)

    arr1, arr2 = [2, 3, 8], [4, 6, 10]
    merge(arr1, arr2)
    print("arr1:", arr1)
    print("arr2:", arr2)

    arr1, arr2 = [1], [2]
    merge(arr1, arr2)
    print("arr1:", arr1)
    print("arr2:", arr2)
