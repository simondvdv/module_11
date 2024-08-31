import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 50)
y1 = x
y2 = [i**2 for i in x]
plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.title('Линейная зависимость y = x')
plt.xlabel('x')
plt.ylabel('y1, y2')
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()
