def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    return print("스택이 초기화되었습니다. 스택 크기는 " + str(size) + "입니다.")
    
def is_full():
    global top
    if top == len(stack) -1:
        return print("스택이 가득 찼습니다.")
    else:
        return print("스택이 가득 차지 않았습니다.")
    
def is_empty():
    global top
    if top == -1:
        return True
    else:
        return False
    
def push(data):
    global top
    top += 1
    stack[top] = data
    
def pop():
    global top
    data = stack[top]
    stack[top] = None
    if (is_empty()):
        top -= 1
        return print("스택이 비어있습니다.")
    else:
        top -= 1
        return print("pop된 데이터:" + str(data))

def peek():
    global top
    data = stack[top]
    return print("peek된 데이터: " + str(data))
    
def print_stack():
    print("-----스택 상태-----")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("-----------------------------")

init_stack(7)
is_full()
push("녹차")
push("커피")
push("꿀물")
push("콜라")
push("사이다")
print_stack()
pop()
pop()
pop()
print_stack()
peek()