SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1

def isFull():
    global rear
    return rear == len(Q)-1


def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("Queue is Full")
    else:
        rear = rear + 1;
        Q[rear] = item;

def deQueue():
    global front
    if isEmpty():
        print("Queue is Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print("Queue is Empty")
    else:
        return Q[front+1]


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())

