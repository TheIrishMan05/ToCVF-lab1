from mandelbrot_set import MandelbrotSet


def run():
    while True:
        input_val = input("Введите класс кривой для отрисовки: ")
        if input_val == "MandelbrotSet":
            min_x = float(input("Введите min_x: "))
            min_y = float(input("Введите min_y: "))
            max_x = float(input("Введите max_x: "))
            max_y = float(input("Введите max_y: "))
            iterations = int(input("Введите количество итераций: "))
            amount_of_x_points = int(input("Введите количество точек по оси x: "))
            amount_of_y_points = int(input("Введите количество точек по оси y: "))
            inf_border = float(input("Введите границу для бесконечности: "))
            mandelbrot_set = MandelbrotSet(min_x, min_y, max_x, max_y, iterations,
                                           amount_of_x_points, amount_of_y_points, inf_border)
            c = mandelbrot_set.count_c(min_x, min_y, max_x, max_y, amount_of_x_points, amount_of_y_points)
            z = mandelbrot_set.count_z(c)
            image = mandelbrot_set.create_image(z, c, iterations, inf_border, amount_of_x_points, amount_of_y_points)
            mandelbrot_set.draw(image)
            continue
        elif input_val == "JuliaSet":
            z = int(input())
            continue
        elif input_val == "KochSnowflake":
            z = int(input())
            continue
        continue


run()
