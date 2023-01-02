import cv2
import os
from glob import glob


def edge(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    img_edge = cv2.adaptiveThreshold(img, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=5,
                                     C=10)

    save_filename = '%s.jpeg' % (os.path.basename(filename).split('.')[0])
    cv2.imwrite('edges/' + save_filename, img_edge)


if __name__ == "__main__":
    if not os.path.exists('edges'):
        os.makedirs('edges')
    file_list = glob('images/*.jpeg')
    for filename in file_list:
        edge(filename)