# Дан массив nums
# Создайте массив ans такой, что ans[i] равен сумме элементов nums
# с индексами от 0 до i включительно (nums[0], nums[1], ..., nums[i])

# Пример: nums = [1, 2, 3, 4], ans = [1, 3, 6, 10]. Объяснение: ans = [1, 1+2, 1+2+3, 1+2+3+4]

nums = list(map(int, input().split(" ")))
print(nums)
