import sys
import os


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.no_of_nodes_in_ll = 0

    def isEmptyLinkedList(self):
        if self.head is None:
            #print("Linked List is Empty. Return True")
            return True
        else:
            #print("Linked List is not Empty. Return False")
            return False

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.no_of_nodes_in_ll += 1
            #print("LinkedList Empty: Marking this new Node as Head of Linked List")
            return
        new_node.nextNode = self.head
        self.head = new_node
        self.no_of_nodes_in_ll += 1
        #print("New node Added to the head of the Linked List ")
        return

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.no_of_nodes_in_ll += 1
            #print("Linked List Empty. Marking this new node as the Head of the LinkedList")
            return
        temp = self.head
        while temp.nextNode is not None:
            temp = temp.nextNode
        temp.nextNode = new_node
        self.no_of_nodes_in_ll += 1
        #print("New Node added to the End of the Linked List ")
        return

    def searchelement(self, data):
        if self.head is None:
            #print("Linked List Empty")
            return False
        temp = self.head
        while temp is not None:
            if temp.data == data:
                #print("Element Found in the LinkedList")
                return True
            temp = temp.nextNode
        #print("Element not Found in the Linked List")
        return False

    def deleteFromStart(self):
        if self.head is None:
            #print("LinkedList is Empty. Nothing to Delete")
            return
        self.head = self.head.nextNode
        self.no_of_nodes_in_ll -= 1
        #print("Node Deleted from the begining of the Linked List")
        return

    def deleteFromEnd(self):
        if self.head is None:
            #print("Linked List is Empty: Noting to Delete")
            return
        elif self.head.nextNode is None:
            #print("There is Just one Node in the Linked List. Deleting it")
            self.no_of_nodes_in_ll -= 1
            self.head = None
            return
        else:
            slow = self.head
            fast = self.head.nextNode
            while fast.nextNode is not None:
                slow = slow.nextNode
                fast = fast.nextNode
            slow.nextNode = None
            self.no_of_nodes_in_ll -= 1
            #print("The last Node from the Linked List is Deleted")

    def reverse_iterative(self):
        if self.head == None or self.head.nextNode == None:
            return self.head
        prev = None
        current = self.head
        while current:
            temp = current.nextNode
            current.nextNode = prev
            prev = current
            current = temp
        return prev







