tab = ''
def pow(base, exponent):
    global tab 
    tab += ''
    if exponent == 0:
        return 1
    print(tab + "%d*%d^(%d-%d)" % (base, base, exponent, 1))
    return base * pow(base, exponent-1)

print('2^4')
print('result: ', pow(2, 4))