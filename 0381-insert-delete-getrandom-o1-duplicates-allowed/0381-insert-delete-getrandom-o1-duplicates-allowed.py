import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        # True if this is the first occurrence
        is_new = val not in self.indices

        # Add value to the list
        self.nums.append(val)

        # Store its index
        if val not in self.indices:
            self.indices[val] = set()

        self.indices[val].add(len(self.nums) - 1)

        return is_new

    def remove(self, val: int) -> bool:
        if val not in self.indices or not self.indices[val]:
            return False

        # Get any index containing val
        idx = self.indices[val].pop()

        # Last element
        last = self.nums[-1]
        last_idx = len(self.nums) - 1

        # Move last element into removed position
        self.nums[idx] = last

        # Update last element's index
        self.indices[last].add(idx)

        # Remove old last index
        self.indices[last].discard(last_idx)

        # Remove last element from list
        self.nums.pop()

        # If no occurrences remain, remove key
        if not self.indices[val]:
            del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)