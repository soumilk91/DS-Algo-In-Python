"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Write code for all basic functions of a Doubly linked list

1) create a new node
2) insert at start
3) insert at end
4) insert in the middle at given position
5) Delete a node from the start
6) Delete a node from the end
7) Delete a node from a given position
8) iterate over the linked list
9) Reverse a Linked List
10) Search an element in the linked list
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedListBasicFunctions():
    def __init__(self):
        self.head = None
        self.tail = None

    def iterateOverLinkedList(self):
        temp_runner = self.head
        while temp_runner:
            print(temp_runner.data)
            temp_runner = temp_runner.next

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def deleteFromStart(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteFromEnd(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


    def searchElement(self, element):
        temp_runner = self.head
        while temp_runner:
            if temp_runner.data == element:
                print("Element Found in the Linked List")
                return True
            temp_runner = temp_runner.next
        print("Element not found in the Linked List")
        return False


def main():
    dllobject = DoublyLinkedListBasicFunctions()
    dllobject.insertAtStart(6)
    dllobject.insertAtStart(5)
    dllobject.insertAtEnd(7)
    dllobject.iterateOverLinkedList()
    #dllobject.deleteFromStart()
    #print("++++++++")
    #dllobject.iterateOverLinkedList()
    #dllobject.deleteFromEnd()
    #print("++++++++")
    #dllobject.iterateOverLinkedList()
    dllobject.searchElement(6)


if __name__ == "__main__":
    main()

