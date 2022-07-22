class Tree():
    def __init__(self, key):
        self.node = key
        self.left = None
        self.right = None

    def __str__(self):
            return '{} ({}, {})'.format(self.node, str(self.left), str(self.right))

    def add(self, local, key):
        if local.node is None:
            self.node = Tree(key)
        else:
            if key == local.node:
                return local.node
            elif key > local.node:
                if local.right is None:
                    local.right  = Tree(key)
                else:
                    self.add(local.right, key)
            elif key<local.node:
                if local.left is None:
                    local.left  = Tree(key)
                else:
                    self.add(local.left, key)

def create_node(numbers):
    tree = Tree(numbers[0])
    for num in numbers[1:]:
        tree.add(tree,num)
    print(tree)

create_node([5,3,4,5,3,1,10,12,11,14,13])
