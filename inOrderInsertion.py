class Node:
    def __init__(self,key):
        self.key = key 
        self.lchild = None
        self.rchild = None

postfixprecedence ={
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '/': 2,
    '*': 2
}
def postfixNumStackConvertsion(infix):
    stackSign = []       
    postFixNumber = []   
    for char in infix:
        if char not in postfixprecedence:
            postFixNumber.append(char)
        else:
            if len(stackSign) == 0:
                stackSign.append(char)
            else:
                if char == '(': 
                    stackSign.append(char)
                elif char == ')':
                    while stackSign[len(stackSign)-1] != '(':
                        postFixNumber.append(stackSign.pop())
                    stackSign.pop()
                elif postfixprecedence[char] > postfixprecedence[stackSign[len(stackSign)-1]]:
                    stackSign.append(char)
                else:
                    while len(stackSign) != 0:
                        if stackSign[len(stackSign)-1] == '(':
                            break
                        postFixNumber.append(stackSign.pop())
                    stackSign.append(char)
    while len(stackSign)  != 0:
        postFixNumber.append(stackSign.pop())
    return postFixNumber 

def buildExpressionTree(infix):
    newlistInfix = postfixNumStackConvertsion(infix)
    stack = []
    for token in newlistInfix:
        if token not in postfixprecedence:
            node = Node(token)
            stack.append(node)
        else:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack

print(postfixNumStackConvertsion("(5+3)*6"))
print(buildExpressionTree("(5+3)*6"))