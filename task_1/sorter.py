import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)


long_list = [i for i in range(10000)]

print(f'Time of .sort() is: {timeit.timeit('long_list.sort()', globals=globals(),number=10000)}')

print(f'Time of sorted() is: {timeit.timeit('sorted(long_list)', globals=globals(),number=10000)}')

print(f'Time of insertion_sort() is: {timeit.timeit('insertion_sort(long_list)', globals=globals(),number=10000)}')

print(f'Time of merge_sort() is: {timeit.timeit('merge_sort(long_list)', globals=globals(),number=10000)}')
