class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = Node()   # least recently used side
        self.tail = Node()   # most recently used side

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """Remove node from linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_end(self, node):
        """Add node just before tail (most recently used)."""
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This key was just used, so make it most recent
        self.remove(node)
        self.add_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # Mark as most recently used
            self.remove(node)
            self.add_to_end(node)

        else:
            node = Node(key, value)

            self.cache[key] = node
            self.add_to_end(node)

            # Capacity exceeded
            if len(self.cache) > self.capacity:
                # First real node = least recently used
                lru = self.head.next

                self.remove(lru)
                del self.cache[lru.key]