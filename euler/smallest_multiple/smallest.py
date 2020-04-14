def smallest_multiple(n):
    curr = 2520

    while True:
        for i in range(n, n//2, -1):
            print(i, curr)
            if curr % i != 0:
                curr += 20
                break
            elif i == n//2 + 1: return curr
        

if __name__ == '__main__':
    print(smallest_multiple(20))