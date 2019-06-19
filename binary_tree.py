class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self, root):
        self.root = Node(root)

    def print_traversal(self, t_type):
        if t_type == 'preorder':
            return self.preorder_traversal(self.root, "")
        elif t_type == 'inorder':
            return self.inorder_traversal(self.root, "")
        elif t_type == 'postorder':
            return self.postorder_traversal(self.root, "")
        else:
            print("Not supported")
            return False

    def preorder_traversal(self, start, traversal):
        # Root -> left -> right
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def postorder_traversal(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal


""" 
        1
      /   \ 
    2       3
   / \     / \
  4   5   6   7
               \
                8
"""

# creating binary tree
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_traversal("preorder"))
#1-2-4-5-3-6-7-8-
print(tree.print_traversal("inorder"))
#4-2-5-1-6-3-7-8-
print(tree.print_traversal("postorder"))
#4-5-2-6-8-7-3-1

#source:
# https://www.youtube.com/watch?v=6oL-0TdVy28&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=34