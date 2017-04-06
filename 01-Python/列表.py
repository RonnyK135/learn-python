#encoding: utf-8
nums = [1,2,4,9,4,10,12]
for num in nums:
    print(num)
#作业1
for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a * b,'\t',end='')
    print()

#作业2
import random
random_num = random.randint(0,100)
print('这是一个猜数游戏，只有5次机会：')
i = 0
while i < 5:
    num = input("请输入你的猜的数字：")
    if int(num) < random_num:
        print("猜小了")
    elif int(num) > random_num:
        print("猜大了")
    elif int(num) == random_num:
        print("恭喜你，猜对了")
        break
    i += 1
else:
    print("呜呜~~，下次再来吧")

