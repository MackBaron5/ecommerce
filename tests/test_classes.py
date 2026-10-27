import pytest
from src.classes import Category, Product


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

    # Проверяем, что геттер возвращает правильный шаблон строки
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n"
        "Iphone 15 Pro, 210000 руб. Остаток: 3 шт.\n"
    )
    assert category.products == expected_output


def test_category_and_product_count(sample_products):
    """Тест подсчета количества категорий и продуктов."""
    assert Category.category_count == 0
    assert Category.product_count == 0

    cat1 = Category("Смартфоны", "Мобильные телефоны", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("Lenovo Legion 5", "Игровой ноутбук", 150000.0, 2)
    cat2 = Category("Ноутбуки", "Игровые ноутбуки", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3
