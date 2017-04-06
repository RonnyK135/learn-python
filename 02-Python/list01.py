#encoding: utf-8

'''
nums = [6, 11, 7, 9, 4, 2, 1]
1.从nums中拿到第一个值放到变量hand中
2.从nums第二个元素开始比较，如果比hand中大，则重新赋值
'''
nums = [6, 11, 7, 9, 4, 2, 1]
hand = nums[0]

for num in nums:
    if num > hand:
        hand = num
print(hand)

nums = [6, 11, 7, 9, 4, 2, 1]
hand = None

for num in nums:
    if hand is None or hand < num:
        hand = num
print(hand)


