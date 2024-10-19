def is_prime(func):
    def surrogate(a, b, c):
        result = func(a, b, c)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result
    return surrogate


@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)