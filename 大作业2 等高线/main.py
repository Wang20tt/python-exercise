import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

x = np.arange(-2.0, 2.0, 0.01)
y = np.arange(-2.0, 2.0, 0.01)
m, n = np.meshgrid(x, y)        # 生成网格点坐标矩阵


# 指定一个函数用于计算每个点的高度，也可以直接使用二维数组储存每个点的高度
def f(a, b):
    return (1 - b ** 5 + a ** 5) * np.exp(-a ** 2 - b ** 2)


# 绘制等高线图，8 个数据间隔，颜色为 plasma
plt.contourf(m, n, f(m, n), 8, cmap='plasma')
C = plt.contour(m, n, f(m, n), 8, cmap='plasma')
# 添加标记，标记处不显示轮廓线，颜色为黑色，保留两位小数
plt.clabel(C, inline=True, colors='k', fmt='%1.2f')
# 显示颜色条
plt.colorbar()
plt.title('等高线图颜色填充示例')
plt.xlabel('x axis label')
plt.ylabel('y axis label')

plt.show()