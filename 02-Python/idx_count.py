#encoding: utf-8

nums = [1, 2 , 3, 4, 3, 2, 1]
idx = 0
count = 0

for i in range(len(nums)):
    if nums[i] == 2:
        count += 1
        if count == 2:
                idx = i
                break
print(idx)