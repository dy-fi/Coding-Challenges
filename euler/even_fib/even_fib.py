
def even_fibonnaci(n):
    fib_ar = [1, 2]
    result = 0
    last = 0

    while(last <= n):
        last = fib_ar[-1] + fib_ar[-2]

        if last % 2 == 0:
            result += last
            print(last)

        fib_ar.append(last)
    
    return result + 2

if __name__ == '__main__':
    print(even_fibonnaci(4000000))