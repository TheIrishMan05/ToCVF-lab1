import numpy as np
import matplotlib.pyplot as plt


class MandelbrotSet:
    def __init__(self, min_x, min_y, max_x, max_y, iterations, amount_x_points, amount_y_points, inf_border):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.iterations = iterations
        self.amount_x_points = amount_x_points
        self.amount_y_points = amount_y_points
        self.inf_border = inf_border

    def count_c(self, min_x, min_y, max_x, max_y, amount_x_points, amount_y_points):
        x, y = np.mgrid[min_x:max_x:(amount_x_points * 1j), min_y:max_y:(amount_y_points * 1j)]
        return x + y * 1j

    def count_z(self, c):
        return np.zeros_like(c)

    def create_image(self, z, c, iterations, inf_border, amount_x_points, amount_y_points):
        image = np.zeros((amount_x_points, amount_y_points))
        for i in range(iterations):
            z = z ** 2 + c
            mask = (np.abs(z) > inf_border) & (image == 0)
            image[mask] = i
            z[mask] = np.nan
        return -image.T

    def draw(self, image):
        plt.xticks([])
        plt.yticks([])
        plt.imshow(image, cmap='flag', interpolation='none')
        plt.show()

    def validate(self, c, iterations):
        if c is not None and abs(c) > 2:
            print("c не определено или модуль этого числа больше 2")
            return False
        if iterations < 100:
            print("Число итераций должно быть не менее 100")
