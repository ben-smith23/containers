'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder
than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the
    class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance
        factor in [-1,0,1].
        '''
        if self.root is None:
            return True
        else:
            return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        stack = [node]
        while stack:
            node = stack.pop()
            balance_factor = AVLTree._balance_factor(node)
            if balance_factor not in [-1, 0, 1]:
                return False
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return True

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        '''
        if node.right is None:
            return newroot
        else:
            newroot = node.right
            node.right = newroot.left
            newroot.left = node
            node.height = 1 + max(BinaryTree._height(node.left),
            BinaryTree._height(node.right))
            newroot.height = 1 + max(BinaryTree._height(newroot.left),
            BinaryTree._height(newroot.right))
            return newroot
        '''
        ogroot = node
        if ogroot.right:
            newroot = Node(ogroot.right.value)
            newroot.left = Node(ogroot.value)
            newroot.right = ogroot.right.right
            newroot.left.left = ogroot.left
            newroot.left.right = ogroot.right.left
            return newroot
        else:
            return ogroot

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        '''
        newroot = node.left
        if node.right is not None:
            node.left = newroot.right
        newroot.right = node
        node.height = 1 + max(BinaryTree._height(node.right),
        BinaryTree._height(node.left))
        newroot.height = 1 + max(BinaryTree._height(newroot.right),
        BinaryTree._height(newroot.left))
        return newroot
        '''
        ogroot = node
        if ogroot.left:
            newroot = Node(ogroot.left.value)
            newroot.right = Node(ogroot.value)
            newroot.left = ogroot.left.left
            newroot.right.right = ogroot.right
            newroot.right.left = ogroot.left.right
            return newroot
        else:
            return ogroot

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert
        into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            return AVLTree._insert(value, self.root)
        else:
            self.root = Node(value)
        self._rebalance(self.root)

    @staticmethod
    def _insert(value, node):
        '''
        ret = False
        if value < node.value and AVLTree._balance_factor in [-1, 0, 1]:
            if node.left:
                ret &= AVLTree._insert(value, node.left)
            else:
                node.left = Node(value)
                ret = True
        elif AVLTree._balance_factor not in [-1, 0, 1]:
            AVLTree._rebalance(node)
        elif value > node.value and AVLTree._balance_factor in [-1, 0, 1]:
            if node.right:
                ret &= AVLTree._insert(value, node.right)
            else:
                node.right = Node(value)
                ret = True
        elif AVLTree._balance_factor not in [-1, 0, 1]:
            AVLTree._rebalance(node)
        return ret
        '''
        if value < node.value:
            if node.left:
                AVLTree._insert(value, node.left)
            else:
                node.left = Node(value, node)
                AVLTree.updateBalance(node.left)
        else:
            if node.right:
                AVLTree._insert(value, node.right)
            else:
                node.right = Node(value, node)
                AVLTree.updateBalance(node.right)

    @staticmethod
    def updateBalance(node):
        balance_factor = AVLTree._balance_factor(node)
        if balance_factor > 1 or balance_factor < -1:
            AVLTree._rebalance(node)
            return
        if node is not None:
            if node.left():
                balance_factor += 1
            elif node.right():
                balance_factor -= 1
            if balance_factor != 0:
                AVLTree.updateBalance(node)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node:
            balance_factor = AVLTree._balance_factor(node)
        if balance_factor > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._right_rotate(node.right)
            node = AVLTree._left_rotate(node)
        elif balance_factor < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            node = AVLTree._left_rotate(node)
        return node
