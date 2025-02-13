class DummyNode:
    def __init__(self):
        self.prev = None
        self.next = None


class Node(DummyNode):
    def __init__(self, value):
        super().__init__()
        self.value = value


class Queue:
    # Конструктор
    # Постусловие: создана новая пустая очередь 
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0
        # Constants
        self.DEQUEUE_NIL = 0       # метод dequeue ещё не вызывался
        self.DEQUEUE_OK = 1        # последний вызов метода dequeue отработал нормально
        self.DEQUEUE_ERR = 2       # последний вызов метода dequeue отработал с ошибкой
        # Statuses
        self.dequeue_status = None

    ## Запросы
    # Постусловие: в очередь добавлен "головной" элемент
    def enqueue(self, value: object) -> None:
        item = Node(value)
        if self.head.next is None:
            self.head.next = item
            self.tail.prev = item
            item.prev = self.head
            item.next = self.tail
        else:
            tail_node = self.tail.prev
            item.prev = tail_node
            tail_node.next = item 
            self.tail.prev = item
        self._size += 1

    # Предусловие: очередь не должна быть пустой
    # Постусловие: из очереди удалён "хвостовой" элемент
    def dequeue(self) -> object:
        if self.size() == 0:
            self.dequeue_status = self.DEQUEUE_ERR
            return None     
        head_node = self.head.next 
        next_node = head_node.next
        self.head.next = next_node
        if next_node is not None:
            next_node.prev = self.head
        self._size -= 1
        self.dequeue_status = self.DEQUEUE_OK 
        return head_node.value

    def clear(self) -> None:
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    ## Команды
    def size(self) -> int:
        return self._size
    
    def get_head(self) -> object:
        if self.head.next is not None:
            return self.head.next.value
    
    def get_tail(self) -> object:
        if self.tail.prev is not None:
            return self.tail.prev.value

    ## Дополнительные запросы
    def get_queue(self):
        return self.queue

    ## Запросы статусов
    def get_dequeue_status(self):
        return self.dequeue_status


