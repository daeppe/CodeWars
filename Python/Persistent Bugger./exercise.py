def persistence(n):
    output = 0

    while n >= 10:
        digits = [int(d) for d in str(n)]
        n = 1

        for digit in digits:
            n *= digit

        output += 1

    return output