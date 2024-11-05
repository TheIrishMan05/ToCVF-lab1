class KochSnowflake:
    __ln = None
    __t = None

    def __init__(self):
        print("Создан экземпляр класса снежинки Коха")

    def set_ln(self, ln):
        self.__ln = ln

    def get_ln(self):
        return self.__ln

    def get_t(self):
        return self.__t

    def set_t(self, t):
        self.__t = t

    def start(self, t):
        t.forward(20)
        t.fd(20)
        t.left(90)
        t.fd(20)
        t.right(120)
        t.fd(40)

    def draw_koch_segment(self, t, ln):
        if ln > 6:
            ln3 = ln // 3
            self.draw_koch_segment(t, ln3)
            t.left(60)
            self.draw_koch_segment(t, ln3)
            t.right(120)
            self.draw_koch_segment(t, ln3)
            t.left(60)
            self.draw_koch_segment(t, ln3)
        else:
            t.left(60)
            t.fd(ln)
            t.right(120)
            t.fd(ln)
            t.left(60)
            t.fd(ln)
