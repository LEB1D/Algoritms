from collections import Counter


def intersect(nums1, nums2):
    count = Counter(nums1)
    result = []

    for num in nums2:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result


# Тести
print(intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9] або [9,4]
