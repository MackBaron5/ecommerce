import pytest
from src.utils import load_data_from_json


def test_load_data_from_json_success():
    """Тест успешной загрузки данных из корректного JSON-файла."""
    categories = load_data_from_json("data/products.json")
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"
    assert len(categories[0].products.strip().split('\n')) == 3


def test_load_data_from_json_file_not_found():
    """Тест возврата пустого списка, если файл не найден."""
    categories = load_data_from_json("data/invalid_path.json")
    assert categories == []
