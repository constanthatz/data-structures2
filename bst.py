import random
from Queue import Queue
import timeit
import subprocess
import sys
import os


class Leaf(object):
    '''Create leaf.'''
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.key = key
        self.right = right
        self.parent = parent

    def __repr__(self):
        if self.parent:
            parent = self.parent.key
        else:
            parent = None
        if self.left:
            left = self.left.key
        else:
            left = None
        if self.right:
            right = self.right.key
        else:
            right = None
        return "parent = {}, left = {} , right = {}".format(parent, left, right)

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.parent is not None:
            yield "\t%s -> %s;" % (self.key, self.parent.key)
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
            return leaf
        elif key < leaf.key:
            return self._contains(key, leaf.left)
        else:
            return self._contains(key, leaf.right)

    def contains(self, key):
        return bool(self._contains(key, self.root))

    def insert(self, key):
        if not self.root:
            self.root = Leaf(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, leaf):
        if key == leaf.key:
            return leaf
        elif key < leaf.key:
            if leaf.left:
                return self._insert(key, leaf.left)
            else:
                leaf.left = Leaf(key, parent=leaf)
                return leaf.left
        else:
            if leaf.right:
                return self._insert(key, leaf.right)
            else:
                leaf.right = Leaf(key, parent=leaf)
                return leaf.right

    def _find_replacement(self, leaf):
        current = leaf
        while current.right:
            current = current.right
        return current

    def _remove_node(self, leaf, replacement_leaf=None):
        if leaf.parent:
            if leaf.parent.left == leaf:
                leaf.parent.left = leaf.left
            else:
                leaf.parent.right = leaf.right
        if replacement_leaf:
            replacement_leaf.parent = leaf.parent

    def delete(self, target):
        self._delete(target, self.root)

    def _delete(self, target, start):
        leaf = self._contains(target, start)
        if leaf:
            if leaf.left and leaf.right:
                successor = self._find_replacement(leaf.left)
                leaf.key = successor.key
                self._delete(successor.key, successor)
            elif leaf.left:
                self._remove_node(leaf, leaf.left)
            elif leaf.right:
                self._remove_node(leaf, leaf.right)
            else:
                self._remove_node(leaf)

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
            return self._depth(self.root)[0]

    def _depth(self, leaf):
        if leaf is None:
            return 0, 0, 0
        else:
            depthL = self._depth(leaf.left)[0]
            depthR = self._depth(leaf.right)[0]
        return max([depthL, depthR]) + 1, depthL, depthR

    def balance(self, start=None):
        if not start:
            return self._balance(self.root)
        else:
            return self._balance(start)

    def _balance(self, leaf):
        depthL, depthR = self._depth(leaf)[1:3]
        return depthL - depthR

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, leaf):
        if leaf is None:
            return
        for val in self._in_order(leaf.left):
            yield val
        yield leaf.key
        for val in self._in_order(leaf.right):
            yield val

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, leaf):
        if leaf is None:
            return
        yield leaf.key
        for val in self._pre_order(leaf.left):
            yield val
        for val in self._pre_order(leaf.right):
            yield val

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, leaf):
        if leaf is None:
            return
        for val in self._post_order(leaf.left):
            yield val
        for val in self._post_order(leaf.right):
            yield val
        yield leaf.key

    def breadth_first_traversal(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            leaf = q.get()
            yield leaf.key
            if leaf.left:
                q.put(leaf.left)
            if leaf.right:
                q.put(leaf.right)

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.root.key is None else (
            "\t%s;\n%s\n" % (
                self.root.key,
                "\n".join(self.root._get_dot())
            )
        ))

    def graph(self, file_name):
        t = subprocess.Popen(["dot", "-Tpng"],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        png_data = t.communicate(self.get_dot())
        with open('{}.png'.format(file_name), 'w') as png_file:
            png_file.write(png_data[0])
        os.system('open {}.png'.format(file_name))

    def nuclear_option(self):
        generator = self.in_order()
        num = []
        while True:
            try:
                num.append(generator.next())
            except StopIteration:
                self.root = self._nuclear_option(num, 0, len(num)-1, None)
                return

    def _nuclear_option(self, num, begin, end, parent):
        if begin > end:
            return None
        midPoint = (begin+end)//2
        root = Leaf(num[midPoint], parent=parent)
        root.left = self._nuclear_option(num, begin, midPoint-1, root)
        root.right = self._nuclear_option(num, midPoint+1, end, root)
        return root

    def avl_insert(self, key):
        if not self.root:
            self.root = Leaf(key)
        else:
            self._insert(key, self.root)
            # self.graph('1_Pre_AVL_Balance')
            bal = self.balance(self.root)
            if bal > 1 or bal < -1:
                self._avl_balance(self.root, bal)

    def _avl_balance(self, current, bal):
        while not (bal == 1 or bal == -1):
            if bal > 1:
                current = current.left
                bal = self.balance(current)
            else:
                current = current.right
                bal = self.balance(current)
        parent = current.parent

        while parent:
            if current is parent.left:
                if self._balance(parent) == 2:
                    if self._balance(current) == -1:
                        self._rotate_left(current)
                        # self.graph('2_Left_Left')
                    self._rotate_right(parent)
                    # self.graph('3_Left_Right')

                    return
                if self._balance(parent) == -1:
                    return
            else:
                if self._balance(parent) == -2:
                    if self._balance(current) == 1:
                        self._rotate_right(current)
                        # self.graph('4_Right_Right')

                    self._rotate_left(parent)
                    # self.graph('5_Right_Left')

                    return
                if self._balance(parent) == 1:
                    return
            current, parent = parent, parent.parent

    def _rotate_left(self, leaf):
        leaf.right.parent = leaf.parent
        try:
            if leaf is leaf.parent.left:
                leaf.parent.left = leaf.right
            else:
                leaf.parent.right = leaf.right
        except:
            self.root = leaf.right
        leaf.right.left, leaf.right, leaf.parent = leaf, leaf.right.left, leaf.right
        try:
            leaf.right.parent = leaf
        except:
            pass

    def _rotate_right(self, leaf):
        leaf.left.parent = leaf.parent
        try:
            if leaf is leaf.parent.right:
                leaf.parent.right = leaf.left
            else:
                leaf.parent.left = leaf.left
        except:
            self.root = leaf.left
        leaf.left.right, leaf.left, leaf.parent = leaf, leaf.left.right, leaf.left
        try:
            leaf.left.parent = leaf
        except:
            pass


if __name__ == '__main__':

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

    if len(sys.argv) > 1:
        if sys.argv[1] == 'con':
            nums = []
            nums.append(range(0, 5))
            nums.append(range(0, 50))
            nums.append(range(0, 500))

            for num in nums:
                T_easy = Tree(makeBalancedTree(num))
                T_hard = Tree()
                for i in num:
                    T_hard.insert(i)

                def test_contains_easy():
                    T_easy.contains(num[-1])

                def test_contains_hard():
                    T_hard.contains(num[-1])

                best_case = '{:10.10f}s :Best Case,  Balanced,   Leaves {},  Depth {}'
                worst_case = '{:10.10f}s :Worst Case, Unbalanced, Leaves {},  Depth {}'
                time_easy = timeit.Timer(
                    "test_contains_easy()",
                    setup="from __main__ import test_contains_easy").timeit(
                    number=10000)
                time_hard = timeit.Timer(
                    "test_contains_hard()",
                    setup="from __main__ import test_contains_hard").timeit(
                    number=10000)

                print(best_case.format(time_easy, len(num), T_easy.depth()))
                print(worst_case.format(time_hard, len(num), T_hard.depth()))
                print('{} times slower'.format(float(time_hard)/float(time_easy)))
                print('\n')
        elif sys.argv[1] == 'avl':
            nums = []
            nums.append(range(0, 5))
            nums.append(range(0, 50))
            nums.append(range(0, 500))

            for num in nums:
                T = Tree()

                def test_avl_insert():
                    for i in num:
                        T.avl_insert(i)

                case = '{:10.10f}s : Leaves {}'
                time = timeit.Timer(
                    "test_avl_insert()",
                    setup="from __main__ import test_avl_insert").timeit(
                    number=100)

                print(case.format(time, len(num)))
                print('\n')
