def print_star(n):
    if n > 0:
        print_star(n-1)
        print('*' * n)
        return
    
print_star(5)