from domain.repositories.task_repository import TaskRepository
from domain.entities.task import Task


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks: list[Task] = []

    def save(self, task):
        self.tasks.append(task)

    def list(self):
        return self.tasks
