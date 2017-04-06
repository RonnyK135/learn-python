#encoding: utf-8

'''
插入排序：在已经排好的数据序列中插入一个数，从而得到一个新的，个数加一的有序数据，但要求插入后此数据系列任然有序
1.定义一个空list nums存储数据 nums = []
2.while True，输入要插入的数字
3.如果插入的是第一个数字，直接放入list中，通过len判断
4.如果是第二个数，则进行比较大小
'''
nums = []
while True:
    num = input('请输入你要放入的数字：')
    if len(nums) == 0:

