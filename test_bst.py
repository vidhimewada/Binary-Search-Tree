import bst
import sys
import traceback
import exceptions

# Entry point of program - Testing BST functionalities
if __name__ == '__main__':
    treeList = [5, 3, 4, 10, 8, 2, 1, 7, 9, 6, 12, 11, 13]

    '''
                    5            
               /        \
              3         10
            /  \       /   \
           2    4     8     12 
         /           / \    / \
        1           7   9  11  13
                   /
                  6 
    '''

    tree = bst.BSTree()

    # Insert values into tree
    try:
        for i in treeList:
            tree.insert(i)
    except exceptions.InsertNodeException as ex:
        print(ex)
        sys.exit()

    try:
        # InOrder Traversal - Sorted Order
        tree.printTree("INORDER")

        # PreOrder Traversal
        tree.printTree("PREORDER")

        # PostOrder Traversal
        tree.printTree("POSTORDER")
    except exceptions.PrintTreeException as ex:
        print(ex)
        sys.exit()

    # Delete a leaf node - 1
    try:
        tree.delete(1)
        tree.printTree("INORDER")

        tree.delete(3)
        tree.printTree("INORDER")

        tree.delete(12)
        tree.printTree("INORDER")

        tree.delete(5)
        tree.printTree("INORDER")

        # Test deletion with empty tree
        # newTree = bst.BSTree()
        # newTree.delete(1)
    except exceptions.DeleteNodeException as ex:
        print(ex)
        sys.exit()
    except exceptions.PrintTreeException as ex:
        print(ex)
        sys.exit()
