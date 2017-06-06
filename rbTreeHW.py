class rbNode():

    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
        self.parent = None
        self.red = False


def TreeMin(tree):
    while tree.left.val != None:
        tree = tree.left
    return tree


class RBT():

    def __init__(self):
        nil = rbNode(None)
        self.root = nil
        self.nil = nil

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
            print(tree.val)
            # print(tree.val, end='')
            # print(tree.red) for color certification
        if tree.left is not None:
            self.treeprint(tree.left, level + 1)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if x.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self, tree):
        if tree.val is None:
            return
        else:
            self.inorder(tree.left)
            print(tree.val, end=' ')
            self.inorder(tree.right)

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
        z.red = True
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.parent.red == True:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.red == True:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                else:
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.red == True:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                else:
                    z.parent.red = False
                    z.parent.parent.red = True
                    self.left_rotate(z.parent.parent)
        self.root.red = False

    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != self.nil:
            v.parent = u.parent

    def rb_delete(self, z):
        y = z
        y_original_color = y.red
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = TreeMin(z.right)
            y_original_color = y.red
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
            y.red = z.red
        if y_original_color == False:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.red == False:
            if x == x.parent.left:
                w = x.parent.right
                if w.red == True:
                    w.red = False
                    x.parent.red = True
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.red == False and w.right.red == False:
                    w.red = True
                    x = x.parent
                else:
                    if w.right.red == False:
                        w.left.red = False
                        w.red = True
                        self.right_rotate(w)
                        w = x.parent.right
                    w.red = x.parent.red
                    x.parent.red = False
                    w.right.red = False
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.red == True:
                    w.red = False
                    x.parent.red = True
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.red == False and w.left.red == False:
                    w.red = True
                    x = x.parent
                else:
                    if w.left.red == False:
                        w.right.red = False
                        w.red = True
                        self.left_rotate(w)
                        w = x.parent.left
                    w.red = x.parent.red
                    x.parent.red = False
                    w.left.red = False
                    self.right_rotate(x.parent)
                    x = self.root
        x.red = False

    def Nodecount(self):
        total = 0
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
                total = total + 1
                if tree.red == False:
                    nb = nb + 1
                tree = tree.right
        tree = self.root
        while tree.left != self.nil:
            if tree.red == False:
                bh = bh + 1
            tree = tree.left
        print("total = ", end="")
        print(total)
        print("nb = ", end="")
        print(nb)
        print("bh = ", end="")
        print(bh)


def main():
    rbt = RBT()
    node_not_found = []
    f = open("input2.txt", 'r')
    lines = f.readlines()
    for line in lines:
        k = int(line)
        if k > 0:
            rbt.rb_insert(rbNode(k))
        elif k < 0:
            ab_val = abs(k)
            nod_val = rbt.findNode(rbt.root, ab_val)
            if nod_val == 'no_val':
                node_not_found.append(nod_val)
            else:
                rbt.rb_delete(nod_val)
        else:
            rbt.Nodecount()
            rbt.inorder(rbt.root)
            print(" ")
            break

    f.close()
main()
# print("##########")
# rbt = RBT()
# rbt.rb_insert(rbNode(41))
# rbt.treeprint(rbt.root, 0)
# print("##########")
# rbt.rb_insert(rbNode(38))
# rbt.treeprint(rbt.root,0)
# print("##########")
# rbt.rb_insert(rbNode(31))
# rbt.treeprint(rbt.root,0)
# print("##########")
# rbt.rb_insert(rbNode(12))
# rbt.treeprint(rbt.root,0)
# print("##########")
# rbt.rb_insert(rbNode(19))
# rbt.treeprint(rbt.root,0)
# print("##########")
# rbt.rb_insert(rbNode(8))
# rbt.treeprint(rbt.root,0)
# print("##########")
# rbt.rb_delete(rbt.root,19)
# rbt.treeprint(rbt.root,0)
# print("##########")
# print()
