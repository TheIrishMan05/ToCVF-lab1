import pygame


class JuliaSet:
    __center = None
    __iterations = None
    __x_view = None
    __y_view = None
    __sc = None
    __scale_c = None

    def __init__(self):
        print("Создан экземпляр класса множества Жюлиа")

    def get_iterations(self):
        return self.__iterations

    def set_iterations(self, iterations):
        self.__iterations = iterations

    def set_center(self, center):
        self.__center = center

    def get_center(self):
        return self.__center

    def set_x_view(self, x_view):
        self.__x_view = x_view

    def get_x_view(self):
        return self.__x_view

    def set_y_view(self, y_view):
        self.__y_view = y_view

    def get_y_view(self):
        return self.__y_view

    def set_sc(self, sc):
        self.__sc = sc

    def get_sc(self):
        return self.__sc

    def set_scale_c(self, scale_c):
        self.__scale_c = scale_c

    def get_scale_c(self):
        return self.__scale_c

    def draw_points(self, sc, iterations, scale_c, x_view, y_view, c):
        width, height = sc.get_size()
        scale = min(width, height) / scale_c
        view = (x_view, y_view)
        for y in range(-height // 2 + view[1], height // 2 + view[1]):
            for x in range(-width // 2 + view[0], width // 2 + view[0]):
                a = x / scale
                b = y / scale
                z = complex(a, b)
                n = 0
                for n in range(iterations):
                    z = z ** 2 + c
                    if abs(z) > 2:
                        break

                if n == iterations - 1:
                    r = g = b = 0
                else:
                    r = (n % 2) * 32 + 128
                    g = (n % 4) * 64
                    b = (n % 2) * 16 + 128

                pygame.draw.circle(sc, (r, g, b), (x + width // 2 - view[0], y + height // 2 - view[1]), 1)

        pygame.display.flip()
