class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):  # t = grado mínimo (m//2)
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(y.leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Insert elements
elements = [22,15,1,12,4,20,13,30,18,5,6,29,11,27,7,28,10,14,21,2,19,3]
btree = BTree(3)  # Para m=5, grado mínimo t = ceil(5/2) = 3
for elem in elements:
    btree.insert(elem)

btree.print_tree()
