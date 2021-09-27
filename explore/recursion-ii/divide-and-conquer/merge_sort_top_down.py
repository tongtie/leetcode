def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = len(nums) // 2
    left = merge_sort(nums[:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# TODO: test
if __name__ == '__main__':
    nums = [3, 5, 2, 1, 4]
    print(merge_sort(nums))
    nums = [1, 2, 3, 4, 5]
    print(merge_sort(nums))
    nums = [5, 4, 3, 2, 1]
    print(merge_sort(nums))
    nums = [1]
    print(merge_sort(nums))
    nums = []
    print(merge_sort(nums))
    nums = [1, 2]
    print(merge_sort(nums))
    nums = [2, 1]
    print(merge_sort(nums))