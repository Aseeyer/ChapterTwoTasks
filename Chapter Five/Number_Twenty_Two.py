# (Simulating a Queue with a List)
queue = []

queue.append(3)
queue.append(2)
queue.append(1)

print("Queue after enqueuing:", queue)

print("Dequeued:", queue.pop(0))
print("Dequeued:", queue.pop(0))
print("Dequeued:", queue.pop(0))

print("Queue after dequeuing:", queue)
