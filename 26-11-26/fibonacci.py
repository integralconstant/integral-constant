def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print('피보나치 수: ', end= '')
for i in range(2, 50):
    print(fibo(i), end=' ')