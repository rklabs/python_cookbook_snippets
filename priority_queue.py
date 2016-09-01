#!/usr/bin/env python
'''
Priority queue implements object popping based on priority attached to that
object.
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


pq = PriorityQueue()
pq.push(Item('foo'), 5)
pq.push(Item('bar'), 4)
pq.push(Item('baz1'), 1)
pq.push(Item('baz2'), 1)

print(pq.pop())
print(pq.pop())
print(pq.pop())
