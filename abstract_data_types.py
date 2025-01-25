class BoundedStackAbstract:
    """
    АТД BoundedStack
    """
    # Конструктор
    # Постусловие: создан новый пустой ограниченный стек
    def __init__(self, capacity: int = 32):
        self.capacity = capacity # максимальное допустимое кол-во элементов в стеке (значение параметра по умолчанию: 32)
        # constants
        self.POP_NIL = 0   # метод pop() ещё не вызывался
        self.POP_OK = 1    # последний вызов метода pop() отработал нормально
        self.POP_ERR = 2   # стек пуст
        
        self.PEEK_NIL = 0  # метод peek() ещё не вызывался
        self.PEEK_OK = 1   # последний вызов метода peek() вернул корректное значение 
        self.PEEK_ERR = 2  # стек пуст

        self.PUSH_NIL = 0  # метод push() ещё не вызывался
        self.PUSH_OK = 1   # последний вызов метода push() отработал нормально
        self.PUSH_ERR = 2  # стек заполнен

    # Команды:
    def push(self, value: int) -> None:
        # Предусловие: размер стека должен быть меньше, чем capacity
        # Постусловие: в стек добавлено новое значение
        raise NotImplementedError()
        
    def pop(self):
        # Предусловие: стек не пустой; 
        # Постусловие: из стека удалён верхний элемент
        raise NotImplementedError()

    def clear(self) -> None:
        # Постусловие: из стека удалятся все значения
        raise NotImplementedError()

    # Запросы:
    def peek(self) -> int:
        # Предусловие: стек не пустой
        raise NotImplementedError()

    def size(self) -> int:
        raise NotImplementedError()

    # Дополнительные запросы
    def get_pop_status(self) -> int:
        # возвращает значение POP_*
        raise NotImplementedError()

    def get_peek_status(self) -> int:
        # возвращает значение PEEK_*
        raise NotImplementedError()
        
    def get_push_status(self) -> int:
        # возвращает значение PUSH_*
        raise NotImplementedError()


class BoundedStack:
    def __init__(self, capacity: int = 32):
        self.capacity = capacity
        self.stack = []
        # constants
        self.POP_NIL = 0
        self.POP_OK = 1
        self.POP_ERR = 2
        self.PEEK_NIL = 0
        self.PEEK_OK = 1
        self.PEEK_ERR = 2
        self.PUSH_NIL = 0
        self.PUSH_OK = 1
        self.PUSH_ERR = 2
        # statuses
        self.peek_status = self.PEEK_NIL
        self.pop_status = self.POP_NIL
        self.push_status = self.PUSH_NIL

    def push(self, value: int) -> None:
        if self.size() >= self.capacity:
            self.push_status = self.PUSH_ERR
        else:
            self.stack.append(value)
            self.push_status = self.PUSH_OK
        
    def pop(self) -> None:
        if self.size() > 0:
            self.stack.pop()
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

    def clear(self) -> None:
        self.stack = []
        self.peek_status = self.PEEK_NIL
        self.pop_status = self.POP_NIL
        self.push_status = self.PUSH_NIL

    def peek(self) -> int:
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = 0
            self.peek_status = self.PEEK_ERR
        return result

    def size(self) -> int:
        return len(self.stack)

    def get_pop_status(self) -> int:
        return self.pop_status

    def get_peek_status(self) -> int:
        return self.peek_status

    def get_push_status(self) -> int:
        return self.push_status


