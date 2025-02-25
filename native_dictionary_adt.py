class NativeDictionary:
    # Конструктор
    # Постусловие: создан новый пустой ассоциативный массив указанного размера
    def __init__(self, capacity: int):
        self.capacity = capacity                 # Максимально допустимый размер  массива
        self.slots = [None] * self.capacity
        self.values = [None] * self.capacity
        self._size = 0
        # Constants
        self.PUT_OK = 1                          # Последний вызов метода `put` отработал нормально
        self.PUT_CAPACITY_ERR = 2                # В массике недостаточно места
        self.PUT_COLLISION_ERR = 3               # Коллизия при добавлении элемента
        self.REMOVE_OK = 1                       # Последний вызов метода `remove` отработал нормально
        self.REMOVE_ERR = 2                      # Искомого ключа нет в массиве
        # Statuses
        self.put_status = None
        self.remove_status = None

    def _hash_fun(self, key: str):
        index = sum([(i + ord(x)) for i, x in enumerate(key)]) % self.capacity
        return index

    ## Запросы
    # Предусловие: в массиве есть свободный слот
    # Постусловие: в массив добавлен новый элемент со значением
    def put(self, key: str, value: object) -> None:
        if self.size() >= self.capacity:
            self.put_status = self.PUT_CAPACITY_ERR
            return None
        i = self._hash_fun(key)
        if self.slots[i] is not None:
            self.put_status = self.PUT_COLLISION_ERR
            return None
        self.slots[i] = key 
        self.values[i] = value
        self._size += 1
        self.put_status = self.PUT_OK

    # Предусловие: в таблице имеется значение по ключу key
    # Постусловие: из таблицы удалено значение по ключу key
    def remove(self, key: str) -> None:
        i = self._hash_fun(key)
        if self.slots[i] is None:
            self.remove_status = self.REMOVE_ERR
            return None
        self.slots[i] = None
        self.values[i] = None
        self._size -= 1
        self.remove_status = self.REMOVE_OK

    ## Команды
    def size(self) -> int:
        # Получить размер массива
        return self._size
    
    def get(self, key: str) -> object:
        # Получить значение массива по его ключу
        i = self._hash_fun(key)
        if self.slots[i] == key:
            return self.values[i]
        
    ## Statuses
    def get_put_status(self):
        return self.put_status

    def get_remove_status(self):
        return self.remove_status
        

