class Node:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
def lowestcommon(root,data1,data2):
        if root is None:
            return None

        if root.data < data1 and root.data < data2 :
            return lowestcommon(root.rchild, data1, data2)
        
        if root.data > data1 and root.data > data2:
             return lowestcommon(root.lchild, data1, data2)
        
        return root



