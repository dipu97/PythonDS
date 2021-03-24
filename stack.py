def create_stack():
    stack = []
    return stack
def check_empty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
while 1:
    print('Select an action')
    print('Select 1 for view:\n')
    print('Select 2 for push:\n')
    print('Select 3 for pop:\n')
    print('Select 4 for exit:\n')
    x=int(input())
    if x==1:
        print("The stack is " + str(stack))

    if x==2:
        y=input('Enter element to push')
        push(stack, str(y))
        print("The stack is " + str(stack))
    if x==3:
        print("popped item: " + pop(stack))
        print("stack after popping an element: " + str(stack))
    if x==4:
        break