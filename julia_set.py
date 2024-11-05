import matplotlib as plt


class JuliaSet:
    __center = None
    __iterations = None
    __start_range = None
    __min_x = None
    __max_x = None
    __min_y = None
    __points_x = None
    __points_y = None

    def __init__(self):
        print("Создан экземпляр класса JuliaSet")

    def set_min_x(self, min_x):
        self.__min_x = min_x

    def get_min_x(self):
        return self.__min_x

    def set_max_x(self, max_x):
        self.__max_x = max_x

    def get_max_x(self):
        return self.__max_x

