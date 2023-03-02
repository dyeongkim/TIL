# B-트리 구현
class Node():
    def __init__(self,leaf=False):
        self.leaf = leaf
        self.key = []
        self.children = []

class BTree():
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def search(self, k, x=None):
        if x is None :
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else :
            return self.search(k, x.children[i])
            
    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t)-1:
            s = Node()
            self.root = s
            s.children.append(r)
            self.split_shild(s,0)
            self.insert_nonfull(s,k)
        else:
            self.insert_nonfull(r,k)

    def insert_nonfull(self, x, k):
        i = len(x.keys) -1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.hild[i].keys) == (2 * self.t)-1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(leaf=y.leaf)

        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t -1])
        
        z.keys = y.keys[t:(2 * t -1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.child = y.child[t: (2 * t)]
            y.child = y.child[0:(t - 1)]

