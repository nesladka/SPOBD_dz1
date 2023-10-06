import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 40, 100)
x2 = np.linspace(0, 40, 100)

X1, X2 = np.meshgrid(x1, x2)

plt.figure(figsize=(8, 6))
plt.xlabel('x1')
plt.ylabel('x2')

plt.plot(x1, (141 - 4 * x1) / 5, label='4*X1 + 5*X2 = 141', color='blue', linestyle='dotted')

plt.axvline(x=19, color='purple', linestyle='dotted', label='x1=19')  
plt.axhline(y=17, color='orange', linestyle='dotted', label='x2=17') 

plt.arrow(0, 0, 3, 5, head_width=0.5, head_length=0.7, fc='red', ec='red', label='вектор z (3, 5)') 

perpendicular_x = np.array([5, -5])
perpendicular_y = np.array([-3, 3])
