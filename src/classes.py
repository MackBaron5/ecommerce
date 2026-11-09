class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового объекта Product из словаря."""
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity")
        )

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой на корректность значения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Задание 2: Сложение общей стоимости товаров ТОЛЬКО одинаковых классов продуктов."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного и того же класса.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = []  # Приватный список товаров
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product) -> None:
        """Задание 3: Добавляет продукт в приватный список с проверкой типа.
        Разрешены только объекты класса Product и его наследников.
        """
        if not isinstance(product, Product):
            raise TypeError("Добавляемый объект должен быть продуктом (класса Product или его наследником).")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращающий отформатированное строковое представление всех продуктов."""
        return "".join([f"{str(product)}\n" for product in self.__products])

    def __str__(self) -> str:
        """Строковое отображение категории со всеми единицами товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    """Класс для представления смартфона, наследник класса Product."""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы, наследник класса Product."""
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
