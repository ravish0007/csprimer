def verify(digits):
    def double(num): return num * 2
    def sum_digits(num): return sum(map(int, str(num)))
    def double_and_sum(num): return sum_digits(double(num))

    def conditional_double_and_sum(tuple): return (lambda index, digit: double_and_sum(
        digit) if index % 2 else digit)(tuple[0], int(tuple[1]))
    return sum(map(conditional_double_and_sum, enumerate(digits))) % 10 == 0


if __name__ == '__main__':
    import os
    os.system('clear')
    print('------------')
    print(verify("17893729975"))
    print(verify("17893729974"))
    print('ok')
    print('------------')
