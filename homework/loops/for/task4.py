# Введите из консоли два числа a и b
# Выведите сумму всех чисел из отрезка [a, b], которые делятся на 3, но не делятся на 7

a = int(input())
b = int(input())
summary = 0

for i in range(a, b+1):
    if i % 3 == 0 and i % 7 != 0:
        print(i)
        summary = summary + i

print(summary)
