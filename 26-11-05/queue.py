def init_queue(size):
    global test_queue, front, rear
    test_queue = [None] * size
    front = -1
    rear = -1
    return print("큐가 초기화되었습니다. 큐 크기는 " + str(size) + "입니다.")

def enqueue(data):
    global rear
    if is_full():
        print("큐가 가득 찼습니다.")
        return
    rear += 1
    test_queue[rear] = data
    
def dequeue():
    global front
    if is_empty():
        print("큐가 비어있습니다.")
        return None
    front += 1
    data = test_queue[front]
    test_queue[front] = None
    return data

def peek_queue():
    global front
    if is_empty():
        print("큐가 비어있습니다.")
        return None
    data = test_queue[front + 1]
    return print("peek된 데이터: " + str(data))

def queue_print():
    print("-----큐 상태-----")
    for i in range(len(test_queue)):
        print(test_queue[i])
    print("-----------------------------")
    print("front: " + str(front))
    print("rear: " + str(rear))
    print("-----------------------------")
    
def is_full():
    global rear
    if rear == len(test_queue) - 1:
        return True
    else:
        return False

def is_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False
    
init_queue(5)

enqueue("커피")
enqueue("녹차")
enqueue("꿀물")
queue_print()

dequeue()
dequeue()
dequeue()
dequeue()
queue_print()
enqueue("콜라")
print("enqueue 후 큐 상태: ")
queue_print()
peek_queue()