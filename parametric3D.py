import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
print('parametric3D')

#the most used math functions
funcs=['sin','cos','tan','arcsin','arccos','arctan','sinh','cosh','tanh','arcsinh','arccosh','arctanh','exp','log','log2','log10','sqrt']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#ask for inerval
tmin=float(input('insert starting value:'))
tmax=float(input('insert end value:'))


t=np.array(np.linspace(tmin,tmax,np.abs(int(tmax-tmin)*100)))

fx = input('insert x function in terms of t:')
for i in range(len(funcs)):
    replaced = re.sub(funcs[i], 'np.'+funcs[i],fx)
    fx=replaced
fx=re.sub('np.np.', 'np.',fx)
fx=re.sub('arcnp.', 'np.arc',fx)
x = eval(fx)

fy = input('insert y function in terms of t:')
for i in range(len(funcs)):
    replaced = re.sub(funcs[i], 'np.'+funcs[i],fy)
    fy=replaced
fy=re.sub('np.np.', 'np.',fy)
fy=re.sub('arcnp.', 'np.arc',fy)
y = eval(fy)

fz = input('insert z function in terms of t:')
for i in range(len(funcs)):
    replaced = re.sub(funcs[i], 'np.'+funcs[i],fz)
    fz=replaced
fz=re.sub('np.np.', 'np.',fz)
fz=re.sub('arcnp.', 'np.arc',fz)
z = eval(fz)


ax.plot(x,y,z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
