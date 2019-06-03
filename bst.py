import node
import exceptions


class BSTree:
    """
        Class to represent Binary Search Tree
    """

    # Default Constructor
    def __init__(self):
        self.root = None

    # Public Method to perform Inorder Traversal
    def inOrderTraversal(self, nodeIn):
        # Base Case
        if not nodeIn:
            return

        # Recursion Case
        self.inOrderTraversal(nodeIn.left)
        print(nodeIn.val, end=" ")
        self.inOrderTraversal(nodeIn.right)

    # Public Method to perform Preorder Traversal
    def preOrderTraversal(self, nodeIn):
        # Base Case
        if not nodeIn:
            return

        # Recursion Case
        print(nodeIn.val, end=" ")
        self.preOrderTraversal(nodeIn.left)
        self.preOrderTraversal(nodeIn.right)

    # Public Method to perform Postorder Traversal
    def postOrderTraversal(self, nodeIn):
        # Base Case
        if not nodeIn:
            return

        # Recursion Case
        self.postOrderTraversal(nodeIn.left)
        self.postOrderTraversal(nodeIn.right)
        print(nodeIn.val, end=" ")

    # Public Method to print Tree as per traversal method
    def printTree(self, traversalMethodIn):
        if traversalMethodIn.upper() == "INORDER":
            print("Inorder Traversal :")
            self.inOrderTraversal(self.root)
            print("\n")
        elif traversalMethodIn.upper() == "PREORDER":
            print("Preorder Traversal :")
            self.preOrderTraversal(self.root)
            print("\n")
        elif traversalMethodIn.upper() == "POSTORDER":
            print("Postorder Traversal :")
            self.postOrderTraversal(self.root)
            print("\n")
        else:
            raise exceptions.PrintTreeException("Exception :: Incorrect Traversal Method (Inorder, Preorder, Postorder) --> Given input is = " + traversalMethodIn)

    # Public method to insert node in a tree -
    # Returns True - if value inserted successfully,
    # Raises exception - if there is duplicate value
    def insert(self, valIn):
        if not self.root:
            # Root is not set - so create root node calling Node constructor
            self.root = node.TreeNode(valIn)
        else:
            # Invoke insert from Node class - Root at starting node
            if not self._insert(valIn, self.root):
                raise exceptions.InsertNodeException("Exception :: Failed to insert duplicate values in BST.")

    # Private method to insert new node recursively
    def _insert(self, valIn, parentIn):
        # Recursive approach
        if parentIn.val < valIn:
            # Check right
            if not parentIn.right:
                parentIn.right = node.TreeNode(valIn)
                parentIn.right.parent = parentIn
                return True
            else:
                # Traverse right
                return self._insert(valIn, parentIn.right)
        elif parentIn.val > valIn:
            # Check left
            if not parentIn.left:
                parentIn.left = node.TreeNode(valIn)
                parentIn.left.parent = parentIn
                return True
            else:
                # Traverse left
                return self._insert(valIn, parentIn.left)
        # val matches with existing node val
        return False

    # Private method to delete leaf node
    def _delLeafNode(self, delNodeIn, parentIn):
        if not parentIn:
            # Root of tree is deleted
            self.root = None
        elif parentIn.val < delNodeIn.val:
            # To delete right child node
            parentIn.right = None
        else:
            # To delete left child node
            parentIn.left = None
        return True

    # Private method to delete node with one child
    def _delSingleChildNode(self, delNodeIn, parentIn):
        if not delNodeIn.left:
            # Right node of delNode is available
            if not parentIn:
                # Root of tree is getting deleted
                delNodeIn.right.parent = None
                self.root = delNodeIn.right
            elif parentIn.val < delNodeIn.val:
                # If del node is on right side of parent
                parentIn.right = delNodeIn.right
                delNodeIn.right.parent = parentIn
            elif parentIn.val > delNodeIn.val:
                # If del node is on left side of parent
                parentIn.left = delNodeIn.right
                delNodeIn.right.parent = parentIn
        elif not delNodeIn.right:
            # Left node of delNode is available
            if not parentIn:
                # Root of tree is getting deleted
                delNodeIn.left.parent = None
                self.root = delNodeIn.left
            if parentIn.val < delNodeIn.val:
                # If del node is on right side of parent
                parentIn.right = delNodeIn.left
                delNodeIn.left.parent = parentIn
            elif parentIn.val > delNodeIn.val:
                # If del node is on left side of parent
                parentIn.left = delNodeIn.left
                delNodeIn.left.parent = parentIn

        return True

    # Private method to delete node with 2 children
    def _delTwoChildrentNode(self, delNodeIn, parentIn):
        # Get the leftmost child of right node / rightmost child of left node
        tempNode = delNodeIn.right
        parent = delNodeIn

        while (tempNode.left):
            parent = tempNode
            tempNode = tempNode.left

        # tempNode no more have left child
        if parent.right == tempNode:
            parent.right = tempNode.right
        else:
            parent.left = tempNode.right

        # Move leftmost node to delNodeIn position
        tempNode.left = delNodeIn.left
        tempNode.right = delNodeIn.right
        tempNode.parent = delNodeIn.parent

        # Change children of delNodeIn parent
        if self.root == delNodeIn:
            self.root = tempNode
        elif parentIn.left == delNodeIn:
            parentIn.left = tempNode
        else:
            parentIn.right = tempNode

        return True

    # Private method to search and delete a node recursively
    def _delete(self, valIn, nodeIn, parentIn):
        # Recursive approach
        if not nodeIn:
            # Node not available
            return False
        elif nodeIn.val < valIn:
            # Check right
            if not nodeIn.right:
                return False
            else:
                # Traverse Right
                return self._delete(valIn, nodeIn.right, nodeIn)
        elif nodeIn.val > valIn:
            # Check left
            if not nodeIn.left:
                return False
            else:
                # Traverse Left
                return self._delete(valIn, nodeIn.left, nodeIn)
        else:
            # Node found
            if not nodeIn.left and not nodeIn.right:
                # Delete leaf node
                return self._delLeafNode(nodeIn, parentIn)
            elif (nodeIn.left and not nodeIn.right) or (nodeIn.right and not nodeIn.left):
                # Single child node delete
                return self._delSingleChildNode(nodeIn, parentIn)
            elif nodeIn.left and nodeIn.right:
                # Two child node delete
                return self._delTwoChildrentNode(nodeIn, parentIn)

    # Public Method to delete value from a tree
    def delete(self, valIn):
        if not self.root:
            # Tree is empty
            raise exceptions.DeleteNodeException("Exception :: Tree is empty while deleting value = " + str(valIn) + ".")
        else:
            if not self._delete(valIn, self.root, None):
                raise exceptions.DeleteNodeException("Exception :: Can not delete Node with given value = " + str(valIn) + ". Node does not exist.")
            else:
                print("Node with value = ", str(valIn), " is deleted successfully.")
