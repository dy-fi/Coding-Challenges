def largest_palindrome_product(n):
    largest = int("9" * n)
    results = []

    for i in range(largest, 0, -1):
        for j in range(largest, 0, -1):
            product = i * j
            if str(product) == str(product)[::-1] and len(str(product)) % 2 == 0:
                results.append(product)
    return max(results)

if __name__ == '__main__':
    print(largest_palindrome_product(3))