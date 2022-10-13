from abc import ABC


class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, name, value) -> None:
        """увеличивает запас items"""
        pass

    def remove(self, name, value) -> None:
        """ уменьшает запас items"""
        pass

    def get_free_space(self) -> int:
        """Вернуть количество свободных мест"""
        pass

    def get_items(self) -> dict:
        """Возвращает сожержание склада в словаре {товар: количество}"""
        pass

    def get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров."""
        pass
