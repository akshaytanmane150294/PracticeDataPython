"""Finding Min element in Binary search Tree"""

def findingMin(root):
    currentnode = root
    if currentnode.lchild == None:
        return currentnode.lchild
    else:
        return findingMin(currentnode.lchild)


def nonrecusivefindingMineEle(root):
    currentnode = root
    if currentnode.lchild == None:
        return currentnode.lchild
    while currentnode.lchild != None:
        currentnode = currentnode.lchild
    return currentnode.lchild


"""Finding Max element in Binary search Tree"""
def findingMax(root):
    currentNode = root
    if currentNode.rchild == None:
        return currentNode.rchild
    else:
        return findingMax(currentNode.rchild)

def nonrecursiveFindigMax(root):
    currentNode = root
    if currentNode.rchild == None:
        return currentNode.rchild
    while currentNode.rchild != None:
        currentNode = currentNode.rchild
    return currentNode.rchild
