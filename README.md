
API available at `http://localhost:5000`.

---

### Option B — Python / FastAPI

```bash
cd python-api
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install fastapi uvicorn pymongo python-dotenv
cp .env.example .env
```

Edit `.env`:
```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority
DB_NAME=todo-list-api
```

Run it:
```bash
uvicorn main:app --reload
```

API available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

---

## 📡 API Endpoints

Identical contract on both implementations (base URL differs — `:5000` for Node, `:8000` for FastAPI):

| Method | Endpoint       | Description              | Success Status |
|--------|----------------|---------------------------|-----------------|
| GET    | `/todos`       | Get all todos             | 200             |
| GET    | `/todos/{id}`  | Get a single todo by ID   | 200             |
| POST   | `/todos`       | Create a new todo         | 201             |
| PUT    | `/todos/{id}`  | Update an existing todo   | 200             |
| DELETE | `/todos/{id}`  | Delete a todo             | 200             |

### Todo object shape
```json
{
  "_id": "64f1c2e5a1b2c3d4e5f6a7b8",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "createdAt": "2026-08-02T10:15:30.000Z"
}
```

### Validation rules
- `title`: string, 2–100 characters, required
- `description`: string, 3–500 characters, required
- `completed`: boolean, defaults to `false`
- `id`: must be a valid MongoDB ObjectId, or the API returns `400` before touching the database

### Status codes used
| Code | Meaning                                                        |
|------|-----------------------------------------------------------------|
| 200  | Successful GET / PUT / DELETE                                  |
| 201  | Successful POST (resource created)                              |
| 400  | Validation error, malformed request body, or invalid ID format  |
| 404  | Todo not found / unmatched route                                 |
| 500  | Unexpected server error                                          |

---

## 🔍 Example Requests (Node.js — port 5000)

### Create a todo
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false
  }'
```

### Get all todos
```bash
curl http://localhost:5000/todos
```

### Update a todo
```bash
curl -X PUT http://localhost:5000/todos/64f1c2e5a1b2c3d4e5f6a7b8 \
  -H "Content-Type: application/json" \
  -d '{ "completed": true }'
```

### Delete a todo
```bash
curl -X DELETE http://localhost:5000/todos/64f1c2e5a1b2c3d4e5f6a7b8
```

> The FastAPI implementation accepts the same requests on port `8000` — or skip curl entirely and use the interactive `/docs` page to try each endpoint.

---

## 🧪 Testing

**Node.js:** Import `node-api/postman/Todo-List-API.postman_collection.json` into Postman. Run requests top to bottom: Create → Get All → Get By ID → Update → Delete, plus the included error-case requests (missing title, invalid ID, not-found ID).

**Python/FastAPI:** Open `http://localhost:8000/docs` and exercise each endpoint directly from the auto-generated Swagger UI — no separate collection needed.

---

## ✅ Requirements Checklist

- [x] `GET /todos`, `GET /todos/:id`, `POST /todos`, `PUT /todos/:id`, `DELETE /todos/:id`
- [x] Todo includes `title`, `description`, `completed`, `createdAt`
- [x] Input validation with proper status codes (200, 201, 400, 404)
- [x] Real database (MongoDB) — no in-memory storage
- [x] Same contract implemented in two languages/frameworks
- [x] Centralized error handling
- [x] README with setup instructions and example requests

---

## 📬 Author

**Saad Abdullah** — Embedded Systems & IoT Engineer
📧 saadiabdullah133@gmail.com · 🔗 [linkedin.com/in/saad-abdullah-iot](https://linkedin.com/in/saad-abdullah-iot)
