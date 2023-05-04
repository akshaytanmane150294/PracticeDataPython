class Node:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
def BstorNot(root):
        if root is None:
            return 0
        
        if root.lchild != None and root.lchild.key > root.key:
            return 0
        
        if root.rchild != None and root.rchild.key < root.key:
             return 0
        
        if not BstorNot(root.lchild) and not BstorNot(root.rchild):
             return 0
        return 1
             

        