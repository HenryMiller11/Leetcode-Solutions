class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def multiply(A, B):
            return {a + b for a in A for b in B}

        def parse(i):
            res = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    # Parse everything inside {}
                    cur, i = parse(i + 1)
                elif expression[i] == ',':
                    # Union: handled by caller
                    break
                else:
                    cur = {expression[i]}
                    i += 1

                # Concatenate with what we have so far
                res = multiply(res, cur)

            return res, i

        def solve(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1

                elif expression[i] == '{':
                    part, i = solve(i + 1)
                    cur = multiply(cur, part)

                else:
                    cur = multiply(cur, {expression[i]})
                    i += 1

            res |= cur

            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        result, _ = solve(0)
        return sorted(result)