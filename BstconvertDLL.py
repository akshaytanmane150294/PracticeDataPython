class Node:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insertion(self,root):
        if not self.key:
            self.key = root
        
        if self.key > root:
            if self.lchild:
                self.lchild.insertion(root)
            else:
                self.lchild = Node(root)
        else:
            if self.rchild:
                self.rchild.insertion(root)
            else:
                self.rchild = Node(root)
        

def BstconvertoDLL(root):
    def bstToDllHelper(node):
        nonlocal prev

        if node is None:
            return None

        lefthead = bstToDllHelper(node.lchild)
        
        if prev is not None:
            prev.right =  node.key
            node.left = prev.key

        prev = node

        righthead = bstToDllHelper(node.rchild)

        if righthead is not None:
            righthead.left = node.key
            node.right = righthead

        if lefthead is None:
            return  node
        else:
            return lefthead
        
    prev = None 
    head = bstToDllHelper(root)

    while head.lchild is not None:
        head = head.lchild
    while prev.rchild is not None:
        prev = prev.rchild

    head.lchild = prev
    prev.rchild = head

    return head

obj = Node(10)
lst = [6, 3, 98, 1, 7, 5, 4, 96]
for i in lst:
	obj.insertion(i)
      
print(obj.insertion)
print(BstconvertoDLL(obj.insertion))
     
    

        

