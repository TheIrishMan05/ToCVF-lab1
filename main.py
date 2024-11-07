from koch_snowflake import KochSnowflake
from mandelbrot_set import MandelbrotSet
import turtle
import pygame


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
                width, height = 800, 800
                pygame.init()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption("Множество Жюлиа")

                center = complex(-1, 0)
                zoom = 1
                move_x, move_y = 0, 0
                max_iter = 300

                def julia(x, y, j_c):
                    j_z = complex(x, y)
                    for i in range(max_iter):
                        j_z = j_z * j_z + j_c
                        if abs(z) > 2:
                            return i
                    return max_iter

                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                    for cx in range(width):
                        for cy in range(height):
                            zx = 1.5 * (cx - width / 2) / (0.5 * zoom * width) + move_x
                            zy = (cy - height / 2) / (0.5 * zoom * height) + move_y
                            color = julia(zx, zy, center)
                            screen.set_at((cx, cy), (color % 8 * 32, color % 16 * 16, color % 32 * 8))

                    pygame.display.flip()

                pygame.quit()
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
