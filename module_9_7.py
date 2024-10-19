def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result < 2:
            print('Простое число должно быть больше 1')
            return result
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result
    return wrapper


@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(0, 0, -6)
print(result)
