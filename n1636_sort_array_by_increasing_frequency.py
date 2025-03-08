from collections import Counter


def frequencySort(nums):
    count = Counter(nums)  # Підраховуємо частоти
    # Сортуємо за частотою, потім у спадному порядку
    return sorted(nums, key=lambda x: (count[x], -x))


# Приклади використання:
nums1 = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums1))  # Вихід: [3,1,1,2,2,2]

nums2 = [2, 3, 1, 3, 2]
print(frequencySort(nums2))  # Вихід: [1,3,3,2,2]

nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(frequencySort(nums3))  # Вихід: [5,-1,4,4,-6,-6,1,1,1]
