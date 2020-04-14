def square_sum(n):

    sum_of_squares = 0
    square_of_sums = 0

    # sum of squares
    for i in range(1, n + 1):
        sum_of_squares += (i ** 2)
    
    # square of sums
    for i in range(1, n + 1):
        square_of_sums += i
    
    square_of_sums = square_of_sums ** 2

    return square_of_sums - sum_of_squares


if __name__ == '__main__':
    print(square_sum(100))