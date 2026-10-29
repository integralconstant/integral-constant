stack = [None, None, None, None, None]
top = -1

top += 1
stack[top]="커피"
top += 1
stack[top]="녹차"
top += 1
stack[top]="꿀물"

print("-----스택 상태-----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
    
def push(data):
    global top
    top += 1
    stack[top] = data
    
def pop():
    global top
    data = stack[top]
    stack[top] = None
    top -= 1
    return print("pop된 데이터:" + str(data))

def print_stack():
    print("-----스택 상태-----")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("=============")
        
print_stack()

pop()
pop()
print_stack()