
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = parent[:]

        def dfs(node):
            ch = s[node]

            old = last.get(ch, -1)

            if old != -1:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old == -1:
                last.pop(ch, None)
            else:
                last[ch] = old

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        ans = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)

        return ans
