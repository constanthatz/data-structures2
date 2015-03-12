class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[]] * self.size


    def get(key):
        pass

    def set(key, val):
        pass

    def hash(key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash