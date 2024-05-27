# an object representing a node
class Node:
    def __init__(self, value):
        self.value = value       # node value
        self.left = None         # node left child
        self.right = None        # node right child

    def __repr__(self):
        return f"{self.value}"

# an object representing the entire tree
class BinaryTree:
    def __init__(self, root): 
        self.root = Node(root)  # tree root   
    
    # print tree in a traversal order
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print("Pre-Order Trasversal:", end=" ")
            return self.pre_order(tree.root, "")
        elif traversal_type == "inorder":
            print("In-Order Trasversal:", end=" ")
            return self.in_order(tree.root, "")
        elif traversal_type == "postorder":
            print("Post-Order Trasversal:", end=" ")
            return self.post_order(tree.root, "")
        else:
            print(f"Traversal type {str(traversal_type)} is not supported...")

    def pre_order(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def in_order(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order(start.right, traversal)
        return traversal
    
    def post_order(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


tree = BinaryTree("F")
tree.root.left = Node("B")
tree.root.right = Node("G")
tree.root.left.left = Node("A")
tree.root.left.right = Node("D")
tree.root.left.right.left = Node("C")
tree.root.left.right.right = Node("E")
tree.root.right.right = Node("I")
tree.root.right.right.left = Node("H")


if __name__ == "__main__":
    print(tree.print_tree("preorder"))