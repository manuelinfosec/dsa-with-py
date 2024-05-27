# Binary Trees

A binary tree is a tree data structure in which each node has at most two children, which are referred to as left child and right child.
<pre>
                    1           -> Root
                 /     \        
                2       3     -> Parent
             /     \   
            4       5           -> Children
</pre>
- The very bottom of the tree are the leaves.
- The depth of the tree is the number of levels traversed.

## Types of Binary Tree
- Complete Binary Tree: In this binary tree, ever level, except possible the lasts, is completely filled, and all nodes in the last level are as far left as possible.
<pre>
                    1           -> Root
                 /     \        
                2        3     -> Parent
              /      
             4                  -> Children
</pre>
- Full Binary Tree: A full binary tree (sometimes referred to as a **proper** or **plane** binary tree) is a tree in which every node has either 0 or 2 children.
<pre>
                1           -> Root
             /     \        
            2        3     -> Parent
          /  \     /   \
         4     5  6     7   -> Children
</pre>
## Traversing A Tree
Tree Traversal is a process of visiting (checking and/or updating) each node in a tree data structure, exactly once. Trees may be traversed in **depth-first** or **breadth-first order.**

Note: Trees cannot be traversed in a linear fashion.

### Depth-First traversal:
The depth-first traversal invlude the pre-order, in-order and post order traversals. Details:

1. Pre-order Traversal: Root -> Left -> Right
    - Check if the current node is empty/null
    - Display the data part of the root (or current node).
    - Traverse the left subtree by recuresively calling the pre-order function.
    - Traverse the right subtree by recursively calling the pre-order function.
<pre>    
                 F           -> Root
             /      \        
            B         G     -> Parent
          /  \          \
         A     D        I   -> Children
             /  \      /
            C    E    H      -> Grand Children

        Output: F-B-A-D-C-E-G-I-H-
</pre>
2. In-order Traversal: Left -> Root -> Right
    - Check if the current node is empty/null
    - Traverse the left subtree by recursively calling the in-order function.
    - Display the data part of the root (or current node).
    - Traverse the right subtree by recursively calling the in-order function.
<pre>
                 F           -> Root
             /      \        
            B         G     -> Parent
          /  \          \
         A     D        I   -> Children
             /  \      /
            C    E    H      -> Grand Children
        Output: A-B-C-D-E-F-G-H-I-
</pre>

3. Post-order Traversal: Left -> Right -> Root
- Check if the current node in empty/null
- Traverse the left subtree by recursively calling the post-order function.
- Traverse the right subtree by recursively calling the post-order function.
- Display the data part of the root (or current node).
<pre>
                 F           -> Root
             /      \        
            B         G     -> Parent
          /  \          \
         A     D        I   -> Children
             /  \      /
            C    E    H      -> Grand Children
        Output: A-C-E-D-B-H-I-G-F-
</pre>
