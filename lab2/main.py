from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import matplotlib.pyplot as plt

def main():
    print("ИУ5-51Б Забелина Варвара Лаб2")
    r = Rectangle("синего", 10, 10)
    c = Circle("зеленого", 10)
    s = Square("красного", 10)
    print(r)
    print(c)
    print(s)

    plt.plot((3, 1, 2, 3, 4, 5, 3), (0, 2, 3, 2, 3, 2, 0))
    plt.show()

if __name__ == "__main__":
    main()