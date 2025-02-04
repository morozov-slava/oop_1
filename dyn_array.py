import ctypes


class DynArray:
    # Конструктор
    # Постусловие: создан новый пустой динамический массив
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self._create_array(self.capacity)
        # constants
        self.INSERT_OK = 1           # последний вызов метода 'insert()' отработал нормально
        self.INSERT_ERR = 2          # индекс добавляемого элемента находится за пределами размера массива
        self.REMOVE_OK = 1           # последний вызов метода 'remove()' отработал нормально
        self.REMOVE_ERR = 2          # индекс удаляемого элемента находится за пределами размера массива
        self.GET_ITEM_OK = 1         # последний вызов метода 'get_item()' отработал нормально
        self.GET_ITEM_ERR_OUT = 2    # значение индекса является отрицательным
        self.GET_ITEM_ERR_NEG = 3    # индекс запрашиваемого элемента находится за пределами размера массива
        # statuses
        self.insert_status = None
        self.remove_status = None
        self.get_item_status = None

    ## Запросы    
    def _create_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def _resize(self, new_capacity: int):
        # Постусловие: максимальный размер массива и вместимость массива устанавливаются на заданное значение
        new_array = self._create_array(new_capacity)
        for i in range(self.get_count()):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        
    def append(self, itm: object):
        # Постусловие: конец массива добавлен указанный элемент (при необходимости увеличивается буфер)
        if self.get_count() == self.get_capacity():
            self._resize(2 * self.get_capacity())
        self.array[self.get_count()] = itm
        self.count += 1

    def insert(self, i: int, itm: object):
        # Предусловие: указанный индекс находится в пределах размера массива
        # Постусловие: добавлен указанный элемент на место указанного индекса (при необходимости увеличивается буфер)
        if i > self.get_count():
            self.insert_status = self.INSERT_ERR
            return None
        if self.get_count() == self.get_capacity():
            self.resize(2*self.capacity)
        if i == self.get_count():
            self.array[self.get_count()] = itm
            self.count += 1
            self.insert_status = self.INSERT_OK
            return None
        new_array = self._create_array(self.get_capacity())
        for j in range(self.get_count()):
            if j < i:
                new_array[j] = self.array[j]
                continue
            if j == i:
                new_array[j] = itm
            new_array[j+1] = self.array[j]
        self.array = new_array
        self.count += 1
        self.insert_status = self.INSERT_OK

    def remove(self, i: int):
        # Предусловие: указанный индекс находится в пределах размера массива
        # Постусловие: из массива удалён элемент по заданному индексу (при необходимости сжимается буфер)
        if i >= self.get_count():
            self.remove_status = self.REMOVE_ERR
            return None
        # Check capacity (and resize if necessary)
        if ((self.get_count() - 1) / self.get_capacity()) < 0.50:
            new_capacity = int(self.get_capacity() / 1.5)
        else:
            new_capacity = self.get_capacity()
        if new_capacity <= 16:
            new_capacity = 16
        self.capacity = new_capacity
        # Create new array (without deleted element)
        new_array = self._create_array(self.capacity)
        for j in range(self.get_count()-1):
            if j < i:
                new_array[j] = self.array[j]
                continue
            new_array[j] = self.array[j+1]
        self.array = new_array
        self.count -= 1
        self.remove_status = self.REMOVE_OK

    ## Команды
    def __len__(self) -> int:
        return self.count

    def get_count(self) -> int:
        return self.count

    def get_item(self, i: int):
        # Предусловие: указанный индекс находится в пределах размера массива, также указанный индекс не является отрицательным
        if i < 0:
            self.get_item_status = self.GET_ITEM_ERR_NEG
            return None
        if i >= self.get_count():
            self.get_item_status = self.GET_ITEM_ERR_OUT
            return None
        self.get_item_status = self.GET_ITEM_OK
        return self.array[i]

    def get_capacity(self):
        return self.capacity

    def get_array(self):
        return self.array

    ## Дополнительные запросы
    def get_insert_status(self) -> int:
        return self.insert_status

    def get_remove_status(self) -> int:
        return self.remove_status

    def get_get_item_status(self) -> int:
        return self.get_item_status


