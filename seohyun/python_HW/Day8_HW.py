import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
my_matrix=np.array([
    [[66,136,199],[66,136,199],[255,242,0],[66,136,199],[66,136,199],[66,136,199],[66,136,199],[66,136,199]],
    [[66,136,199],[66,136,199],[255,242,0],[66,136,199],[66,136,199],[66,136,199],[66,136,199],[66,136,199]],
    [[255,242,0],[255,242,0],[255,242,0],[255,242,0],[255,242,0],[255,242,0],[255,242,0],[255,242,0]],
    [[66,136,199],[66,136,199],[255,242,0],[66,136,199],[66,136,199],[66,136,199],[66,136,199],[66,136,199]],
    [[66,136,199],[66,136,199],[255,242,0],[66,136,199],[66,136,199],[66,136,199],[66,136,199],[66,136,199]]
])
plt.imshow(my_matrix)
plt.show()

my_matri=np.array([
    [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[255,242,0],[255,242,0],[255,242,0],[255,242,0],[255,242,0]]
])
plt.imshow(my_matri)
plt.show()

my_matr=np.array([
    [[34,177,76],[255,255,255],[255,0,0]],
    [[34,177,76],[255,255,255],[255,0,0]]
])
plt.imshow(my_matr)
plt.show()

