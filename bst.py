import random
import numpy.random as nprnd

class Leaf(object):
    '''Create leaf.'''
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.key = key
        self.right = right

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.key, self.left.key)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.key, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.key, self.right.key)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.key, r)


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

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.key is None else (
            "\t%s;\n%s\n" % (
                self.root.key,
                "\n".join(self.root._get_dot())
            )
        ))

if __name__ == '__main__':
    import timeit

    def test_contains_easy():
        nums = nprnd.randint(100, size=100)
        t = Tree()
        t.insert(50)
        t.insert(49.5)
        for i in nums:
            t.insert(i)
        t.contains(49.5)

    def test_contains_hard():
        nums = nprnd.randint(100, size=100)
        t = Tree()
        t.insert(50)
        for i in nums:
            t.insert(i)
        t.contains(nums[50])

    print(timeit.Timer("test_contains_easy()", setup="from __main__ import test_contains_easy").timeit(number=1000))
    print(timeit.Timer("test_contains_hard()", setup="from __main__ import test_contains_hard").timeit(number=1000))
