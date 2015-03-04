class Leaf(object):
    '''Create leaf.'''
    def __init__(self, left=None, value=None, right=None):
        self.left = left
        self.value = value
        self.right = right


class Tree(object):
    '''Create tree'''
    def __init__(self, root=None):
        self.root = root

    def search(self, value, leaf):
        if leaf is None or leaf.value == value:
            return leaf
        elif value < leaf.key:
            return search(value, leaf.left)
        else:
            return search(value, leaf.right)

    def insert(self, value):

        if node is None:
            self.root = Leaf(value=value)
        elif 
