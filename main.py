import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 40, 100)
x2 = np.linspace(0, 40, 100)

# Создаем сетку X1 и X2
X1, X2 = np.meshgrid(x1, x2)

#Параметры графика
plt.figure(figsize=(8, 6))
plt.xlabel('x1')
plt.ylabel('x2')

# Ограничение
plt.plot(x1, (141 - 4 * x1) / 5, label='4*X1 + 5*X2 = 141', color='blue', linestyle='dotted')

plt.axvline(x=19, color='purple', linestyle='dotted', label='x1=19')  
plt.axhline(y=17, color='orange', linestyle='dotted', label='x2=17') 

plt.arrow(0, 0, 3, 5, head_width=0.5, head_length=0.7, fc='red', ec='red', label='вектор z (3, 5)') 

#Перпендикуляр к вектору Z
perpendicular_x = np.array([5, -5])
perpendicular_y = np.array([-3, 3])

plt.plot(perpendicular_x, perpendicular_y, linestyle='dotted', color='green', label='перпендикуляр')  

plt.title('Линейная функция')

# Добавление текстовых меток
plt.text(10, 16, '4*X1 + 5*X2 = 141', fontsize=10, color='blue', rotation=-38.7)
plt.text(20, 5, 'x1=19', fontsize=10, color='purple', rotation=270)  
plt.text(5, 17.5, 'x2=17', fontsize=10, color='orange') 
plt.text(3, 2.5, 'z (3, 5)', fontsize=10, color='red') 

plt.grid(True)
plt.legend()
plt.show() 
