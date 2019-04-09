from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import re

funcs=['sin','cos','tan','arcsin','arccos','arctan','sinh','cosh','tanh','arcsinh','arccosh','arctanh','exp','log','log2','log10','sqrt']

print('surface3D')
xmin=float(input('insert x starting value:'))
xmax=float(input('insert x end value:'))

ymin=float(input('insert y starting value:'))
ymax=float(input('insert y end value:'))

resolution = float(input('insert resolution (4 recommended!):'))

f = input('insert z in terms of x,y:')


fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(xmin, xmax, resolution)
y = np.arange(ymin, ymax, resolution)
x, y = np.meshgrid(x, y)

for i in range(len(funcs)):
    replaced = re.sub(funcs[i], 'np.'+funcs[i],f)
    f=replaced
fx=re.sub('np.np.', 'np.',f)
fx=re.sub('arcnp.', 'np.arc',f)
z = eval(f)

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
