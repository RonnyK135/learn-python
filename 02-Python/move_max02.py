#encoding: utf-8
'''
nums=[6, 11,7, 9, 4, 2, 1]
'''

nums=[6, 11, 7, 9, 4, 2, 1]

for j in range(len(nums)-1):
    for i in range(len(nums)- 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
print(nums)

for i in range(len(nums)- 1):
        if nums[i] > nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
print(nums)



