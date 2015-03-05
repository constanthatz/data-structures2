import random
import numpy.random as nprnd
from Queue import Queue



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

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.key is None else (
            "\t%s;\n%s\n" % (
                self.root.key,
                "\n".join(self.root._get_dot())
            )
        ))

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, leaf):
        if leaf is None:
            return
        for val in self._in_order(leaf.left):
            yield val
        yield(leaf.key)
        for val in self._in_order(leaf.right):
            yield val

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, leaf):
        if leaf is None:
            return
        yield(leaf.key)
        for val in self._in_order(leaf.left):
            yield val
        for val in self._in_order(leaf.right):
            yield val

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, leaf):
        if leaf is None:
            return
        for val in self._in_order(leaf.left):
            yield val
        for val in self._in_order(leaf.right):
            yield val
        yield(leaf.key)

    def breadth_first_traversal(self):
        q = Queue()
        q.put(self.root)
        while not q.empty:
            leaf = q.get()
            yield leaf.key
            if leaf.left:
                q.put(leaf.left)
            if leaf.right:
                q.put(leaf.right)






if __name__ == '__main__':
    import timeit

    nums = []
    nums.append(range(0, 5))
    nums.append(range(0, 50))
    nums.append(range(0, 500))

    for item in nums:
        num = item

        def makeBalancedTree(num):
            return makeBalance(num, 0, len(num)-1)

        def makeBalance(num, begin, end):
            if begin > end:
                return None
            midPoint = (begin+end)//2
            root = Leaf(num[midPoint])
            root.left = makeBalance(num, begin, midPoint-1)
            root.right = makeBalance(num, midPoint+1, end)
            return root

        T_easy = Tree(makeBalancedTree(num))
        T_hard = Tree()
        for i in num:
            T_hard.insert(i)

        def test_contains_easy():
            T_easy.contains(num[-1])

        def test_contains_hard():
            T_hard.contains(num[-1])

        best_case = '{:10.10f} s : Best Case,  Balanced,   Leaves {},  Depth {}'
        worst_case = '{:10.10f} s : Worst Case, Unbalanced, Leaves {},  Depth {}'
        time_easy = timeit.Timer(
            "test_contains_easy()",
            setup="from __main__ import test_contains_easy").timeit(number=10000)
        time_hard = timeit.Timer(
            "test_contains_hard()",
            setup="from __main__ import test_contains_hard").timeit(number=10000)

        print(best_case.format(time_easy, len(num), T_easy.depth()))
        print(worst_case.format(time_hard, len(num), T_hard.depth()))
        print('{} times slower'.format(float(time_hard)/float(time_easy)))
        print('\n')


    