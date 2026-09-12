class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_front(self, node):
        # Add after dummy head
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # key -> Node
        self.cache = {}

        # frequency -> DLL
        self.freq_map = {}

        # Minimum frequency currently in cache
        self.min_freq = 0

    def _get_list(self, freq):
        if freq not in self.freq_map:
            self.freq_map[freq] = DoublyLinkedList()

        return self.freq_map[freq]

    def _increase_frequency(self, node):
        old_freq = node.freq
        old_list = self.freq_map[old_freq]

        old_list.remove(node)

        # If this was the last node at min_freq,
        # min_freq increases.
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1

        node.freq += 1

        new_list = self._get_list(node.freq)
        new_list.add_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Using the key increases its frequency
        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Capacity 0 case
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # put() also increases frequency
            self._increase_frequency(node)

            return

        # Cache is full -> evict LFU
        if self.size == self.capacity:
            lfu_list = self.freq_map[self.min_freq]

            # Least recently used among LFU nodes
            node_to_remove = lfu_list.remove_last()

            del self.cache[node_to_remove.key]

            self.size -= 1

        # Insert new node
        node = Node(key, value)

        self.cache[key] = node

        self._get_list(1).add_front(node)

        self.min_freq = 1
        self.size += 1