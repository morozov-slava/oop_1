class DummyNode:
    def __init__(self):
        self.prev = None
        self.next = None


class Node(DummyNode):
    def __init__(self, value):
        super().__init__()
        self.value = value


class ParentQueue:
    # Конструктор
    # Постусловие: создана новая пустая очередь 
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0
        # Constants
        self.GET_HEAD_OK = 1            # последний вызов метода get_head отработал нормально
        self.GET_HEAD_ERR = 2           # очередь пустая
        self.GET_TAIL_OK = 1            # последний вызов метода get_tail отработал нормально
        self.GET_TAIL_ERR = 2           # очередь пустая
        self.DEQUEUE_HEAD_OK = 1        # последний вызов метода dequeue_head отработал нормально
        self.DEQUEUE_HEAD_ERR = 2       # очередь пустая
        # Statuses
        self.get_head_status = None
        self.get_tail_status = None
        self.dequeue_head_status = None 

    ## Запросы
    # Постусловие: в хвост очереди добавлен новый элемент
    def enqueue_to_tail(self, value: object) -> None:
        item = Node(value)
        if self.tail.prev is None:
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

    # Предусловие: очередь не пуста.
    # Постусловие: из головы очереди удалён элемент
    def dequeue_head(self):
        if self.size() == 0:
            self.dequeue_head_status = self.DEQUEUE_HEAD_ERR
            return None     
        head_node = self.head.next 
        next_node = head_node.next
        self.head.next = next_node
        if next_node is not None:
            next_node.prev = self.head
        self._size -= 1
        self.dequeue_head_status = self.DEQUEUE_HEAD_OK 
        return head_node.value

    ## Команды
    def size(self) -> int:
        return self._size

    ## Дополнительные команды
    # Предусловие: очередь не должна быть пустой
    def get_head(self) -> object:
        if self.size() == 0:
            self.get_head_status = self.GET_HEAD_ERR
            return None
        self.get_head_status = self.GET_HEAD_OK
        return self.head.next.value

    # Предусловие: очередь не должна быть пустой
    def get_tail(self) -> object:
        if self.size() == 0:
            self.get_tail_status = self.GET_TAIL_ERR
            return None
        self.get_tail_status = self.GET_TAIL_OK
        return self.tail.prev.value

    ## Запросы статусов
    def get_head_status(self):
        return self.get_head_status
    
    def get_tail_status(self):
        return self.get_tail_status
    
    def get_dequeue_head_status(self):
        return self.dequeue_head_status


class Queue(ParentQueue):
    def __init__(self):
        super().__init__()


class Dequeue(ParentQueue):
    def __init__(self):
        super().__init__()
        # Constants
        self.DEQUEUE_TAIL_OK = 1     # последний вызов метода dequeue_tail отработал нормально
        self.DEQUEUE_TAIL_ERR = 2    # очередь пустая
        # Statuses
        self.dequeue_tail_status = None

    ## Запросы
    # Постусловие: в голову очереди добавлен новый элемент
    def enqueue_to_head(self, value: object) -> None:
        item = Node(value)
        if self.head.next is None:
            self.head.next = item
            self.tail.prev = item
            item.prev = self.head
            item.next = self.tail
        else:
            head_node = self.head.next
            item.next = head_node
            head_node.prev = item
            self.head.next = item
        self._size += 1 

    # Предусловие: очередь не пуста.
    # Постусловие: из хвоста очереди удалён элемент
    def dequeue_tail(self):
        if self.size() == 0:
            self.dequeue_tail_status = self.DEQUEUE_TAIL_ERR
            return None   
        tail_node = self.tail.prev
        prev_node = tail_node.prev
        self.tail.prev = prev_node
        if prev_node is not None:
            prev_node.next = self.tail
        self._size -= 1
        self.dequeue_tail_status = self.DEQUEUE_TAIL_OK 
        return tail_node.value

    ## Запросы статусов
    def get_dequeue_tail_status(self):
        return self.dequeue_tail_status


