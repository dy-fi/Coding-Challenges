# Given a binary search tree containing integers and a target integer, 
# come up with an efficient way to locate two nodes in the tree whose
# sum is equal to the target value.

class Node():
    def __init__(self, val:int, left:Node=None, right:Node=None):
        self.val = int
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self, root:Node):
        self.root = root

def bin_search(root:Node, target:int) -> bool:
    
    while True:
        if root.val > target:
            if root.left: return bin_search(root.left, target)
            else: break
        elif root.val < target:
            if root.right: return bin_search(root.right, target) 
            else: break
        else:
            return True
    
    return False

def two_sum_bin(target:int, root:Node) -> (int, int):
    curr1 = root

    compliment = target - curr1.val
    b = bin_search(root, compliment)
    
    if b: return (curr1.val, compliment)
    
    if root.left:
        result = two_sum_bin(target, root.left)
        if result: return result
    
    elif root.right:
        result = two_sum_bin(target, root.right)
        if result: return result
    
    else:
        return None


# count depth on trees from the left and right of root
def superbalanced(root:Node, v=0, v2=0) -> bool:
    if root.left:
        superbalanced(root.left, v+1)
    if root.right:
        superbalanced(root.right, v2+1)
    else:
        if v == v2: return True
        else: return False