# Введите два числа a и b из консоли
# Выведите таблицу умножения для чисел [0, a] на [0, b]

a = int(input())
b = int(input())

for i in range(0, a + 1):
    for j in range(0, b + 1):
        print(i*j)
