# Интерфейс обработки команд бота
from service import TaskService
from bots_netology.main import logger

# Добавление задачи на определённую дату (вывод)
def handle_add(service: TaskService, date: str, text: str):
    service.add_task(date, text)
    return f"Задача {text} на дату {date} добавлена"

# Получение списка задач на определённую дату (вывод)
def handle_list(service: TaskService, date_str: str):
    result = service.list_tasks(date_str)
    return result if result else "Задач нет" 

# Редактирование задачи по индексу на определённую дату (вывод)
def handle_edit(service: TaskService, date_str: str, index: int, new_text: str) -> str:
    service.edit_task(date_str, index, new_text)
    return f"Задача под номером {index} отредактирована на: {new_text}"

# Удаление задачи по индексу на определённую дату (вывод)
def handle_remove(service: TaskService, date_str: str, index: int) -> str:
    logger.info("Remove command received", extra={"index": index})
    # service.remove_task(date_str, index)
    try:
        return service.remove_task(date_str, index)
        # return f"Задача под номером {index} на дату {date_str} была удалена"
    except ValueError as e:
        logger.error("Remove failed", exc_info=True)
        return str(e)

handlers = {
    "add": handle_add,
    "list": handle_list,
    "edit": handle_edit,
    "remove": handle_remove, 
}

# Получение обработчика по команде через словарь
def get_handler(command: str) -> callable:
    handler = handlers.get(command)
    if handler is None:
        raise ValueError(f"Unknown command: {command}")
    return handler
    