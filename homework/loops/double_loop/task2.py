# Вывести все возможные подстрочки из строки s
# подстрочкой считается часть строки от i до j (по индексам), где i <= j
# чтобы получить подстрочку s для индексов i, j надо написать s[i : j+1]
# чтобы узнать длину строки s надо написать len(s)

# s = input() # "abcdefghij"
s = "abcdefghij"

for i in range(0, len(s)):
    for j in range(i, len(s)):
        print(s[i: j + 1])
