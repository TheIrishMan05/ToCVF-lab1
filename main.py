from mandelbrot_set import MandelbrotSet


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
                pass
                continue
            elif input_val == "KochSnowflake":
                pass
                continue
        except ValueError as ve:
            print("Oops! Error has occured: " + str(ve))
            continue
        except KeyboardInterrupt:
            print("Program exit has been called!")
            break


run()
