class ProductIterator:
    """Вспомогательный класс для итерации по продуктам категории."""

    def __init__(self, category) -> None:
        self.products = category.products_list
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
