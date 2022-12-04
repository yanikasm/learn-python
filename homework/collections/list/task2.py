# Дан массив nums, который вводят из консоли
# Создать массив ans такой, что ans[i] = nums[nums[i]]


nums = list(map(int, input().split(",")))
ans = []

for i in range(0, len(nums)):
   ans.append(nums[nums[i]])
print(ans)




#nums = [0, 2, 1, 5, 3, 4]
# i = 5
# x = nums[i] = 4
# y = nums[x]
