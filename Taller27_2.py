class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None  # Para enlazar hojas

class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode(True)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BPlusTreeNode(False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.leaf:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            child = node.children[i]
            if len(child.keys) == self.order - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        order = self.order
        child = parent.children[i]
        mid_index = order // 2
        new_child = BPlusTreeNode(child.leaf)

        if child.leaf:
            new_child.keys = child.keys[mid_index:]
            child.keys = child.keys[:mid_index]
            new_child.next = child.next
            child.next = new_child
            parent.keys.insert(i, new_child.keys[0])
            parent.children.insert(i + 1, new_child)
        else:
            parent.keys.insert(i, child.keys[mid_index])
            new_child.keys = child.keys[mid_index + 1:]
            child.keys = child.keys[:mid_index]
            new_child.children = child.children[mid_index + 1:]
            child.children = child.children[:mid_index + 1]
            parent.children.insert(i + 1, new_child)

    def print_tree(self):
        def _print(node, level=0):
            print("Level", level, ":", node.keys)
            if not node.leaf:
                for child in node.children:
                    _print(child, level + 1)
        _print(self.root)

    def print_leaves(self):
        # Recorrido por las hojas
        node = self.root
        while not node.leaf:
            node = node.children[0]
        print("Leaves:")
        while node:
            print(node.keys, end=" -> ")
            node = node.next
        print("None")

# Insert elements
elements = [22,15,1,12,4,20,13,30,18,5,6,29,11,27,7,28,10,14,21,2,19,3]
bptree = BPlusTree(order=5)
for elem in elements:
    bptree.insert(elem)

bptree.print_tree()
bptree.print_leaves()
