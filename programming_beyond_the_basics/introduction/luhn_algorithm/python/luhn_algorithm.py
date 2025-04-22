def verify(digits):
    double = lambda num: num * 2 
    sum_digits = lambda num: sum(map(int, str(num)))
    double_and_sum = lambda num: sum_digits(double(num))
    conditional_double_and_sum = lambda tuple : (lambda index, digit: double_and_sum(digit) if index%2 else digit)(tuple[0], int(tuple[1]))
    return sum(map(conditional_double_and_sum, enumerate(digits))) % 10 == 0


if __name__ == '__main__'
    import os
    os.system('clear')
    print('------------')
    print(verify("17893729975"))
    print(verify("17893729974"))
    print('ok')
    print('------------')

