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

    def insert(self, value, compare=value):
        if self.root is None:
            self.root = Leaf(value=value)
