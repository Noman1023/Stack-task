try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

from exceptions import EmptyStackException, NullElementException

class Stack:
	def __init__(self, items=None):
		self.items = []

	def size(self):
		return len(self.items)

	def push(self, element):
		if element is None:
			raise NullElementException('Cannot push null item.')
		self.items.append(element)

	def pop(self):
		if not self.items:
			raise EmptyStackException('Stack is empty.')
		return self.items.pop()

	def peek(self):
		if not self.items:
			raise EmptyStackException('Stack is empty.')
		return self.items[-1]
		
	def empty(self):
		return not bool(self.items)


stack = Stack()  # can provide list as an argument
stack.push(54)
stack.pop()
print(stack.empty())
print(stack.size())
print(stack.items)