import pytest
from service import TaskService
from storage import TaskStorage

def test_add_task_valid_date():
    """Тестирование добавления задачи с валидной датой"""
    storage = TaskStorage() # Создаем экземпляр хранилища
    service = TaskService(storage) # Создаем экземпляр сервиса с хранилищем
    service.add_task("2024-12-31", "New Year's Eve task") # Добавляем задачу с валидной датой
    tasks = storage.get_by_date("2024-12-31") # Получаем задачи на эту дату
    assert len(tasks) == 1 # Проверяем, что задача добавлена
    assert tasks[0].text == "New Year's Eve task" # Проверяем текст задачи

def test_add_task_invalid_date():
    service = TaskService(TaskStorage())

    with pytest.raises(ValueError):
        service.add_task("14-01-2026", "Ошибка")


def test_find_task_success():
    storage = TaskStorage()
    service = TaskService(storage)

    service.add_task("2026-01-14", "Задача 1")

    task = service.find_task("2026-01-14", 0)
    assert task.text == "Задача 1"

def test_find_task_invalid_index():
    service = TaskService(TaskStorage())
    service.add_task("2026-01-14", "Задача")

    with pytest.raises(IndexError):
        service.find_task("2026-01-14", 2)

def test_find_task_invalid_date():
    service = TaskService(TaskStorage())

    with pytest.raises(ValueError):
        service.find_task("14-01-2026", "Ошибка")

def test_add_task_human_date():
    service = TaskService(TaskStorage())
    service.add_task("завтра", "Сделать дело")

    tasks = service.list_tasks("tomorrow")
    assert len(tasks) == 1
    assert tasks[0].text == "Сделать дело"


def test_invalid_date():
    service = TaskService(TaskStorage())

    with pytest.raises(ValueError):
        service.add_task("каша из говна", "Ошибка")