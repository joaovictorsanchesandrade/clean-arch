from domain.entities.task import Task
from application.use_cases.create_task import CreateTask
from infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository


def test_create_task():
    """Test if the use case for creating a task"""
    repository = InMemoryTaskRepository()
    create_task = CreateTask(repository)
    create_task.execute("Testando o meu caso de uso")
    assert len(repository.list()) > 0
