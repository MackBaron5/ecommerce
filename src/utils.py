import json
from src.classes import Category, Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Читает данные из JSON-файла и возвращает список объектов Category."""
    categories_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for category_data in data:
            products_in_category = []

            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
                products_in_category.append(product)

            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products_in_category,
            )
            categories_list.append(category)

    except FileNotFoundError:
        print(f"Ошибка: Файл по пути {file_path} не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Не удалось десериализовать JSON."
              "Проверьте синтаксис файла.")

    return categories_list
