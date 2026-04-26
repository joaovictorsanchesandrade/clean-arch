from domain.entities.task import Task
from domain.repositories.task_repository import TaskRepository


class CreateTask:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, title: str):
        task = Task(title=title)
        self.repository.save(task)
        return task
