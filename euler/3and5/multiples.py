def three_and_five():
    result = 0
    for i in range(1000):
        if i % 3 == 0:
            result += i 
        elif i % 5 == 0:
            result += i
    return result

if __name__ == '__main__':
    print(three_and_five())