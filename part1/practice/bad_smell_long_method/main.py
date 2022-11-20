# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


from typing import List

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_users_list(users: str) -> List[dict]:
    """Читать пользователей из файла и создавать словарь"""
    users_list = []
    for line in users.split('\n'):
        name, age = line.split(';')
        users_list.append({'name': name, 'age': int(age)})
    return users_list


def sort_users_by_age(users: List[dict]) -> List[dict]:
    """Сортировать пользователей по возрасту в порядке возрастания с помощью пузырьковой сортировки."""

    for i in range(len(users) - 1):
        for j in range(len(users) - i - 1):
            if users[j]['age'] > users[j+1]['age']:
                users[j], users[j+1] = users[j+1], users[j]
    return users


def get_users(users: str, age_threshold: int = 10) -> List[dict]:
    """Получить пользователей из файла с возрастом ниже порогового значения"""
    users_list = sort_users_by_age(read_users_list(users))
    return [user for user in users_list if user['age'] < age_threshold]


if __name__ == '__main__':
    print(get_users(csv, 50))
