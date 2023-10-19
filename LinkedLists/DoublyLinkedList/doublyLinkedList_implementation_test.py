import unittest
from doublyLinkedList_implementation import doublyLinkedList

class TestdoublyLinkedList(unittest.TestCase):

    def test_isEmpty_return_true(self):
        temp = doublyLinkedList()
        self.assertTrue(temp.isEmpty())

    def test_isEmpty_return_false(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        self.assertFalse(temp.isEmpty())

    def test_insertNodeAtStart(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        temp.insertNodeAtStart(4)
        self.assertEqual(temp.head.data, 4)

    def test_insertNodeAtEnd(self):
        temp = doublyLinkedList()
        temp.insertNodeAtEnd(4)
        temp.insertNodeAtEnd(5)
        temp.insertNodeAtEnd(6)
        self.assertEqual(temp.tail.data, 6)
        self.assertNotEqual(temp.head.data, 6)

    def test_reverse_list(self):
        temp = doublyLinkedList()
        temp.insertNodeAtEnd(4)
        temp.insertNodeAtEnd(5)
        temp.insertNodeAtEnd(6)
        temp.reverse_list()
        reverse_list = []
        runner = temp.head
        while runner:
            reverse_list.append(runner.data)
            runner = runner.next
        self.assertEqual([6,5,4], reverse_list)

        temp.reverse_list()
        reverse_list = []
        runner = temp.head
        while runner:
            reverse_list.append(runner.data)
            runner = runner.next
        self.assertNotEqual([6, 5, 4], reverse_list)

    def test_searchElement_found(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        temp.insertNodeAtStart(4)
        self.assertTrue(temp.searchElement(4))

    def test_searchElement_not_found(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        temp.insertNodeAtStart(4)
        self.assertFalse(temp.searchElement(10))

    def test_deleteFromStart(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        temp.insertNodeAtStart(4)
        temp.deleteFromStart()
        self.assertEqual(temp.head.data, 5)

    def test_deleteFromEnd(self):
        temp = doublyLinkedList()
        temp.insertNodeAtStart(5)
        temp.insertNodeAtStart(4)
        temp.deleteFromEnd()
        self.assertEqual(temp.tail.data, 4)

if __name__ == '__main__':
    unittest.main()
