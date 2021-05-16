import matplotlib.pyplot as plt
import numpy as np


def roots(a, b, c):
    D = b ** 2 - 4 * a * c
    d = D ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    if D > 0:
        return x1, x2
    elif x1 == x2:
        return x1
    else:
        exit('Complex roots')


k1, k2, k3 = 4, 15, 3

roots = roots(k1, k2, k3)
if isinstance(roots, tuple):
    x1, x2 = roots
    points = x1, x2
    print(points)
    y0 = 0, 0
    plt.scatter(points, y0, color='red')
else:
    x = roots
    points = x
    y0 = 0
    plt.scatter(points, y0, color='red')

freq = 100  # частота дискретизации типо
a, b = -10, 10  # здесь ручками выставляем пределы по оси икс

# квадратичная функция
xi = np.linspace(a, b, freq)
y = [k1 * t * t + k2 * t + k3 for t in xi]
plt.plot(xi, y)

plt.grid()
plt.show()

# import matplotlib.pyplot as plt
#
#
# x = [i for i in range(10)]
#
#
# def y(x):
#     return [i * i for i in x]
#
#
# plt.plot(x, y(x))
# plt.show()
