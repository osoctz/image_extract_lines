import cv2


def edge(filename):
    image = cv2.imread(filename)
    # 将BGR图像转换为灰度
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 图像反转
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # cv2.imshow("原图", image)
    # cv2.imshow("铅笔素描", pencil_sketch)
    # cv2.waitKey(0)

    cv2.imwrite('edges/chbaobao.jpeg', pencil_sketch)


if __name__ == "__main__":
    edge('images/chbaobao.jpeg')
