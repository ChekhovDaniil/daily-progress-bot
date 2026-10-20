# Априорные данные для работы с задачами 
from utils.models import Task
class TaskStorage:
    def __init__(self):
        self._tasks: dict[str, list[Task]] = {} # Основной словарь хранения данных

    # Добавление задачи на определённую дату
    def add(self, date: str, task: Task) -> None:
        self._tasks.setdefault(date, []).append(task)

    # Получение задачи по дате и индексу
    def get_by_date(self, date: str) -> list[Task]:
        return self._tasks.get(date, [])

    # Удаление задачи по дате и индексу
    def delete(self, date: str, index: int) -> None:
        del self._tasks[date][index]
        if not self._tasks[date]:
            del self._tasks[date]

    # Получение всех задач по дате
    def all(self) -> dict[str, list[Task]]:
        return self._tasks
    

    