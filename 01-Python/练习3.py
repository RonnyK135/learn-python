#encoding: utf-8
num = input('请输入一个数字或exit：')
input_sum = 0
input_count = 0
while num != 'exit':
    input_sum += int(num)
    input_count += 1
    num = input('请输入一个数字或exit：')

if input_count == 0:
    print('sum:0 avg:0')
else:
    print('sum:',input_sum,'avg:',input_sum // input_count)