import matplotlib.pylab as plt
import numpy as np
points = np.array([[1,1],[1,2],[1,3],
                [2,1],[2,2],[2,3],
                [3,1],[3,2],[3,3]]
)
print(points)
print(points.shape)

plt.plot(points[:,0], points[:,1],"ro") # r : red , o : circle

n = np.array([2.5,2])
plt.plot(n[0],n[1],"o")

plt.show()
