import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

x= np.array([[1,2],[3,4],[1,4],[4,4],[1,0],[4,2]])

km = KMeans(n_clusters=2)
km.fit(x)

labels = km.labels_
cen=km.cluster_centers_

plt.scatter(x[:,0],x[:,1])
plt.scatter(cen[:,0],cen[:,1],marker='X',color = 'red')
plt.show()