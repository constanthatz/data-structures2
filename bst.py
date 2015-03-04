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
            self.root = self._insert(key, self.root)

    def _insert(self, key, leaf):
        if leaf is None:
            return Leaf(key)
        elif key == leaf.key:
            return Leaf(key, leaf.left, leaf.right)
        elif key < leaf.key:
            return Leaf(leaf.key, self._insert(key, leaf.left), leaf.right)
        else:
            return Leaf(leaf.key, leaf.left, self._insert(key, leaf.right))

    def size(self):
        if not self.root:
            return 0
        else:
            return self._size(self.root, 1)

    def _size(self, leaf, count):
        if leaf.left:
            count += 1
            count = self._size(leaf.left, count)
        if leaf.right:
            count += 1
            count = self._size(leaf.right, count)
        return count

    def depth(self):
        if not self.root:
            return 0
        else:
            return self._depth(self.root)

    def _depth(self, leaf):
        if leaf is None:
            return 0
        else:
            depthL = self._depth(leaf.left)
            depthR = self._depth(leaf.right)
        return max([depthL, depthR]) + 1

if __name__ == '__main__':
    t = Tree()
    t.insert(10)
    t.insert(15)
    t.insert(5)
    print(t.size)
