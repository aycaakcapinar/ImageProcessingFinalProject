import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as img
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans


def find_color_palette(img):
    img = cv2.imread(img, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((img.shape[1]*img.shape[0], 3))
    kmeans = KMeans(n_clusters=5)
    s = kmeans.fit(img)
    labels = kmeans.labels_
    labels = list(labels)
    centroid = kmeans.cluster_centers_
    colors = np.array(centroid/255)
    percent = []
    for i in range(len(centroid)):
        j = labels.count(i)
        j = j/(len(labels))
        percent.append(j)

    return colors, percent
