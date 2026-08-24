from src.file_reader import pandas_read_csv, pandas_read_excel, pandas_read_json

def main():
    print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

    transactions = None

    while True:
        try:
            menu_choice_input = int(input())
        except Exception as e:
            print('Ошибка. Введите номер пункта корректно')
            continue

        if menu_choice_input == 1:
            print('Для обработки выбран JSON-файл.')
            transactions = pandas_read_json('data/operations.json')
            break
        elif menu_choice_input == 2:
            print('Для обработки выбран CSV-файл.')
            transactions = pandas_read_csv('data/transactions.csv')
            break
        elif menu_choice_input == 3:
            print('Для обработки выбран XLSX-файл.')
            transactions = pandas_read_excel('data/transactions_excel.xlsx')
            break
        else:
            print('Пожалуйста, введите номер пункта корректно.')
            continue

    print('Укажите статус операции.')
    user_input_status = input()
    status = user_input_status.upper()
    allowed_statuses = ['EXECUTED', 'CANCELED', 'PENDING']

    if status not in allowed_statuses:
        print(f'Статус операции "{user_input_status}" недоступен.')
        print('Доступные статусы: EXECUTED, CANCELED, PENDING')
    else:
        filtered_transactions = []
        for transaction in transactions:
            if transaction.get('state') == status:
                filtered_transactions.append(transaction)

        if filtered_transactions:
            print(f'Найдено {len(filtered_transactions)} транзакций со статусом "{status}"')
        else:
            print(f'Не найдено ни одной транзакции со статусом "{status}"')

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice in ['да', 'yes', 'д', 'y']:
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        # Сортируем по полю 'date'
        # Если дата в формате 'ДД.ММ.ГГГГ', сортировка будет работать как строковая
        if order in ['по возрастанию', 'возрастанию', 'asc']:
            filtered_transactions.sort(key=lambda x: x.get('date', ''))
        elif order in ['по убыванию', 'убыванию', 'desc']:
            filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=True)

    rub_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_choice in ['да', 'yes', 'д', 'y']:
        filtered_transactions = [
            t for t in filtered_transactions
            if t.get('currency', {}).get('code') == 'RUB'
               or t.get('currency_code') == 'RUB'
               or 'руб' in t.get('description', '').lower()
        ]

    word_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if word_choice in ['да', 'yes', 'д', 'y']:
        search_word = input("Введите слово для поиска: ").strip()
        filtered_transactions = [
            t for t in filtered_transactions
            if search_word.lower() in t.get('description', '').lower()
        ]

    print("\nРаспечатываю итоговый список транзакций...")
    print("=" * 50)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

        for idx, t in enumerate(filtered_transactions, 1):
            date = t.get('date', 'Дата не указана')
            description = t.get('description', 'Описание отсутствует')
            amount = t.get('amount', 0)
            currency = t.get('currency', {}).get('code', '')
            if not currency:
                currency = t.get('currency_code', '')

            from_account = t.get('from', '')
            to_account = t.get('to', '')

            if from_account:
                from_account = f"{from_account[:4]} {from_account[4:6]}** **** {from_account[-4:]}"
            if to_account:
                to_account = f"{to_account[:4]} {to_account[4:6]}** **** {to_account[-4:]}"

            print(f"{idx}. {date} {description}")
            if from_account and to_account:
                print(f"{from_account} -> {to_account}")
            elif from_account:
                print(f"Счет {from_account}")
            elif to_account:
                print(f"Счет {to_account}")

            print(f"Сумма: {amount} {currency if currency else ''}\n")


if __name__ == "__main__":
    main()
