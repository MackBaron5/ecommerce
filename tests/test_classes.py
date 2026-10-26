import pytest
from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
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


def test_category_initialization(sample_products):
    """Тест корректности инициализации объекта Category."""
    category = Category("Смартфоны", "Мобильные телефоны и аксессуары", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны и аксессуары"
    assert category.products == sample_products


def test_category_and_product_count(sample_products):
    """Тест подсчета количества категорий и уникальных продуктов."""
    assert Category.category_count == 0
    assert Category.product_count == 0

    cat1 = Category("Смартфоны", "Мобильные телефоны", sample_products)
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("Lenovo Legion 5", "Игровой ноутбук", 150000.0, 2)
    cat2 = Category("Ноутбуки", "Игровые и рабочие ноутбуки", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3
