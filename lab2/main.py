from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 10, 10)
    c = Circle("зеленого", 10)
    s = Square("красного", 10)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()