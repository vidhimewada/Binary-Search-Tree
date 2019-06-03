class InsertNodeException(Exception):
    """
        Class to represent custom exception while inserting a node in BST
    """

    # Value Constructor
    def __init__(self, msgIn):
        Exception.__init__(self, msgIn)


class DeleteNodeException(Exception):
    """
        Class to represent custom exception while deleting a node in BST
    """

    # Value Constructor
    def __init__(self, msgIn):
        Exception.__init__(self, msgIn)


class PrintTreeException(Exception):
    """
        Class to represent custom exception while printing BST
    """

    # Value Constructor
    def __init__(self, msgIn):
        Exception.__init__(self, msgIn)
