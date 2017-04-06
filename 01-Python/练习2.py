#encoding: utf-8

year = input('请输入一个年份：')
if int(year) % 4 ==0 and int(year) % 100 != 0:
    print(year,'为闰年')
elif int(year) % 400 == 0:
    print(year,'为闰年')
else:
    print(year,'不是闰年')