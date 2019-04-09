

import subprocess
input = input('0 for parametric3D \n1 for surface3D \n:')
if input == '0':
    subprocess.call("python3 parametric3D.py", shell=True)
elif input == '1':
    subprocess.call("python3 surface3D.py", shell=True)
else:
    print('please insert a number')
