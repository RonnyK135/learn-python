#encoding: utf-8
#break和continue的区别
#break 跳出循环，结束执行
#continue 跳过本次循环，继续下一次循环条件判断
idx = 0
max_idx = 5
print('break')
while idx <= max_idx:
    idx += 1
    if idx == 3:
        #break
        continue
    print(idx)