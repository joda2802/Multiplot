from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
print('surface3D')
xmin=float(input('insert x starting value:'))
xmax=float(input('insert x end value:'))

ymin=float(input('insert y starting value:'))
ymax=float(input('insert y end value:'))

resolution = float(input('insert resolution (4 recommended!):'))



fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(xmin, xmax, resolution)
y = np.arange(ymin, ymax, resolution)
x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt( x**2+y**2))

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
