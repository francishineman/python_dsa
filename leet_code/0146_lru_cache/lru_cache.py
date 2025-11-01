#!/usr/bin/env python3


'''
Design a data structure that follows the constraints of a LRU Cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size 
capacity.
int get(int key) Return the value of the key if the key exists, 
otherwise return -1.
void put(int key, int value) Update the value of the key if the key 
exists. Otherwise, add the key-value pair to the cache. If the number of
 keys exceeds the capacity from this operation, evict the least recently
 used key.

implement functions :
Add a new node right after the dummy head (making it the MRU).

And then create a test to input new nodes to the LRUCache class
'''


class Node:
    __slots__ = ("key", "value", "prev", "next")
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        self.capacity = capacity
        self.cache = {}

        # Sentinels: head <-> ... <-> tail
        self.head = Node(0, 0)  # MRU side
        self.tail = Node(0, 0)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- DLL helpers ---
    def _remove_node(self, node: Node) -> None:
        """Detach node from the list (node must not be a sentinel)."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        # optional hygiene
        node.prev = node.next = None

    def _insert_after(self, left: Node, node: Node) -> None:
        """Insert node right after 'left'."""
        right = left.next
        left.next = node
        node.prev = left
        node.next = right
        right.prev = node

    def _add_to_mru(self, node: Node) -> None:
        """Add node immediately after head (most recently used position)."""
        self._insert_after(self.head, node)

    def _pop_lru(self) -> Node | None:
        """Remove and return the LRU node (just before tail), or None if empty."""
        lru = self.tail.prev
        if lru is self.head:
            return None
        self._remove_node(lru)
        return lru

    # --- API ---
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self._remove_node(node)
        self._add_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self._remove_node(node)
            self._add_to_mru(node)
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_mru(new_node)

        if len(self.cache) > self.capacity:
            evicted = self._pop_lru()
            if evicted is not None:
                self.cache.pop(evicted.key, None)


# --- Test Cases ---

def test_lru_cache():
    print("--- Test Case 1: Standard LRU Flow (Capacity 2) ---")
    lru_cache = LRUCache(2)

    # 1. Put (1, 1)
    print("\nPutting (1, 1)")
    lru_cache.put(1, 1)
    
    # 2. Put (2, 2)
    print("Putting (2, 2)")
    lru_cache.put(2, 2)
    
    # Cache state: MRU -> [2, 2] | LRU -> [1, 1]

    # 3. Get key 1 (Promotes 1 to MRU)
    result_1 = lru_cache.get(1)
    print(f"Getting key 1: {result_1} (Expected: 1). Cache state: MRU -> [1, 1] | LRU -> [2, 2]")
    
    # 4. Put (3, 3) - Forces eviction of LRU (key 2)
    print("Putting (3, 3) - Should evict key 2")
    lru_cache.put(3, 3)
    # Cache state: MRU -> [3, 3] | LRU -> [1, 1]

    # 5. Get key 2 (Should be -1)
    result_2 = lru_cache.get(2)
    print(f"Getting key 2: {result_2} (Expected: -1, because it was evicted)")
    
    # 6. Put (4, 4) - Forces eviction of LRU (key 1)
    print("Putting (4, 4) - Should evict key 1")
    lru_cache.put(4, 4)
    # Cache state: MRU -> [4, 4] | LRU -> [3, 3]

    # 7. Get key 1 (Should be -1)
    result_3 = lru_cache.get(1)
    print(f"Getting key 1: {result_3} (Expected: -1)")

    # 8. Get key 3 (Should be 3, promotes 3 to MRU)
    result_4 = lru_cache.get(3)
    print(f"Getting key 3: {result_4} (Expected: 3). Cache state: MRU -> [3, 3] | LRU -> [4, 4]")
    
    # 9. Put (5, 5) - Forces eviction of LRU (key 4)
    print("Putting (5, 5) - Should evict key 4")
    lru_cache.put(5, 5)
    # Cache state: MRU -> [5, 5] | LRU -> [3, 3]

    # 10. Get key 4 (Should be -1)
    result_5 = lru_cache.get(4)
    print(f"Getting key 4: {result_5} (Expected: -1)")

    print("\n" + "="*50)
    print("--- Test Case 2: Update Operation (Capacity 3) ---")
    lru_cache_update = LRUCache(3)
    
    lru_cache_update.put(10, 100) # [10]
    lru_cache_update.put(20, 200) # [20, 10]
    lru_cache_update.put(30, 300) # [30, 20, 10]
    print("Initial state (Capacity 3): Keys: 30(MRU), 20, 10(LRU)")

    # 11. Put (20, 222) - Update existing key 20, should move it to MRU
    print("Putting (20, 222) - Update and promote key 20")
    lru_cache_update.put(20, 222)
    # Cache state: MRU -> [20, 222] | [30, 300] | LRU -> [10, 100]
    result_update_1 = lru_cache_update.get(20)
    print(f"Getting key 20: {result_update_1} (Expected: 222). State: MRU -> 20, 30, 10(LRU)")

    # 12. Put (40, 400) - Should evict LRU (key 10)
    print("Putting (40, 400) - Should evict key 10")
    lru_cache_update.put(40, 400)
    # Cache state: MRU -> [40, 400] | [20, 222] | LRU -> [30, 300]
    result_update_2 = lru_cache_update.get(10)
    print(f"Getting key 10: {result_update_2} (Expected: -1)")
    result_update_3 = lru_cache_update.get(30) # Get 30 to check it's still there
    print(f"Getting key 30: {result_update_3} (Expected: 300). State: MRU -> 30, 40, 20(LRU)")
    
    print("\n" + "="*50)
    print("--- Test Case 3: Edge Case (Capacity 1) ---")
    lru_cache_one = LRUCache(1)
    
    # 13. Put (100, 1)
    print("Capacity 1: Putting (100, 1)")
    lru_cache_one.put(100, 1) # [100]

    # 14. Put (200, 2) - Evicts key 100
    print("Capacity 1: Putting (200, 2) - Should evict key 100")
    lru_cache_one.put(200, 2) # [200]

    # 15. Get key 100 (Should be -1)
    result_one_1 = lru_cache_one.get(100)
    print(f"Capacity 1: Getting key 100: {result_one_1} (Expected: -1)")

    # 16. Get key 200 (Should be 2)
    result_one_2 = lru_cache_one.get(200)
    print(f"Capacity 1: Getting key 200: {result_one_2} (Expected: 2)")


def main():
    test_lru_cache()


if __name__ == "__main__":
    main()
