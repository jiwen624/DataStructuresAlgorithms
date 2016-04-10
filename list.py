#!/usr/bin/env python3

"""This is a sample implementation of the following data structures:
 - LinkedList
 - Stack (implemented with SingleList interally
"""


class Node:
    __slots__ = ['_value', '_prev_node', '_next_node']
    def __init__(self, value, prev_node=None, next_node=None):
        self._value = value
        self._prev_node = prev_node
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        self._prev_node = prev_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    def __repr__(self):
        return 'value={}'.format(self._value)


class LinkedList:
    def __init__(self, node):
        if not node:
            raise ValueError('Invalid value: None')

        self._head = node
        self._head.prev_node = None
        self._tail = self._head
        self._tail.next_node = None
        self._size = 1

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node

    def __repr__(self):
        list_str = 'total_size={} '.format(self.size)
        node = self.head
        while node:
            list_str += '(value={})->'.format(node.value)
            node = node.next_node
        return list_str

    def append(self, node):
        """Append a Node object onto the tail of the LinkedList.

        :type node: Node
        """
        if not node:
            raise ValueError('Invalid value: None')

        self.tail.next_node = node
        node.prev_node = self.tail

        self.tail = node
        self.tail.next_node = None
        self.size += 1
        return True

    def pop_head(self):
        if not self.size:
            raise ValueError('The list is already empty!')

        old_head = self.head
        self.head = self.head.next_node
        old_head.next_node = None
        self.head.prev_node = None

        self.size -= 1
        return old_head

    def pop_tail(self):
        if not self.size:
            raise ValueError('The list is already empty!')

        pop_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        pop_node.prev_node = None

        self.size -= 1

    def insert_head(self, node):
        if not node:
            raise ValueError('Invalid value: None')

        node.next_node = self.head
        node.prev_node = None
        self.head.prev_node = node

        self.head = node
        self.size += 1
        return self


class Stack():
    """A simple implementation of Stack
    """

    class _Node():
        """The internal class for nodes"""
        __slots__ = ['_value', '_next']

        def __init__(self, value, next=None):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty!')
        e = self._head._value
        self._head = self._head._next
        self._size -= 1
        return e

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._head._value

    def __repr__(self):
        str = 'Stack: '
        e = self._head
        while e:
            str += '{}|'.format(e._value)
            e = e._next

        return str


class CircularQueue:
    """A simple implementation of the Circular Queue.
    """

    class _Node:
        __slots__ = ['_value', '_next_node']

        def __init__(self, value, next_node=None):
            self._value = value
            if next_node is not None:
                self._next_node = next_node
            else:
                self._next_node = self

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        @property
        def next(self):
            return self._next_node

        @next.setter
        def next(self, node):
            self._next_node = node

    def __init__(self, value=None):
        if value is not None:
            self._tail = self._Node(value, None)
            self._size = 1
        else:
            self._tail = None
            self._size = 0

    def __len__(self):
        return self._size

    def first(self):
        if self._size == 0:
            raise ValueError('The Queue is empty!')
        return self._tail.next.value

    def enqueue(self, value):
        if not value:
            raise ValueError('Cannot assign None to the value')

        if self._size != 0:
            node = self._Node(value, self._tail.next)
            self._tail.next = node
            self._tail = self._tail.next

            self._size += 1
        else:
            self._tail = self._Node(value, None)
            self._size = 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('CircularQueue is empty now!')
        else:
            node = self._tail.next
            self._tail.next = node.next
            node.next = None

            self._size -= 1

            if self.is_empty():
                self._tail = None

        return node.value

    def rotate(self):
        if self._size == 0:
            raise ValueError('The Queue is empty!')

        self._tail = self._tail.next
        return self._tail.value

    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    @property
    def tail(self):
        if self._size:
            return self._tail.value
        else:
            return None

    def __iter__(self):
        node = None
        if self._size != 0:
            node = self._tail.next

        cnt = self._size

        while cnt > 0:
            yield node.value
            cnt -= 1
            node = node.next


class CircularQueue:
    """A simple implementation of the Circular Queue.
    """

    class _Node:
        __slots__ = ['_value', '_next_node']

        def __init__(self, value, next_node=None):
            self._value = value
            if next_node is not None:
                self._next_node = next_node
            else:
                self._next_node = self

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

        @property
        def next(self):
            return self._next_node

        @next.setter
        def next(self, node):
            self._next_node = node

    def __init__(self, value=None):
        if value is not None:
            self._tail = self._Node(value, None)
            self._size = 1
        else:
            self._tail = None
            self._size = 0

    def __len__(self):
        return self._size

    def first(self):
        if self._size == 0:
            raise ValueError('The Queue is empty!')
        return self._tail.next.value

    def enqueue(self, value):
        if not value:
            raise ValueError('Cannot assign None to the value')

        if self._size != 0:
            node = self._Node(value, self._tail.next)
            self._tail.next = node
            self._tail = self._tail.next

            self._size += 1
        else:
            self._tail = self._Node(value, None)
            self._size = 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('CircularQueue is empty now!')
        else:
            node = self._tail.next
            self._tail.next = node.next
            node.next = None

            self._size -= 1

            if self.is_empty():
                self._tail = None

        return node.value

    def rotate(self):
        if self._size == 0:
            raise ValueError('The Queue is empty!')

        self._tail = self._tail.next
        return self._tail.value

    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    @property
    def tail(self):
        if self._size:
            return self._tail.value
        else:
            return None

    def __iter__(self):
        node = None
        if self._size != 0:
            node = self._tail.next

        cnt = self._size

        while cnt > 0:
            yield node.value
            cnt -= 1
            node = node.next


if __name__ == '__main__':
    q = CircularQueue(-1)
    print('Size: {}, Tail: {}'.format(q.size, q.tail))

    q.enqueue(3)
    q.enqueue(4)
    q.enqueue('tom')
    q.enqueue(8)
    print('Size: {}, Tail: {}'.format(q.size, q.tail))

    cnt = q.size
    while cnt >= 0:
        print(q.rotate(), end=';')
        cnt -= 1

    print('Size: {}, Tail: {}'.format(q.size, q.tail))
    for i in q:
        print(i, end=',')


