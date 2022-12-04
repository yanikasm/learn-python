# Введите число a из консоли и заполните список числами [0, a]
a = int(input())
arr = []
for i in range(a+1):
    arr.append(i)
    if i == 4:
        print(arr)