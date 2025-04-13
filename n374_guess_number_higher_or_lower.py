pick = 20


def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(guessNumber(100))
