import matplotlib.pyplot as plt
import numpy as np
import re
print('parametric2D')


funcs=['sin','cos','tan','arcsin','arccos','arctan','sinh','cosh','tanh','arcsinh','arccosh','arctanh','exp','log','log2','log10','sqrt']

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

plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
