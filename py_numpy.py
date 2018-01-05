import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('.\images\lena.png')

plt.imshow(img)
plt.show()
