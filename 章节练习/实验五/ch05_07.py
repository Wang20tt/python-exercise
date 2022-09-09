def func(n):
    for i in range(2,n):
        if n % i == 0:
            print('{}不是素数'.format(n))
            break
    else:
        print('{0}是素数'.format(n))
print('请输入一个整数，以判断它是不是一个素数')
func(791)