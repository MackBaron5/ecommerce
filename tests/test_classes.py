import pytest
from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture(autouse=True)
def reset_counters():
    """Фикстура для сброса счетчиков класса Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов."""
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)
    p2 = Product("Iphone 15 Pro", "128GB, Blue", 210000.0, 3)
    return [p1, p2]


def test_product_initialization():
    """Тест корректности инициализации объекта Product."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Gray"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter(capsys):
    """Тест работы сеттера цены, включая проверку некорректных значений."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)

    # Проверка корректной смены цены
    product.price = 150000.0
    assert product.price == 150000.0

    # Проверка отрицательной цены
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 150000.0  # Цена не изменилась


def test_product_new_product():
    """Тест создания продукта через класс-метод из словаря."""
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }
    product = Product.new_product(product_data)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_category_initialization(sample_products):
    """Тест корректности инициализации объекта Category и вывода геттера продуктов."""
    category = Category("Смартфоны", "Мобильные телефоны и аксессуары", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны и аксессуары"

    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15 Pro, 210000.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output


def test_category_and_product_count(sample_products):
    """Тест подсчета количества категорий и продуктов."""
    assert Category.category_count == 0
    assert Category.product_count == 0

    Category("Смартфоны", "Мобильные телефоны", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("Lenovo Legion 5", "Игровой ноутбук", 150000.0, 2)
    Category("Ноутбуки", "Игровые ноутбуки", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_product_str():
    """Тест строкового представления продукта."""
    p = Product("Test Phone", "Description", 50000.0, 10)
    assert str(p) == "Test Phone, 50000.0 руб. Остаток: 10 шт."


def test_category_str(sample_products):
    """Тест строкового представления категории (сумма всех штук на складе)."""
    category = Category("Смартфоны", "Описание", sample_products)
    assert str(category) == "Смартфоны, количество продуктов: 8 шт."


def test_product_add():
    """Тест сложения двух продуктов (стоимость всех товаров на складе)."""
    p1 = Product("Samsung S23", "Specs", 100000.0, 5)  # 100000 * 5 = 500000
    p2 = Product("Xiaomi 13", "Specs", 50000.0, 10)  # 50000 * 10 = 500000
    assert p1 + p2 == 1000000.0


def test_products_getter_with_str(sample_products):
    """Тест, что оптимизированный геттер возвращает корректную строку через __str__."""
    category = Category("Смартфоны", "Описание", sample_products)
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15 Pro, 210000.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output


def test_smartphone_initialization():
    """Тест создания объекта Smartphone и его уникальных свойств."""
    smart = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert smart.name == "Iphone 15"
    assert smart.efficiency == 98.2
    assert smart.model == "15"
    assert smart.memory == 512
    assert smart.color == "Gray space"


def test_lawngrass_initialization():
    """Тест создания объекта LawnGrass и его уникальных свойств."""
    grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_products_addition_different_classes_error():
    """Тест Задания 2: Нельзя складывать объекты разных классов."""
    smart = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        _ = smart + grass


def test_add_invalid_product_to_category_error():
    """Тест Задания 3: Нельзя добавлять в категорию сторонние объекты."""
    category = Category("Смартфоны", "Тест")

    with pytest.raises(TypeError):
        category.add_product("Не объект продукта, а обычная строка")


def test_base_product_abstract():
    """Тест Задания 1 (16.2): Проверяет абстрактность BaseProduct."""
    from src.classes import BaseProduct
    with pytest.raises(TypeError):
        _ = BaseProduct("Тест", "Описание", 100.0, 1)


def test_log_mixin_output(capsys):
    """Тест Задания 2 (16.2): Проверяет логирование через миксин."""
    _ = Product("Тест Лога", "Проверка миксина", 1000.0, 10)
    captured = capsys.readouterr()
    assert "Product" in captured.out
    assert "Тест Лога" in captured.out
