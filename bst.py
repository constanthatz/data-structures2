class Leaf(object):
    '''Create leaf.'''
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.key = key
        self.right = right


class Tree(object):
    '''Create tree'''
    def __init__(self, root=None):
        self.root = root

    def search(self, key, leaf):
        if leaf is None or leaf.key == key:
            return leaf
        elif key < leaf.key:
            return self.search(key, leaf.left)
        else:
            return self.search(key, leaf.right)

    def contains(self, key):
        result = self.search(key, self.root)
        if result is None:
            return False
        else:
            return True

    def insert(self, key, leaf):
        if leaf is None:
            return Leaf(key)
        elif key == leaf.key:
            return Leaf()
        elif key < leaf.key:
            return Leaf(leaf.key, self.insert(key, leaf.left), leaf.right)
        else:
            return Leaf(leaf.key, leaf.left, self.insert(key, leaf.right))
