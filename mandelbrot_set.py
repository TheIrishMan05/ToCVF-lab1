import matplotlib.pyplot as plt
import numpy as np


class MandelbrotSet:
    __min_x = None
    __min_y = None
    __max_x = None
    __max_y = None
    __iterations = None
    __amount_x_points = None
    __amount_y_points = None
    __inf_border = None

    def __init__(self):
        print("Создан экземпляр класса множества Мандельборта")

    def get_min_x(self):
        return self.__min_x

    def set_min_x(self, min_x):
        self.__min_x = min_x

    def get_min_y(self):
        return self.__min_y

    def set_min_y(self, min_y):
        self.__min_y = min_y

    def get_max_x(self):
        return self.__max_x

    def set_max_x(self, max_x):
        self.__max_x = max_x

    def get_max_y(self):
        return self.__max_y

    def set_max_y(self, max_y):
        self.__max_y = max_y

    def get_iterations(self):
        return self.__iterations

    def get_inf_border(self):
        return self.__inf_border

    def set_inf_border(self, inf_border):
        self.__inf_border = inf_border

    def set_iterations(self, iterations):
        if 100 <= iterations <= 5500:
            self.__iterations = iterations
        else:
            raise ValueError("Количество итерации должно быть больше 100 и не более 5500")

    def get_amount_x_points(self):
        return self.__amount_x_points

    def set_amount_x_points(self, amount_x_points):
        self.__amount_x_points = amount_x_points

    def get_amount_y_points(self):
        return self.__amount_y_points

    def set_amount_y_points(self, amount_y_points):
        self.__amount_y_points = amount_y_points

    def count_c(self, min_x, min_y, max_x, max_y, amount_x_points, amount_y_points):
        x, y = np.mgrid[min_x:max_x:(amount_x_points * 1j), min_y:max_y:(amount_y_points * 1j)]
        return x + y * 1j
    def count_z(self, c):
        if np.abs(c.all()) > 2:
            raise ValueError("Нарушено свойство: |c| <= 2, точки с |c| > 2 не лежат в множестве Мандельборта")
        else:
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
