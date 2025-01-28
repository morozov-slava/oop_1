class LinkedList:
    # Конструктор
    # Постусловие: создан новый пустой связный список
    def __init__(self):
        
        self.HEAD_OK = 1             # последний вызов метода head() отработал нормально
        self.HEAD_ERR = 2            # связный список пуст
          
        self.TAIL_OK = 1             # последний вызов метода tail() отработал нормально
        self.TAIL_ERR = 2            # связный список пуст
          
        self.RIGHT_OK = 1            # последний вызов метода right() отработал нормально
        self.RIGHT_ERR = 2           # связный список пуст

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
    
        
    ## Команды:
    def head(self) -> None:
        # Предусловие: связный список не должен быть пустым
        # Постусловие: курсор установлен на первый узел в списке
        raise NotImplementedError()

    def tail(self) -> None:
        # Предусловие: связный список не должен быть пустым
        # Постусловие: курсор установлен на последний узел в списке
        raise NotImplementedError()

    def right(self) -> None:
        # Предусловие: связный список не должен быть пустым
        # Постусловие: курсор установлен на ближайшие узел справа. Если текущий курсор находился на последнем узле в списке, то
        #              курсор устанавливается на первый узел в списке
        raise NotImplementedError()

    def put_right(self, value) -> None:
        # Постусловие: добавлен узел с заданным значением в список следом за текущим узлом
        raise NotImplementedError() 

    def put_left(self, value) -> None:
        # Постусловие: добавлен узел с заданным значением в список перед текущим узлом
        raise NotImplementedError() 

    def remove(self) -> None:
        # Постусловие: удалён текущий узел (курсор смещается к правому соседу, если он есть, в противном случае курсор смещается к левому соседу, если он есть)
        raise NotImplementedError()  

    def clear(self) -> None:
        # Постусловие: из списка удаляются все значения
        raise NotImplementedError() 

    def add_to_empty(self, value) -> None:
        # Предусловие: список должен быть пустым
        # Постусловие: добавлен узел с заданным значением в список
        raise NotImplementedError() 

    def add_tail(self, value) -> None:
        # Постусловие: добавлен узел с заданным значением в список
        raise NotImplementedError()

    def replace(self, value) -> None:
        # Предусловие: список не должен быть пустым
        # Постусловие: значение текущего узла заменено на заданное
        raise NotImplementedError()

    def find(self, value) -> None:
        # Предусловие: заданное значение должно присутствовать в списке
        # Постусловие: следующий узел с заданным значение становится текущим узлом (на нём устанавливается курсор)
        raise NotImplementedError()

    def remove_all(self, value) -> None:
        # Постусловие: из списка удалены все узлы с заданным значением
        raise NotImplementedError()
        

    ## Запросы
    def get(self):
        # Предусловие: связный список не должен быть пустым
        raise NotImplementedError()

    def size(self) -> int:
        raise NotImplementedError()

    def is_head(self) -> bool:
        # Предусловие: связный список не должен быть пустым
        raise NotImplementedError()

    def is_tail(self) -> bool:
        # Предусловие: связный список не должен быть пустым
        raise NotImplementedError()

    def is_value(self) -> bool:
        raise NotImplementedError()

    ## Дополнительные запросы
    def get_head_status(self):
        # возвращает значение HEAD_*
        raise NotImplementedError()

    def get_tail_status(self):
        # возвращает значение TAIL_*
        raise NotImplementedError()

    def get_right_status(self):
        # возвращает значение RIGHT_*
        raise NotImplementedError()

    def get_add_to_empty_status(self):
        # возвращает значение ADD_TO_EMPTY_*
        raise NotImplementedError()

    def get_replace_status(self):
        # возвращает значение REPLACE_*
        raise NotImplementedError()

    def get_find_status(self):
        # возвращает значение FIND_*
        raise NotImplementedError()

    def get_get_status(self):
        # возвращает значение GET_*
        raise NotImplementedError()

    def get_is_head_status(self):
        # возвращает значение IS_HEAD_*
        raise NotImplementedError()

    def get_is_tail_status(self):
        # возвращает значение IS_TAIL_*
        raise NotImplementedError()



# 2.2. Почему операция tail не сводима к другим операциям (если исходить из эффективной реализации)?

# При эффективной реализации операция tail() не сводима к другим операциям, потому что 'хвост' связного списка 
# будет храниться как отдельный атрибут класса, к которой метод tail() будет обращаться.
# При попытке сведения к другим операциям мы будем вынуждены итерироваться по всем элементам связного списка, смещая на каждом шаге курсор пока не достигнем хвоста.


# 2.3. Операция поиска всех узлов с заданным значением, выдающая список таких узлов, уже не нужна. Почему?

# Данную операцию эффективно заменяет комбинация методов find() и right().
# Есть возможность поэтапно вызывать метод find(), находя нужный элемент с последующим сдвигом курсора с помощью метода right().




