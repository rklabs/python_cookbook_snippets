#!/usr/bin/env python
'''
Priority queue implements object ordering based on priority attached to that
object.  The item is pushed into the queue along with priority and index.
Before understanding why index is required lets see tuple comparison.  Tuple
comparison is done element by element in same position.  This is true for all
sequence types.  Index is required when two Items have the same priority.  If
name and priority is two Item's is same then they are compared based on index
value.
'''
import heapq


class PriorityQueue(object):

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return 'Item({!r})'.format(self._name)

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push(Item('foo'), 5)
    pq.push(Item('bar'), 4)
    pq.push(Item('baz1'), 1)
    pq.push(Item('baz2'), 1)

    print(pq.pop())
    print(pq.pop())
    print(pq.pop())
