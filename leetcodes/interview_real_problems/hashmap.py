# When you don't know the collision strategy of a hashmap, How do you implement a hashmap from scratch?
# Your hash function should be able to handle collisions.
# Your hash function should be able to handle any type of key.
# Your hash function should be able to handle any type of value.
# Your hash function should be able to handle any type of hashmap.


class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        hash_index = self.hash_function(key)
        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self.hash_function(key)
        return self.table[hash_index]

    def remove(self, key):
        hash_index = self.hash_function(key)
        self.table[hash_index] = None

    def contains(self, key):
        hash_index = self.hash_function(key)
        return self.table[hash_index] is not None

    def keys(self):
        return [key for key in self.table if key is not None]

    def values(self):
        return [value for value in self.table if value is not None]

    def clear(self):
        self.table = [[] for _ in range(self.size)]


# if __name__ == "__main__":
#     hash_map = HashMap(10)
#     hash_map.put(1, "one")
#     hash_map.put(1, "two")
#     hash_map.put(2, "two")
#     hash_map.put(3, "three")
#     print(hash_map.get(1))
#     print(hash_map.get(2))


# Use Linked List to handle collisions


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapLinkedList:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        hash_index = self.hash_function(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = Node(key, value)
        else:
            current = self.table[hash_index]
            while current:
                if current.key == key:
                    current.value = value

                if current.next is None:
                    current.next = Node(key, value)
                    break

                current = current.next

    def get(self, key):
        hash_index = self.hash_function(key)
        current = self.table[hash_index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        hash_index = self.hash_function(key)
        current = self.table[hash_index]
        while current:
            if current.key == key:
                current.value = None
                break
            current = current.next

    def contains(self, key):
        hash_index = self.hash_function(key)
        current = self.table[hash_index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def keys(self):
        keys = []
        for node in self.table:
            while node:
                keys.append(node.key)
                node = node.next
        return keys

    def values(self):
        values = []
        for node in self.table:
            while node:
                values.append(node.value)
                node = node.next
        return values

    def clear(self):
        self.table = [None] * self.size


if __name__ == "__main__":
    hash_map = HashMapLinkedList(10)
    hash_map.put(1, "one")
    hash_map.put(2, "two")
    hash_map.put(3, "three")
    hash_map.put(1, "two")
    print(hash_map.get(1))
    print(hash_map.get(2))
    print(hash_map.get(3))
    print(hash_map.contains(1))
    print(hash_map.contains(2))
    print(hash_map.contains(3))
