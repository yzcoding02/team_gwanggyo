import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
e=np.zeros((10,10))
e[:,:]=3
e[:5,5:]=2
e[5:,5:]=1
plt.imshow(e)
plt.show()