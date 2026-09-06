from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter_id = {}
        start_r = start_c = 0
        litter_count = 0

        # Locate S and assign each L a bit.
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = litter_count
                    litter_count += 1

        # No litter to collect.
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1

        # (row, col, mask, remaining_energy)
        queue = deque()
        queue.append((start_r, start_c, 0, energy))

        visited = set()
        visited.add((start_r, start_c, 0, energy))

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c, mask, remaining = queue.popleft()

                if mask == full_mask:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need one unit of energy to move.
                    if remaining == 0:
                        continue

                    new_energy = remaining - 1
                    new_mask = mask

                    # Collect litter.
                    if (nr, nc) in litter_id:
                        new_mask |= 1 << litter_id[(nr, nc)]

                    # Reset energy after reaching R.
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1