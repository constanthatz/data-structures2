class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[]] * self.size

    def get(self, key):
        index = self.hash(key)
        for item in self.table[index]:
            if key == item[0]:
                return item[1]
        raise ValueError("Key not in table")

    def set(self, key, val):
        try:
            index = self.hash(key)
        except TypeError:
            raise

        self.table[index].append((key, val))

    def hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        index = hash % self.size
        return index
