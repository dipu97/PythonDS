def Queue_Start():
    queue=[]
    return queue
def inqueue(queue,item):
    queue.append(item)
def dequeue(queue):
        if len(queue) < 1:
            return None
        return queue.pop(0)
queue = Queue_Start()
while 1:
    print('Select an action')
    print('Select 1 for view:\n')
    print('Select 2 for enqueue:\n')
    print('Select 3 for dequeue:\n')
    print('Select 4 for exit:\n')
    x=int(input())
    if x==1:
        print("The stack is " + str(queue))

    if x==2:
        y=input('Enter element to push')
        inqueue(queue, str(y))
        print("The stack is " + str(queue))
    if x==3:
        dequeue(queue)
        print("stack after popping an element: " + str(queue))
    if x==4:
        break