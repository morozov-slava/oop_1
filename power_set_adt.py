class PowerSet:
    # Конструктор
    # Постусловие: создано пустое множество
    def __init__(self):
        self.hash_table = {}
        self._size = 0
        # Constants
        self.PUT_OK = 1              # Последний вызов метода `put` отработал нормально
        self.PUT_ERR = 2             # Элемент с указанным значением уже присутствует в множестве
        self.REMOVE_OK = 1           # Последний вызов метода `remove` отработал нормально
        self.REMOVE_ERR = 2          # Указанного значения нет в множестве
        self.GET_OK = 1              # Последний вызов метода `get` отработал нормально
        self.GET_ERR = 2             # Указанного значения нет в множестве
        # Statuses
        self.put_status = None
        self.remove_status = None
        self.get_status = None

    def _hash_func(self, value: str):
        return hash(value)

    ## Запросы 
    # Предусловие: указанный элемент отсутствует в множестве
    # Постусловие: во множество добавлен новый элемент с указанным значением
    def put(self, value: str) -> None:
        if self.is_value(value):
            self.put_status = self.PUT_ERR
            return None
        i = self._hash_func(value)
        self.hash_table[i] = value 
        self.put_status = self.PUT_OK
        self._size += 1

    # Предусловие: заданное значение присутствует в множестве
    # Постусловие: заданное значение удалено из множества
    def remove(self, value: str) -> None:
        if not self.is_value(value):
            self.remove_status = self.REMOVE_ERR
            return None
        i = self._hash_func(value)
        if self.hash_table[i] == value:
            del self.hash_table[i]
            self.remove_status = self.REMOVE_OK
            self._size -= 1
        
    ## Команды
    def intersection(self, OtherSet):
        intersected_ps = PowerSet()
        for value in OtherSet.get_values():
            if self.is_value(value):
                intersected_ps.put(value)
        return intersected_ps

    def union(self, OtherSet):
        union_ps = PowerSet()
        for value in self.get_values():
            union_ps.put(value)
        for value in OtherSet.get_values():
            if not union_ps.is_value(value):
                union_ps.put(value)
        return union_ps

    def difference(self, OtherSet):
        difference_ps = PowerSet()
        for value in self.get_values():
            if not OtherSet.is_value(value):
                difference_ps.put(value)
        return difference_ps

    def is_subset(self, OtherSet) -> bool:
        for value in OtherSet.get_values():
            if not self.is_value(value):
                return False
        return True

    def equals(self, OtherSet) -> bool:
        if self.size() != OtherSet.size():
            return False
        for value in OtherSet.get_values():
            if not self.is_value(value):
                return False
        return True

    # Предусловие: указанное значение присутствует в множестве
    def is_value(self, value: object) -> bool:
        # Проверяет наличие указанного значения в множестве
        i = self._hash_func(value)
        if (i in self.hash_table) and (self.hash_table[i] == value):
            return True
        return False

    def size(self) -> int:
        # Возвращает текущий размер (мощность) множества
        return self._size
    
    ## Дополнительные запросы
    def get_values(self):
        # Возвращает перечень всех значений множества
        return self.hash_table.values()
    
    ## Статусы
    def get_put_status(self) -> int:
        return self.put_status

    def get_remove_status(self) -> int:
        return self.remove_status









class HashTable:
    # Конструктор
    # Постусловие: создана новая пустая хэш-таблица заданного размера
    def __init__(self, capacity: int):
        self.capacity = capacity      # Максимальный допустимый размер хэш-таблицы
        self.hash_table = {}
        self._size = 0
        # Constants
        self.PUT_OK = 1               # Последний вызов метода `put` отработал нормально
        self.PUT_CAPACITY_ERR = 2     # В хэш-таблице недостаточно места
        self.PUT_COLLISION_ERR = 3    # Коллизия при добавлении элемента
        # Statuses
        self.put_status = None

    def _hash_fun(self, value: str):
        key = sum([(i + ord(x)) for i, x in enumerate(value)])
        return key


    ## Запросы
    # Предусловие: в хэш-таблице есть место
    # Постусловие: в хэш-таблицу добавлен новый элемент со значением
    def put(self, value: str) -> None:
        if self.size() >= self.get_capacity():
            self.put_status = self.PUT_CAPACITY_ERR
            return None
        key = self._hash_fun(value)
        if key in self.hash_table:
            self.put_status = self.PUT_COLLISION_ERR
            return None
        self.hash_table[key] = value
        self._size += 1
        self.put_status = self.PUT_OK

    # Постусловие: из хэш-таблицы удалён заданный элемент
    def remove(self, value: str) -> None:
        key = self._hash_fun(value)
        if key in self.hash_table:
            del self.hash_table[key]
            self._size -= 1

    # Постусловие: установлен новый максимальный допустим размер хэш-таблицы
    def resize(self, new_capacity: int):
        self.capacity = new_capacity


    ## Команды
    def find(self, value: str) -> object:
        key = self._hash_fun(value)
        if key in self.hash_table:
            return key

    def size(self) -> int:
        return self._size
    

    ## Additional commands
    def get_capacity(self) -> int:
        return self.capacity


    ## Statuses
    def get_put_status(self) -> int:
        return self.put_status


