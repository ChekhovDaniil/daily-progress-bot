from utils.logging import setup_logging

setup_logging()

# from storage import TaskStorage
# from service import TaskService
# from handlers import handle_add, handle_list

# storage = TaskStorage()
# service = TaskService(storage)

# print(handle_add(service, "Купить хлеб", "2026-01-15"))
# print(handle_add(service, "Сделать бота", "2026-01-15"))

# print(handle_list(service, "2026-01-15"))

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя, пример ввода: /add 31/12 прогулка).
# show - напечатать все добавленные задачи/задачу на определённую дату (/show 31/12).
# random - добавить случайную задачу из списка.
# exit - выйти из программы.
# all - выводит все задачи, сгруппированные по датам и пронумированные.
# print - принимает несколько дат: /print 01/04 02/04 03/04 — выводит задачи на каждую из дат, сортирует по альфавиту.
# edit - /edit номер_задачи новое_описание — изменение текста задачи.   
# delete - /delete номер_задачи — удаление задачи по порядковому номеру
# """

# # Список поддерживаемых команд (используется в функции errors)
# commands = ['/help', '/add', '/show', '/random', '/exit', '/all', '/print', '/edit', '/delete', '/list']

# random_tasks = [
#     "Сделать домашнее задание",
#     "Прочитать книгу",
#     "Пойти на прогулку",
#     "Позвонить другу",
#     "Приготовить ужин"
#  ]
# name = 'Daniil'

# print(f"Ты приедешь со скоростью {int(speed)} км/ч, в {distance} км, это займет {distance/speed}")