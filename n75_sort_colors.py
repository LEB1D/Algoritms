from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1

        for i in range(0, zeros):
            nums[i] = 0

        for i in range(zeros, zeros + ones):
            nums[i] = 1

        for i in range(zeros + ones, n):
            nums[i] = 2


# Создаём объект класса Solution
solution = Solution()

# Тестируем метод
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)  # Вызываем метод через объект
print(nums)  # Вывод: [0, 0, 1, 1, 2, 2]
