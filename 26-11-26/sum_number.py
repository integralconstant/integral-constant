# 
# sum = 0
# for i in range(100000000, 0, -1):
#     sum += i
# print("The sum is:", sum)

def sum_number(n, m):
    if n > m:
        max = n
        min = m
    else:
        max = m
        min = n
    foo = ((min+max)*max)/2
    print(foo)
    
sum_number(1000, 1)