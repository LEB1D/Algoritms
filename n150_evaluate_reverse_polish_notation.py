from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = {"+": 0, "-": 1, "*": 2, "/": 3}
        stack = []
        for st in tokens:
            if st in exp:
                n2 = stack.pop()
                n1 = stack.pop()
                if exp[st] == 0:
                    stack.append(n1+n2)
                elif exp[st] == 1:
                    stack.append(n1-n2)
                elif exp[st] == 2:
                    stack.append(n1*n2)
                else:
                    stack.append(int(n1/n2))
            else:
                stack.append(int(st))
        return stack[0]


sol = Solution()
tokens = ["2", "1", "+", "3", "*"]  # (2 + 1) * 3 = 9
result = sol.evalRPN(tokens)
print("Результат:", result)
