from koch_snowflake import KochSnowflake
from mandelbrot_set import MandelbrotSet
from julia_set import JuliaSet
import turtle
import pygame
import os


def run():
    while True:
        try:
            input_val = input("Введите класс кривой для отрисовки: ")
            if input_val == "MandelbrotSet":
                mandelbrot_set = MandelbrotSet()
                mandelbrot_set.set_min_x(float(input("Введите min_x: ")))
                mandelbrot_set.set_min_y(float(input("Введите min_y: ")))
                mandelbrot_set.set_max_x(float(input("Введите max_x: ")))
                mandelbrot_set.set_max_y(float(input("Введите max_y: ")))
                mandelbrot_set.set_iterations(int(input("Введите количество итераций: ")))
                mandelbrot_set.set_amount_x_points(int(input("Введите количество точек по оси x: ")))
                mandelbrot_set.set_amount_y_points(int(input("Введите количество точек по оси y: ")))
                mandelbrot_set.set_inf_border(float(input("Введите границу для бесконечности: ")))
                c = mandelbrot_set.count_c(mandelbrot_set.get_min_x(), mandelbrot_set.get_min_y(),
                                           mandelbrot_set.get_max_x(), mandelbrot_set.get_max_y(),
                                           mandelbrot_set.get_amount_x_points(), mandelbrot_set.get_amount_y_points())
                z = mandelbrot_set.count_z(c)
                image = mandelbrot_set.create_image(z, c, mandelbrot_set.get_iterations(),
                                                    mandelbrot_set.get_inf_border(),
                                                    mandelbrot_set.get_amount_x_points(),
                                                    mandelbrot_set.get_amount_y_points())
                mandelbrot_set.draw(image)
                continue
            elif input_val == "JuliaSet":
                julia_set = JuliaSet()
                white = (255, 255, 255)
                x = 20
                y = 40
                os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
                pygame.init()
                w = 1200
                h = 800
                julia_set.set_sc(pygame.display.set_mode((w, h)))
                pygame.display.set_caption("Множества Жюлиа")
                julia_set.get_sc().fill(white)
                fps = 30
                clock = pygame.time.Clock()
                julia_set.set_center(complex(float(input("Введите Re(c): ")), float(input("Введите Im(z): "))))
                julia_set.set_scale_c(float(input("Введите коэффициент масштабирования: ")))
                julia_set.set_iterations(int(input("Введите количество итераций: ")))
                julia_set.set_x_view(int(input("Введите координату x для смещения обзора: ")))
                julia_set.set_y_view(int(input("Введите координату y для смещения обзора: ")))
                julia_set.draw_points(julia_set.get_sc(), julia_set.get_iterations(),
                                      julia_set.get_scale_c(), julia_set.get_x_view(), julia_set.get_y_view(),
                                      julia_set.get_center())
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    clock.tick(fps)
            elif input_val == "KochSnowflake":
                koch_snowflake = KochSnowflake()
                koch_snowflake.set_t(turtle.Turtle())
                koch_snowflake.set_ln(float(input("Введите длину линейного сегмента: ")))
                iterations = int(input("Введите количество итераций: "))
                koch_snowflake.get_t().ht()
                koch_snowflake.get_t().speed(1000)
                option = input("Выберите вариант снежинки Коха(обычный, реверсивный): ")
                if option == "реверсивный":
                    koch_snowflake.get_t().ht()
                    koch_snowflake.get_t().speed(1000)
                    for _ in range(iterations):
                        koch_snowflake.draw_koch_segment(koch_snowflake.get_t(), koch_snowflake.get_ln())
                        koch_snowflake.get_t().left(120)
                    turtle.done()
                    continue
                elif option == "обычный":
                    koch_snowflake.get_t().ht()
                    koch_snowflake.get_t().speed(1000)
                    for _ in range(iterations):
                        koch_snowflake.draw_koch_segment(koch_snowflake.get_t(), koch_snowflake.get_ln())
                        koch_snowflake.get_t().right(120)
                    turtle.done()
                    continue
                else:
                    continue
        except ValueError as ve:
            print("Oops! Error has occured: " + str(ve))
            continue
        except KeyboardInterrupt:
            print("Program exit has been called!")
            break


run()
