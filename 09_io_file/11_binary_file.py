
import samples.bmp as bmp
import reprlib
import samples.fractal as fractal

pixels = fractal.mandelbrot(448, 256)

print(reprlib.repr(pixels))

bmp.write_grayscale("09_io_file/mandel.bmp", pixels)

dim = bmp.dimensions("09_io_file/mandel.bmp")
print(dim)
