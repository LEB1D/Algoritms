def heightChecker(heights: list[int]) -> int:
    """
    Повертає кількість позицій, де висоти відрізняються від очікуваних (відсортованих).
    """
    expected = sorted(heights)
    count = sum(heights[i] != expected[i] for i in range(len(heights)))
    return count


heights = [1, 2, 3, 4, 5]
print(heightChecker(heights))  # Очікуваний результат: 3
