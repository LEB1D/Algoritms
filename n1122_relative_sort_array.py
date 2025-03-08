from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)  # Лічимо кількість входжень кожного елемента
        result = []

        # Додаємо елементи, що є в arr2, у правильному порядку
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        # Додаємо решту елементів, яких немає в arr2, у відсортованому порядку
        for num in sorted(count.keys()):
            result.extend([num] * count[num])

        return result


# Виклик функції через екземпляр класу Solution
solution = Solution()
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
# Очікуваний вихід: [2,2,2,1,4,3,3,9,6,7,19]
print(solution.relativeSortArray(arr1, arr2))

arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
# Очікуваний вихід: [22,28,8,6,17,44]
print(solution.relativeSortArray(arr1, arr2))
