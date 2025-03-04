class BloomFilter:
    # Конструктор:
    # Постусловие: создан пустой фильтр 
    def __init__(self, filter_size: int):
        self.filter_size = filter_size
        self.bit_array = bytearray(self.filter_size // 8)

    def _set_bit(self, i: int) -> None:
        byte_index = i // 8
        bit_index = i % 8
        self.bit_array[byte_index] |= (1 << bit_index)

    def _get_bit(self, i: int) -> int:
        byte_index = i // 8
        bit_index = i % 8
        return (self.bit_array[byte_index] >> bit_index) & 1
            
    def _hash_17(self, string: str) -> int:
        i = 0
        for c in string:
            i = ord(c) + i * 17
        i = i % self.filter_size
        return i

    def _hash_223(self, string: str) -> int:
        i = 0
        for c in string:
            i = ord(c) + i * 223
        i = i % self.filter_size
        return i

    ## Команды:
    # Постусловие: в фильтр добавлен новый элемент
    def add(self, string: str) -> None:
        i1 = self._hash_17(string)
        i2 = self._hash_223(string)
        if self._get_bit(i1) == 0:
            self._set_bit(i1)
        if self._get_bit(i2) == 0:
            self._set_bit(i2)

    ## Запросы:
    def is_value(self, string: str) -> bool:
        i1 = self._hash_17(string)
        i2 = self._hash_223(string)
        if (self._get_bit(i1) == 1) and (self._get_bit(i2) == 1):
            return True
        return False 
    

    