def enigma(x, y, z):
    if x == len(y):
        return (z)
    elif x < len(y):
        return (y[x:])
    else:
        s = foo(z)
        return (s + y)


def foo(w):
    r = ""
    for i in range(len(w) - 1, -1, -1):
        r = r + w[i]
    return (r)


one = enigma(7, "caramel", "dulce de leche")
two = enigma(3, "cupcake", "vanilla")
three = enigma(10, "pie", "nomel")

print(one, two, three)

#################################################################################

# gets average color of an image

import numpy as np
import matplotlib.pyplot as plt


def avg(img):
    # Displays the average color of the input image object (numpy array)
    img[:, :, 0] = np.average(img[:, :, 0])  # red
    img[:, :, 1] = np.average(img[:, :, 1])  # green
    img[:, :, 2] = np.average(img[:, :, 2])  # blue
    plt.imshow(img)
    plt.show()


def main():
    # can create image or load existing one
    my_img = np.ones((50, 50, 3))
    my_img[::2, :, 0] = 0  # cyan
    my_img[1::2, :, 1] = 0  # magenta
    plt.imshow(my_img)
    plt.show()
    avg(my_img)

    in_img = plt.imread("purpleandyellow.png")
    plt.imshow(in_img)
    plt.show()
    avg(in_img)


main()
