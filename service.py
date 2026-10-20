# Функционал сервиса для работы с задачами
from telebot import logger
from utils.models import Task
from storage import TaskStorage
import dateparser

class TaskService:
    def __init__(self, storage: TaskStorage):
        self.storage = storage

    @staticmethod
    def parse_human_date(value: str) -> str:
        dt = dateparser.parse(
        value,
        languages=["ru", "en"],
        settings={"PREFER_DATES_FROM": "future"}
    )
        if dt is None:
            raise ValueError("Не удалось распознать дату")
        return dt.date().isoformat()  # 'YYYY-MM-DD

    # Добавляет задачу если дата валидна 
    def add_task(self, date: str, text: str) -> None:
        date = self.parse_human_date(date)
        self.storage.add(date, Task(text=text))

    # Возвращает список задач на указанную дату
    def list_tasks(self, date: str) -> list[Task]:
        return "\n".join(f"{i}. {task.text}"
        for i, task in enumerate(self.storage.get_by_date(date)))
        # return self.storage.get_tasks(date)
        # return enumerate(self.storage.get_by_date(date))


    # Возвращает задачу по индексу на указанную дату
    def find_task(self, date: str, index: int) -> Task:
        date = self.parse_human_date(date)
        tasks = self.storage.get_by_date(date)
        if index < 0 or index >= len(tasks):
            logger.warning(
                "Invalid task index",
                extra={"index": index, "tasks_count": len(tasks)}
            )
            raise IndexError("Нет задачи с таким номером")
        return tasks[index]

    # Редактирует текст задачи по индексу на указанную дату и новому тексту
    def edit_task(self, date: str, index: int, new_text: str) -> None:
        task = self.find_task(date, index)
        task.text = new_text

    # Удаляет задачу по индексу на указанную дату
    def remove_task(self, date: str, index: int) -> None:
        self.find_task(date, index)  # проверка
        self.storage.delete(date, index)


task_service = TaskService(TaskStorage())
logger.debug("Listing tasks", extra={"date": task_service.parse_human_date})
