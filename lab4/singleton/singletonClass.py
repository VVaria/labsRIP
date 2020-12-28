class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    file = "file.txt"
    def return_file(cls):
        f = open(cls.file, 'r')
        line = f.read()
        f.close()
        return line

    def write_file(cls, l):
        f = open(cls.file, 'a')
        f.write(l)
        f.close()
