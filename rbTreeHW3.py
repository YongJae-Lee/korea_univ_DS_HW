class rbNode():

    def __init__(self, newval):
        self.val = newval
        self.parent = None
        self.left = None
        self.right = None
        self.color = "B"


def TreeMin(tree):
    while tree.left.val is not None:
        tree = tree.left
    return tree



class RBT():

    def __init__(self):
        nil = rbNode(None)
        self.root = nil
        self.nil = nil

    def rb_insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "R"
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == "R":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                else:
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                else:
                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self.left_rotate(z.parent.parent)
        self.root.color = "B"


    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def rb_delete(self, z):
        y = z
        yoc = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = TreeMin(z.right)
            yoc = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yoc == "B":
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == "B":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "R":
                    w.color = "B"
                    x.parent.color = "R"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "B" and w.right.color == "B":
                    w.color = "R"
                    x = x.parent
                else:
                    if w.right.color == "B":
                        w.left.color = "B"
                        w.color = "R"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "B"
                    w.right.color = "B"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "R":
                    w.color = "B"
                    x.parent.color = "R"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "B" and w.left.color == "B":
                    w.color = "R"
                    x = x.parent
                else:
                    if w.left.color == "B":
                        w.right.color = "B"
                        w.color = "R"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "B"
                    w.left.color = "B"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "B"
    def inorder(self, tree):
        if tree.val is None:
            return
        else:
            self.inorder(tree.left)
            print(tree.val, end=' ')
            print(tree.color) #for color certification
            self.inorder(tree.right)
    def findNode(self, tree, x):
        if tree != self.nil:
            if x < tree.val:
                return self.findNode(tree.left, x)
            elif x > tree.val:
                return self.findNode(tree.right, x)
            else:
                return tree
        else:
            return 'no_val'
    def treeprint(self, tree, level):
        if tree.right is not None:
            self.treeprint(tree.right, level + 1)
        if tree.val != None:
            for i in range(level):
                print('   ', end='')
            # print(tree.val)
            print(tree.val, end='')
            print(tree.color) #for color certification
        if tree.left is not None:
            self.treeprint(tree.left, level + 1)
    def Nodecount(self):
        nb = 0
        bh = 0
        tree = self.root
        stk = []
        while len(stk) != 0 or tree.val != None:
            if tree.val != None:
                stk.append(tree)
                tree = tree.left
            else:
                tree = stk.pop()
                if tree.color == "B":
                    nb += 1
                tree = tree.right
        tree = self.root
        while tree.left != self.nil:
            if tree.color == "B":
                bh += 1
            tree = tree.left
        print("nb = ", end="")
        print(nb)
        print("bh = ", end="")
        print(bh)

def main():
    rbt = RBT()
    node_not_found = 0
    insert = 0
    deleted = 0
    f = open("test05.txt", 'r')
    lines = f.readlines()
    for line in lines:
        k = int(line)
        if k > 0:
            rbt.rb_insert(rbNode(k))
            insert += 1
        elif k < 0:
            ab_val = abs(k)
            nod_val = rbt.findNode(rbt.root, ab_val)
            if nod_val == 'no_val':
                node_not_found += 1
            else:
                rbt.rb_delete(nod_val)
                deleted += 1
        else:
            print("filename = ", end="")
            print(f.name)
            print("total = ", end="")
            print(insert - deleted)
            print("insert = ", end="")
            print(insert)
            print("deleted = ", end="")
            print(deleted)
            print("miss = ", end="")
            print(node_not_found)
            rbt.Nodecount()
            rbt.inorder(rbt.root)
            print(" ")
            break
    # rbt.treeprint(rbt.root,0)
    f.close()
main()