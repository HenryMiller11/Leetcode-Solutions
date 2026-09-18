class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first, last = {}, {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i

        intervals = []
        for i in range(n):
            c = s[i]
            if first[c] != i:
                continue
            start, end, j, valid = i, last[c], i, True
            while j <= end:
                cj = s[j]
                if first[cj] < start:
                    valid = False
                    break
                if last[cj] > end:
                    end = last[cj]
                j += 1
            if valid:
                intervals.append((start, end))

        intervals.sort()
        res, stack = [], []  # stack: [start, end, has_child]
        for start, end in intervals:
            while stack and stack[-1][1] < start:
                s0, e0, has_child = stack.pop()
                if not has_child:
                    res.append((s0, e0))
                if stack:
                    stack[-1][2] = True
            stack.append([start, end, False])
        while stack:
            s0, e0, has_child = stack.pop()
            if not has_child:
                res.append((s0, e0))
            if stack:
                stack[-1][2] = True

        return [s[a:b+1] for a, b in res]