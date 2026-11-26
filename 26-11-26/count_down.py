def count_down(n):
    if n <= 0:
        print("Countdown finished")
        return
    print(n)
    m = n-1
    count_down(m)
    
count_down(100)