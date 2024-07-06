
import json
class BSTreeNode:
    value : any = None
    left = None
    right = None
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
    


class BSTree:
    root = None
    def __init__(self, root: BSTreeNode =None) -> None:
        self.root = root

    def insert(self,value) -> None:
        if(self.root == None):
            self.root = BSTreeNode(value)
        else:
            node = self.root
            while (True):
                if(value > node.value):
                    if(node.right == None):
                        node.right = BSTreeNode(value)
                        break
                    node = node.right
                else:
                    if(node.left == None):
                        node.left = BSTreeNode(value)
                        break
                    node = node.left

    def lookup(self,value) -> None | BSTreeNode:
        node = self.root
        while(node is not None):
            if(node.value == value):
                return node
            if(value > node.value):
                node = node.right
            else:
                node = node.left
        return None
    
    def remove(self,value) -> None | BSTreeNode:
        if(self.root is None):
            return None
        
        node = self.root
        parent = None
        #  Find node
        while(node is not None):
            if(node.value == value):
                break
            if(value > node.value):
                node = node.right
            else:
                node = node.left
            parent = node
        
        #  If not found return
        if(node is None):
            return None
        
        #  Keep ref to node
        key_node = node

        # Case 1 right emtpy
        if(node.right is None):
            # Sub case parent not emtpy
            if(parent is not None):
                # Replace parent with child node
                if(node.value > parent.value):
                    parent.right = node.left
                else:
                    parent.left = node.left
            # Parent empty means root node
            else: 
               # Reasign root with as left 
               self.root =  node.left 
        else:
            # Case 2 Right not emtpy
            # Keep track of sub parent to None
            sub_parent = parent
            node = node.right

            #  Drill down left
            while(node.left is not None):
                sub_parent = node
                node = node.left
            
            # if Parent not empty
            if(parent is not None):
                # Replace parent key_node with node
                if(node.value > parent.value):
                    parent.right = node    
                else:
                    parent.left = node
            else:
                # If Parent empty must be root node
                self.root = node
            
            # if parent is not sub parent
            if(parent is not sub_parent):
                    sub_parent.left = node.right

            # Reassign node values
            node.left = key_node.left
            node.right = key_node.right


                


                    


def traverse(tree: BSTree):
    tree.left = None if (tree.left == None) else traverse(tree.left)
    tree.right = None if (tree.right == None) else traverse(tree.right)
    print(tree.value)
    return tree


tree = BSTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)



# print(tree.lookup(20).value    if tree.lookup(20)   is not None else None)
# print(tree.lookup(21).value    if  tree.lookup(21)  is not None else None)
# print(tree.lookup(9).value     if  tree.lookup(9)   is not None else None)
# print(tree.lookup(81).value    if  tree.lookup(81)  is not None else None)
# print(tree.lookup(170).value   if  tree.lookup(170) is not None else None)

    #  9
#   4     20
# 1  6  15  170
#      13
#         14    
# 
# 
#      9
#   4     20
# 1  6  13  170
#          14     


tree.insert(13)
tree.insert(14)
tree.remove(15)

traverse(tree.root)
