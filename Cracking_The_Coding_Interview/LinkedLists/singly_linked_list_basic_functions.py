"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Write code for all basic functions of a singly linked list

1) create a new node -- Done
2) insert at start -- Done
3) insert at end -- Done
4) insert in the middle at given position -- Done
5) Delete a node from the start -- Done
6) Delete a node from the end -- Done
7) Delete a node from a given position
8) iterate over the linked list -- Done
9) Reverse a Linked List -- Done
10) Search an element in the linked list -- Done
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListBasicFunctions():
    def __init__(self):
        self.head = None

    def iterateOverLinkedList(self):
        temp_runner = self.head
        while temp_runner:
            print(temp_runner.data)
            temp_runner = temp_runner.next

    def searchElement(self, element):
        temp_runner = self.head
        while temp_runner:
            if temp_runner.data == element:
                print("Element is Found in the Linked List")
                return True
            temp_runner= temp_runner.next
        return False

    def insertAtstart(self, data):
        # create a new node and insert at the start ... Check if the linked list empty before doing this.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        # Create a new node and insert at the end ... Check if the linked List is empty before doing this.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp_runner = self.head
            while temp_runner.next != None:
                temp_runner = temp_runner.next
            temp_runner.next = new_node

    def insertAtGivenPosition(self, data, position):
        if position == 1:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                return
        prev = None
        temp_runner = self.head
        for i in range(position - 1):
            if temp_runner is None:
                print("Given Position does not exist in the Linked List ... Return without adding the Node")
                return
            prev = temp_runner
            temp_runner = temp_runner.next
        new_node = Node(data)
        prev.next = new_node
        new_node.next = temp_runner

    def deleteAtStart(self):
        # Check if linkedlist empty. If not just move the head pointer
        if self.head is not None:
            self.head = self.head.next

    def deleteAtEnd(self):
        #Check if the linkedList is empty. If not, use an auxilary variable to track the previous node to the last
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                prev = None
                current = self.head
                while current.next:
                    prev = current
                    current = current.next
                prev.next = None

    def deleteFromGivenPosition(self):
        pass

    def reverseLinkedListIterative(self):
        # Use 2 temp variables to reverse the linked List
        if (self.head is None) or (self.head.next is None):
            return self.head
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head

    def reverseLinkedListRecursive(self, head):
        if (head is None) or (head is None):
            return head
        temp = self.reverseLinkedListRecursive(head.next)
        head.next.next = head
        head.next = None
        return temp


def main():
    llObject = LinkedListBasicFunctions()
    llObject.insertAtstart(5)
    llObject.insertAtstart(4)
    llObject.insertAtEnd(6)
    #llObject.deleteAtStart()
    #llObject.deleteAtEnd()
    #llObject.searchElement(5)
    #llObject.iterateOverLinkedList()
    #llObject.reverseLinkedListIterative()
    #llObject.reverseLinkedListRecursive(llObject.head)
    #llObject.iterateOverLinkedList()
    llObject.insertAtGivenPosition(1, 3)
    llObject.iterateOverLinkedList()

if __name__ == "__main__":
    main()