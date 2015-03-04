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

    def _contains(self, key, leaf):
        if leaf is None or leaf.key == key:
            return bool(leaf)
        elif key < leaf.key:
            return self._contains(key, leaf.left)
        else:
            return self._contains(key, leaf.right)

    def contains(self, key):
        return self._contains(key, self.root)

    def insert(self, key):
        if not self.root:
            self.root = Leaf(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, leaf):
        if leaf is None:
            return Leaf(key)
        elif key == leaf.key:
            return Leaf(key, leaf.left, leaf.right)
        elif key < leaf.key:
            return Leaf(leaf.key, self.insert(key, leaf.left), leaf.right)
        else:
            return Leaf(leaf.key, leaf.left, self.insert(key, leaf.right))

    