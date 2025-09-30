import queue


pq = queue.PriorityQueue()

# pq.put((priority, task))
# this will add the task to the queue with the given priority
# it is a tuple where the first element is the priority and the second element is the task itself
# this will add the tuple to the priority queue, which is a min-heap by default


pq.put((1, (2,3))) # lower numbers indicate higher priority
pq.put((3, 'low priority task')) # can be any object, here we use a string, but it could be a function, a class instance, etc.
pq.put((2, 'medium priority task'))

priority, task = pq.get()
print(f'Priority: {priority}, Task: {task}')


pq.put((0, 'urgent priority task'))
pq.put((4, 'very low priority task'))
pq.put((1, 'new high priority task'))



while not pq.empty():
    priority, task = pq.get()
    print(f'Priority: {priority}, Task: {task}')




