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
        if key == leaf.key:
            return
        elif key < leaf.key:
            if leaf.left:
                self._insert(key, leaf.left)
            else:
                leaf.left = Leaf(key)
        else:
            if leaf.right:
                self._insert(key, leaf.right)
            else:
                leaf.right = Leaf(key)

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
            return max(self._depth(self.root))+1

    def _depth(self, leaf):
        if leaf is None:
            return 0
        else:
            depthL = self._depth(leaf.left)
            depthR = self._depth(leaf.right)
        if leaf == self.root:
            return depthL, depthR
        return max([depthL, depthR]) + 1

    def balance(self):
        depthL, depthR = self._depth(self.root)
        return depthL - depthR

if __name__ == '__main__':
    t = Tree()
    t.insert(10)
    t.insert(15)
    t.insert(5)
    print(t.size)
