from fastapi import FastAPI, HTTPException, status
from bson import ObjectId
from datetime import datetime
from database import todo_collection
from models import TodoCreate, TodoUpdate

app = FastAPI(title="Todo API | MongoDB CRUD")


# 1. POST /todos - Create Todo (201 Created)
@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: TodoCreate):
    todo_dict = todo_data.model_dump()
    todo_dict["createdAt"] = datetime.utcnow()
    result = todo_collection.insert_one(todo_dict)
    return {
        "_id": str(result.inserted_id),
        **todo_dict
    }


# 2. GET /todos - Get All Todos (200 OK)
@app.get("/todos", status_code=status.HTTP_200_OK)
def get_all_todos():
    todos = []
    for item in todo_collection.find():
        item["_id"] = str(item["_id"])
        todos.append(item)
    return todos


# 3. GET /todos/{todo_id} - Single Todo
@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def get_single_todo(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID format")

    todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo["_id"] = str(todo["_id"])
    return todo


# 4. PUT /todos/{todo_id} - Update Todo
@app.put("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def update_todo(todo_id: str, update_data: TodoUpdate):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID format")

    update_fields = update_data.model_dump(exclude_unset=True)
    if not update_fields:
        raise HTTPException(status_code=400, detail="No valid data provided for update")

    update_result = todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": update_fields}
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo updated successfully"}


# 5. DELETE /todos/{todo_id} - Delete Todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID format")

    delete_result = todo_collection.delete_one({"_id": ObjectId(todo_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted successfully"}