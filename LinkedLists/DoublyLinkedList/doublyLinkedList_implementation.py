import sys
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtStart(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertNodeAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def reverse_list(self):
        if self.head == None or self.head.next == None:
            pass
        else:
            current = self.head
            while current:
                current.prev, current.next = current.next, current.prev
                current = current.prev
            self.head, self.tail = self.tail, self.head


    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def searchElement(self, element):
        temp = self.head
        while temp:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    def deleteFromStart(self):
        if not self.head:
            return self.head
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = self.head
            return self.head

    def deleteFromEnd(self):
        if not self.head:
            return self.head
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = self.tail
            return self.head

