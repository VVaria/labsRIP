# используется для сортировки
from operator import itemgetter

class Browser:
    """Браузер"""
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.memory = size
        self.comp_id = comp_id

class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BrowComp:
    """
    'Браузеры компьютера' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, comp_id, brow_id):
        self.comp_id = comp_id
        self.brow_id = brow_id

# Компьютеры
comps = [
    Computer(1, 'ASUS Zenbook 14"'),
    Computer(2, 'Dell XPS 15'),
    Computer(3, 'Macbook 13.3'),

    Computer(11, 'ASUS Zenbook 14" (другой)'),
    Computer(22, 'Dell XPS 15 (другой)'),
    Computer(33, 'Macbook 13.3 (другой)'),
]

# Браузеры
brows = [
    Browser(1, 'Microsoft Edge', 400, 1),
    Browser(2, 'Opera', 210, 1),
    Browser(3, 'Firefox', 270, 2),
    Browser(4, 'Chrome', 237, 2),
    Browser(5, 'Safari', 600, 3),
]

brow_comp = [
    BrowComp(1,1),
    BrowComp(1,2),
    BrowComp(2,3),
    BrowComp(2,4),
    BrowComp(3,5),

    BrowComp(11,1),
    BrowComp(11,2),
    BrowComp(22,3),
    BrowComp(22,4),
    BrowComp(33,5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(b.name, b.memory, c.name) 
        for c in comps 
        for b in brows 
        if b.comp_id==c.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, bc.comp_id, bc.brow_id) 
        for c in comps 
        for bc in brow_comp 
        if c.id==bc.comp_id]
    
    many_to_many = [(b.name, b.memory, comp_name) 
        for comp_name, comp_id, brow_id in many_to_many_temp
        for b in brows if b.id==brow_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все компьютеры
    for c in comps:
        # Список бразузеров компьютера
        c_brows = list(filter(lambda i: i[2]==c.name, one_to_many))
        # Если компьютер не пустой        
        if len(c_brows) > 0:
            # Занятая память бразуерами в компьютере
            c_size = [memory for _,memory,_ in c_brows]
            # Суммарная память браузеров в компьютере
            c_size_sum = sum(c_size)
            res_12_unsorted.append((c.name, c_size_sum))

    # Сортировка по суммарной памяти
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все компьютеры
    for c in comps:
        if 'ASUS' in c.name:
            # Список браузеров компьютера
            c_brows = list(filter(lambda i: i[2]==c.name, many_to_many))
            # Только название бразузеров
            c_brows_names = [x for x,_,_ in c_brows]
            # Добавляем результат в словарь
            # ключ - компьютер, значение - список браузеров
            res_13[c.name] = c_brows_names

    print(res_13)

if __name__ == '__main__':
    main()

