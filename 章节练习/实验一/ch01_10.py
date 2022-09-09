x=input('请输入一个三位以上的数')
x=int(x)
if 0<x<99:
    print('请重新输入一个三位以上的数')
else:
    x=x//100
    print(x)
