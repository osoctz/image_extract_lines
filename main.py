# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np


def extract(source, target):
    im = Image.open(source).convert('L')  # jpg是这里将用于转换的原图
    a = np.asarray(im).astype('float')  # 将图像以灰度图的方式打开并将数据转为float存入np中.

    depth = 5  # (0-100)
    grad = np.gradient(a)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)  # 构造x和y轴梯度的三维归一化单位坐标系
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化,(梯度和光源相互作用，将梯度转化为灰度)
    b = b.clip(0, 255)

    im2 = Image.fromarray(b.astype('uint8'))  # 重构图像

    im2.save(target)  # 保存得到的手绘图片
    im2.show()  # 展示


if __name__ == '__main__':
    extract('baojinz.jpeg', 'baojinz-line.jpeg')
