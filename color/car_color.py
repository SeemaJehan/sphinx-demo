
from sklearn.cluster import KMeans
import numpy as np
import webcolors


def car_color(frame: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> str:
    """predicts car color 

    Args:
        frame (np.ndarray): input image 
        x1 (int): x-coordinate of the top left of the bounding box
        y1 (int): y-coordinate of the top left of the bounding box
        x2 (int): width of the bounding box
        y2 (int): height of the bounding box

    Returns:
        str: car color
    """
    X, Y, W, H = int(x1), int(y1), int(x2), int(y2)
    img = frame[Y:H, X:W]
    height, width, dim = img.shape
    img_vec = np.reshape(img, [height * width, dim])

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(img_vec)

    unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
    sort_ix = np.argsort(counts_l)
    sort_ix = sort_ix[::-1]

    b, g, r = kmeans.cluster_centers_[sort_ix[0]]

    requested_colour = (int(r), int(g), int(b))
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name   
    clr_name = min_colours[min(min_colours.keys())]
    return clr_name
