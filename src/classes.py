class Product:
    """Класс для представления товара."""

    def __init__(
            self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
            self, name: str, description: str, products: list | None = None
    ) -> None:
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)
