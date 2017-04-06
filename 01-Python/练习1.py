#encoding: utf-8
num = input('请输入你的成绩')
num = float(num)

if num >= 90:
    print('优秀')
elif num >= 80:
    print('良好')
elif num >= 60:
    print('及格')
else:
    print('不及格')
