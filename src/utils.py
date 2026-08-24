import json
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/app.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json_file(file_path):
    logger.info(f"Чтение файла: {file_path}")
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"Успешно прочитано {len(data)} записей")
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception) as e:
        logger.error(f"Ошибка чтения файла {file_path}: {e}")
        return []

# if __name__ == "__main__":
#     from src.utils import read_json_file
#     transactions = read_json_file("data/operations.json")
#     print(len(transactions))

if __name__ == "__main__":
    from src.utils import read_json_file

    data = read_json_file("../data/operations.json")
    print(f"Загружено {len(data)} записей")

    data = read_json_file("../data/not_found.json")
    print(f"Результат: {data}")
