import unittest
from singlyLinkedList_implementation import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_isEmpty_return_true(self):
        temp = LinkedList()
        self.assertTrue(temp.isEmptyLinkedList())

    def test_isEmpty_return_false(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        self.assertFalse(temp.isEmptyLinkedList())

    def test_searchelement_found(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(6)
        temp.insertAtStart(10)
        self.assertTrue(temp.searchelement(6))

    def test_searchelement_Notfound(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(6)
        temp.insertAtStart(10)
        self.assertFalse(temp.searchelement(12))

    def test_insertAtStart(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(6)
        temp.insertAtStart(10)
        runner = temp.head
        self.assertEqual(10, runner.data)

    def test_insertAtEnd(self):
        temp = LinkedList()
        temp.insertAtEnd(5)
        temp.insertAtEnd(6)
        temp.insertAtEnd(10)
        runner = temp.head
        while runner.nextNode != None:
            runner = runner.nextNode
        self.assertEqual(10, runner.data)

    def test_deleteFromStart(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(6)
        temp.insertAtStart(10)
        temp.insertAtStart(16)
        temp.deleteFromStart()
        runner = temp.head
        self.assertEqual(10, runner.data)

    def test_deleteFromStart(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(6)
        temp.insertAtStart(10)
        temp.insertAtStart(16)
        temp.deleteFromEnd()
        runner = temp.head
        while runner.nextNode != None:
            runner = runner.nextNode
        self.assertEqual(6, runner.data)

    def test_reverse_iterative_none(self):
        temp = LinkedList()
        self.assertEqual(None, temp.reverse_iterative())

    def test_reverse_iterative_one_node(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        self.assertEqual(temp.head, temp.reverse_iterative())

    def test_reverse_iterative_multiple_nodes(self):
        temp = LinkedList()
        temp.insertAtStart(5)
        temp.insertAtStart(4)
        temp.insertAtStart(3)
        reverse_list = []
        runner = temp.reverse_iterative()
        while runner:
            reverse_list.append(runner.data)
            runner = runner.nextNode
        self.assertEqual(reverse_list, [5,4,3])

if __name__ == '__main__':
    unittest.main()