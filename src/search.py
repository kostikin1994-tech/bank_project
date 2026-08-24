import re

def process_bank_search(data:list[dict], search:str) -> list[dict]:
    '''Функция принимает список словарей и строку для поиска, возвращает словари, которые подходят под условие'''

    if isinstance(data, list) and all(isinstance(item, dict) for item in data) and isinstance(search, str):
        try:
            pattern = re.compile(search, re.IGNORECASE)
            result = [item for item in data if any(re.search(pattern, str(val)) for val in item.values())]
            return result
        except Exception as e:
            print(f'Ошибка: {e}')
    else:
        print('Введенные данные не соответствуют параметрам')
        return None

def process_bank_operations(data:list[dict], categories:list) -> dict:
    '''Функция принимает список словарей и список названий категорий транзакций, возвращает словарь, где ключ - название транзакции, значение - количество '''
    result = {cat: 0 for cat in categories}
    if not (isinstance(data, list) and isinstance(categories, list)):
        return {}
    else:
        for transaction in data:
            for category in categories:
                data_description = transaction['description']
                if category.lower() in data_description.lower():
                    result[category] += 1
    return result




