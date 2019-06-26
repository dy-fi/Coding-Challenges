def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        return str(dec_to_bin(number/2) + dec_to_bin(number%2))