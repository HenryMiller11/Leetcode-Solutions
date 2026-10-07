class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0

        # Find minimum removals needed
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = set()

        def backtrack(i, path, balance, l, r):
            if balance < 0:
                return

            if i == len(s):
                if balance == 0 and l == 0 and r == 0:
                    result.add("".join(path))
                return

            ch = s[i]

            if ch == '(':
                # Remove '('
                if l > 0:
                    backtrack(i + 1, path, balance, l - 1, r)

                # Keep '('
                path.append(ch)
                backtrack(i + 1, path, balance + 1, l, r)
                path.pop()

            elif ch == ')':
                # Remove ')'
                if r > 0:
                    backtrack(i + 1, path, balance, l, r - 1)

                # Keep ')' only if it has a matching '('
                if balance > 0:
                    path.append(ch)
                    backtrack(i + 1, path, balance - 1, l, r)
                    path.pop()

            else:
                path.append(ch)
                backtrack(i + 1, path, balance, l, r)
                path.pop()

        backtrack(0, [], 0, left, right)

        return list(result)