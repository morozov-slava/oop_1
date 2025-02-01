class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class ParentList:
    # Конструктор
    # постусловие: создан новый пустой связный список
    def __init__(self):
        # constants
        self.HEAD_OK = 1             # последний вызов метода head() отработал нормально
        self.HEAD_ERR = 2            # связный список пуст
        self.TAIL_OK = 1             # последний вызов метода tail() отработал нормально
        self.TAIL_ERR = 2            # связный список пуст
        self.RIGHT_OK = 1            # последний вызов метода right() отработал нормально
        self.RIGHT_ERR = 2           # правее курсора нет элемента
        self.ADD_TO_EMPTY_OK = 1     # последний вызов метода add_to_empty() отработал нормально
        self.ADD_TO_EMPTY_ERR = 2    # связный список не был пустым
        self.REPLACE_OK = 1          # последний вызов метода replace() отработал нормально
        self.REPLACE_ERR = 2         # связный список пуст
        self.FIND_OK = 1             # последний вызов метода find() отработал нормально
        self.FIND_ERR = 2            # искомое значение отсутствует в связном списке
        self.GET_OK = 1              # последний вызов метода get() отработал нормально
        self.GET_ERR = 2             # связный список пустой
        self.IS_HEAD_OK = 1          # последний вызов метода is_head() отработал нормально
        self.IS_HEAD_ERR = 2         # связный список пустой
        self.IS_TAIL_OK = 1          # последний вызов метода is_tail() отработал нормально
        self.IS_TAIL_ERR = 2         # связный список пустой
        self.PUT_RIGHT_OK = 1        # последний вызов метода put_right() отработал нормально
        self.PUT_RIGHT_ERR = 2       # связный список пуст
        self.PUT_LEFT_OK = 1         # последний вызов метода put_left() отработал нормально
        self.PUT_LEFT_ERR = 2        # связный список пуст  
        self.REMOVE_OK = 1           # последний вызов метода remove() отработал нормально
        self.REMOVE_ERR = 2          # связный список пустой
        # statuses
        self.head_status = None
        self.tail_status = None
        self.right_status = None
        self.add_to_empty_status = None
        self.replace_status = None
        self.find_status = None
        self.get_status = None
        self.is_head_status = None
        self.is_tail_status = None
        self.put_right_status = None
        self.put_left_status = None
        self.remove_status = None
        # arguments
        self.head_node = None
        self.tail_node = None
        self.cursor = None
        self.list_size = 0
    
    ## Команды:
    def head(self) -> None:
        # предусловие: связный список не должен быть пустым
        # постусловие: курсор установлен на первый узел в списке
        if self.size() == 0:
            self.head_status = self.HEAD_ERR
            return None
        self.cursor = self.head_node
        self.head_status = self.HEAD_OK

    def tail(self) -> None:
        # предусловие: связный список не должен быть пустым
        # постусловие: курсор установлен на последний узел в списке
        if self.size() == 0:
            self.tail_status = self.TAIL_ERR
            return None
        self.cursor = self.tail_node
        self.tail_status = self.TAIL_OK

    def right(self) -> None:
        # предусловие: правее курсора есть элемент; 
        # постусловие: курсор сдвинут на один узел вправо
        if (self.cursor is None) or (self.cursor.next is None):
            self.right_status = self.RIGHT_ERR
            return None
        self.cursor = self.cursor.next
        self.right_status = self.RIGHT_OK

    def put_right(self, value) -> None:
        # предусловие: связный список не пуст 
        # постусловие: следом за текущим узлом добавлен новый узел с заданным значением
        if self.size() == 0:
            self.put_right_status = self.PUT_RIGHT_ERR
            return None
        new_node = Node(value)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next
        if self.cursor.next:
            self.cursor.next.prev = new_node
        self.cursor.next = new_node
        if self.cursor == self.tail_node:
            self.tail_node = new_node
        self.list_size += 1
        self.put_right_status = self.PUT_RIGHT_OK

    def put_left(self, value) -> None:
        # предусловие: связный список не пуст; 
        # постусловие: перед текущим узлом добавлен новый узел с заданным значением
        if self.size() == 0:
            self.put_left_status = self.PUT_LEFT_ERR
            return None
        new_node = Node(value)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev
        if self.cursor.prev:
            self.cursor.prev.next = new_node
        self.cursor.prev = new_node
        if self.cursor == self.head_node:
            self.head_node = new_node
        self.list_size += 1
        self.put_left_status = self.PUT_LEFT_OK

    def remove(self) -> None:
        # предусловие: список не пуст; 
        # постусловие: текущий узел удалён, курсор смещён к правому соседу, если он есть, в противном случае курсор смещён к левому соседу, если он есть
        if self.size() == 0:
            self.remove_status = self.REMOVE_ERR
            return None
        if (self.cursor == self.head_node == self.tail_node):
            self.head_node = None
            self.tail_node = None
            self.cursor = None
        elif (self.cursor == self.head_node):
            next_node = self.cursor.next
            next_node.prev = None
            self.head_node = next_node
            self.cursor = next_node
        elif (self.cursor == self.tail_node):
            prev_node = self.cursor.prev
            prev_node.next = None
            self.tail_node = prev_node
            self.cursor = prev_node
        else:
            next_node = self.cursor.next
            prev_node = self.cursor.prev
            prev_node.next = next_node
            next_node.prev = prev_node
        self.list_size -= 1
        self.remove_status = self.REMOVE_OK
        
    def clear(self) -> None:
        # Постусловие: из списка удаляются все значения
        self.head_node = None
        self.tail_node = None
        self.cursor = None
        self.list_size = 0

    def add_to_empty(self, value) -> None:
        # Предусловие: список должен быть пустым
        # Постусловие: добавлен узел с заданным значением в список
        if self.size() != 0:
            self.add_to_empty_status = self.ADD_TO_EMPTY_ERR
            return None
        new_node = Node(value)
        self.head_node = self.tail_node = self.cursor = new_node
        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node
        self.list_size += 1
        self.add_to_empty_status = self.ADD_TO_EMPTY_OK
        
    def add_tail(self, value) -> None:
        # Постусловие: добавлен узел с заданным значением в список
        new_node = Node(value)
        if self.size() == 0:
            self.head_node = self.tail_node = self.cursor = new_node
        else:
            new_node.prev = self.tail_node
            self.tail_node.next = new_node
            self.tail_node = new_node
        self.list_size += 1
    
    def replace(self, value) -> None:
        # Предусловие: список не должен быть пустым
        # Постусловие: значение текущего узла заменено на заданное
        if self.size() == 0:
            self.replace_status = self.REPLACE_ERR
            return None
        new_node = Node(value)
        new_node.next = self.cursor.next
        new_node.prev = self.cursor.prev
        if new_node.prev is not None:
            new_node.prev.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
            
        if (self.get() == self.head_node):
            self.head_node = new_node
        if (self.get() == self.tail_node):
            self.tail_node = new_node
        self.cursor = new_node
        self.replace_status = self.REPLACE_OK
        
    def find(self, value) -> None:
        # постусловие: курсор установлен на следующий узел c искомым значением, если такой узел найден
        current_node = self.cursor.next
        while current_node is not None:
            if current_node.value == value:
                self.cursor = current_node
                break
            current_node = current_node.next

    def remove_all(self, value) -> None:
        # Постусловие: из списка удалены все узлы с заданным значением
        current_node = self.head_node
        while current_node is not None:
            if (current_node.value == value) and (current_node == self.get()):
                self.remove()
            elif (current_node.value == value) and (current_node == self.head_node) and (current_node == self.tail_node):
                self.clear()
            elif (current_node.value == value) and (current_node == self.head_node):
                self.head_node = current_node.next
                self.head_node.prev = None
                self.list_size -= 1
            elif (current_node.value == value) and (current_node == self.tail_node):
                self.tail_node = current_node.prev
                self.tail_node.next = None
                self.list_size -= 1
            current_node = current_node.next

    def get_all_node_values(self) -> list:
        all_nodes = []
        current_node = self.head_node
        while current_node is not None:
            all_nodes.append(current_node.value)
            current_node = current_node.next
        return all_nodes

    ## Запросы
    def get(self):
        # Предусловие: связный список не должен быть пустым
        if self.size() == 0:
            self.get_status = self.GET_ERR
            return None
        return self.cursor

    def size(self) -> int:
        return self.list_size

    def is_head(self) -> bool:
        return self.head_node == self.cursor

    def is_tail(self) -> bool:
        return self.tail_node == self.cursor

    def is_value(self) -> bool:
        return self.cursor is not None

    ## Дополнительные запросы
    def get_head_status(self):
        # возвращает значение HEAD_*
        return self.head_status

    def get_tail_status(self):
        # возвращает значение TAIL_*
        return self.tail_status

    def get_right_status(self):
        # возвращает значение RIGHT_*
        return self.right_status

    def get_add_to_empty_status(self):
        # возвращает значение ADD_TO_EMPTY_*
        return self.add_to_empty_status

    def get_replace_status(self):
        # возвращает значение REPLACE_*
        return self.replace_status

    def get_find_status(self):
        # возвращает значение FIND_*
        return self.find_status

    def get_get_status(self):
        # возвращает значение GET_*
        return self.get_status

    def get_is_head_status(self):
        # возвращает значение IS_HEAD_*
        return self.is_head_status

    def get_is_tail_status(self):
        # возвращает значение IS_TAIL_*
        return self.is_tail_status

    def get_put_right_status(self):
        # возвращает значение PUT_RIGHT_*
        return self.put_right_status

    def get_put_left_status(self):
        # возвращает значение PUT_LEFT_*
        return self.put_left_status

    def get_remove_status(self):
        # возвращает значение REMOVE_*
        return self.remove_status


class LinkedList(ParentList):
    def __init__(self):
        super().__init__()


class TwoWayList(ParentList):
    def __init__(self):
        super().__init__()
    
        self.LEFT_OK = 1            # последний вызов метода left() отработал нормально
        self.LEFT_ERR = 2           # левее курсора нет элемента
        # statuses
        self.left_status = None

    def left(self) -> None:
        # Сдвигаем курсор на один узел влево
        # предусловие: левее курсора есть элемент; 
        # постусловие: курсор сдвинут на один узел влево
        if (self.cursor is None) or (self.cursor.prev is None):
            self.left_status = self.LEFT_ERR
            return None
        self.cursor = self.cursor.prev
        self.left_status = self.LEFT_OK

    def get_left_status(self) -> None:
        # возвращает значение LEFT_*
        return self.left_status


