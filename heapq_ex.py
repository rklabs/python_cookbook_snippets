import heapq
import random

nums = [random.randint(0, 100) for _ in range(100)]

print('before heapify')
print(nums)

# Create copy of above list and heapify the list
nums_heapq = list(nums)
heapq.heapify(nums_heapq)

print('after heapify')
print(nums_heapq)

# Get the 3 least numbers from heap list
for _ in range(3):
    print(heapq.heappop(nums_heapq))
