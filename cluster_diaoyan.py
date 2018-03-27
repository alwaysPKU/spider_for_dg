# 层次聚类
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import cdist, pdist
import numpy as np

X = np.reshape(range(100), [10, 10])
# print(X)

Y = np.reshape(range(10), [1, 10])
# print(Y)

Z = cdist(X, Y, 'cosine')
print(Z)

z = pdist(X, 'cosine')
print(z.shape)
