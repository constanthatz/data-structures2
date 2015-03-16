class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for i in xrange(size)]

    def get(self, key):
        index = self.hash(key)
        for item in self.table[index]:
            if key == item[0]:
                return item[1]
        raise ValueError("Key not in table")

    def set(self, key, val):
        index = self.hash(key)
        for item_num, item in enumerate(self.table[index]):
            if key == item[0]:
                self.table[index][item_num] = (key, val)
                return
        self.table[index].append((key, val))

    def hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.size

    def bin_size(self):
        print [len(bin_list) for bin_list in self.table]
