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


