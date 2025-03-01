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


