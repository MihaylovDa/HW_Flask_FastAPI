from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool

# —оздание пустого списка задач
tasks = []

# GET /tasks Ч возвращает список всех задач
@app.get('/tasks', response_model=List[Task])
async def get_tasks():
    return tasks

# GET /tasks/{id} Ч возвращает задачу с указанным идентификатором
@app.get('/tasks/{id}', response_model=Task)
async def get_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    return {'error': 'Task not found'}

# POST /tasks Ч добавл€ет новую задачу
@app.post('/tasks', response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

# PUT /tasks/{id} Ч обновл€ет задачу с указанным идентификатором
@app.put('/tasks/{id}', response_model=Task)
async def update_task(id: int, task: Task):
    for i, t in enumerate(tasks):
        if t.id == id:
            tasks[i] = task
            return task
    return {'error': 'Task not found'}

# DELETE /tasks/{id} Ч удал€ет задачу с указанным идентификатором
@app.delete('/tasks/{id}')
async def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task.id == id:
            del tasks[i]
            return {'message': 'Task deleted'}
    return {'error': 'Task not found'}