# На основе предыдущего решения
# Вычислите x1 = (-b + sqrt(D)) / 2a, x2 = (-b - sqrt(D)) / 2a и выведите их
from math import sqrt

print("Привет, я решаю квадратные уравненения! Введи коэффиценты a,b,c")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = b * b - 4 * a * c

if d < 0:
    print("Дискриминант должен быть больше 0, а в вашем случае он " + str(d))
    exit()

x = (-b + sqrt(d)) / 2 * a
x2 = (-b - sqrt(d)) / 2 * a
print(x)
print(x2)
print("Спасибо, что воспользовался мной, друг!")
