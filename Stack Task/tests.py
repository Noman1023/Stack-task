
import unittest
from stack import Stack
from exceptions import EmptyStackException, NullElementException


class StackTester(unittest.TestCase):

    def test_stack_init(self):
        s = Stack()
        self.assertEqual(0, s.size())

    def test_push1_size(self):
        s = Stack()
        s.push()
        self.assertEqual(1, s.size())

    def test_push1_size(self):
        s = Stack()
        s.push(10)
        self.assertEqual(1, s.size())

    def test_push1_items(self):
        s = Stack()
        s.push(5)
        self.assertEqual([5], s.items)

    def test_push2_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(2, s.size())

    def test_push2_items(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual([5,6], s.items)

    def test_push2_pop1_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        s.pop()
        self.assertEqual(1, s.size())

    def test_push2_pop1_value(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(9, s.pop())

    def test_push2_pop2_size(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        s.pop()
        self.assertEqual(0, s.size())

    def test_push2_pop2_value(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        self.assertEqual("Glob", s.pop())

    def test_empty(self):
        s = Stack()
        s.push(10)
        s.pop()
        self.assertEqual(True, s.empty())

    def test_empty_push1(self):
        s = Stack()
        s.push(5)
        self.assertEqual(False, s.empty())

    def test_empty_push1_pop1(self):
        s = Stack()
        s.push(1)
        s.pop()
        self.assertEqual(True, s.empty())

    def test_peek_push1(self):
        s = Stack()
        s.push(88)
        self.assertEqual(88, s.peek())

    def test_peek_push3_pop1(self):
        s = Stack()
        s.push('hello')
        s.push('world')
        s.pop()
        self.assertEqual('hello', s.peek())

    def test_pop_empty(self):
        s = Stack()
        self.assertRaises(EmptyStackException, s.pop)

    def test_peek_empty(self):
        s = Stack()
        self.assertRaises(EmptyStackException, s.peek)

    def test_null_push(self):
    	s = Stack()
    	self.assertRaises(NullElementException, s.push, None)

if __name__ == '__main__':
    unittest.main()