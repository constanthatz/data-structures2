class Leaf(object):
    '''Create leaf.'''
    def __init__(self, left=None, key=None, value=None, right=None):
        self.left = left
        self.key = key
        self.value = value
        self.right = right


class Tree(object):
    '''Create tree'''
    def __init__(self):
        self.root = None
