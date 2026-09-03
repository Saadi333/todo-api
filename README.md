# Todo List REST API

A RESTful API supporting full CRUD (Create, Read, Update, Delete) operations for a todo list application. Built with **Node.js**, **Express**, and **MongoDB** (Mongoose).

> Live Pakistan Internship Program — Backend Web Development, Week 1 Task

---

## 📋 Objective

Provide a reliable, well-structured backend API that a front-end team can build a todo app on top of — with proper validation, HTTP status codes, and real database persistence (no in-memory storage).

---

## 🛠️ Tech Stack

- **Runtime:** Node.js
- **Framework:** Express.js
- **Database:** MongoDB (via Mongoose ODM) — works with a local MongoDB instance or MongoDB Atlas free tier
- **Environment config:** dotenv

---

## 📁 Project Structure

```
todo-api/
│
├── config/
│   └── db.js                 # MongoDB connection logic
├── controllers/
│   └── todoController.js     # CRUD business logic for todos
├── middleware/
│   └── errorHandler.js       # Centralized error handling + 404 handler
├── models/
│   └── Todo.js                # Mongoose schema/model for a Todo
├── routes/
│   └── todoRoutes.js          # /todos route definitions
├── utils/
│   └── ApiError.js            # Custom error class carrying an HTTP status code
├── postman/
│   └── Todo-List-API.postman_collection.json   # Importable Postman collection
├── .env.example                # Template for environment variables
├── .gitignore
├── package.json
├── server.js                   # App entry point
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- [Node.js](https://nodejs.org/) v18 or later
- A MongoDB database — either:
  - **Local MongoDB** installed and running (`mongod`), or
  - **MongoDB Atlas** free tier cluster (recommended): [mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)

### 2. Install dependencies
```bash
cd todo-api
npm install
```

### 3. Configure environment variables
Copy the example file and fill in your own values:
```bash
cp .env.example .env
```

Edit `.env`:
```env
PORT=5000
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/todo-list-api?retryWrites=true&w=majority
NODE_ENV=development
```

> On MongoDB Atlas: create a free cluster → Database Access (create a user) → Network Access (allow your IP, or `0.0.0.0/0` for testing) → Connect → "Connect your application" → copy the connection string into `MONGO_URI`.

### 4. Run the server
```bash
# Production
npm start

# Development (auto-restarts on file changes, requires devDependency 'nodemon')
npm run dev
```

You should see:
```
MongoDB connected: <your-cluster-host>
Server running in development mode on port 5000
```

The API is now available at `http://localhost:5000`.

---

## 📡 API Endpoints

Base URL: `http://localhost:5000`

| Method | Endpoint       | Description              | Success Status |
|--------|----------------|---------------------------|-----------------|
| GET    | `/todos`       | Get all todos             | 200             |
| GET    | `/todos/:id`   | Get a single todo by ID   | 200             |
| POST   | `/todos`       | Create a new todo         | 201             |
| PUT    | `/todos/:id`   | Update an existing todo   | 200             |
| DELETE | `/todos/:id`   | Delete a todo             | 200             |

### Todo object shape
```json
{
  "_id": "64f1c2e5a1b2c3d4e5f6a7b8",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "createdAt": "2026-08-02T10:15:30.000Z",
  "updatedAt": "2026-08-02T10:15:30.000Z"
}
```

### Status codes used
| Code | Meaning                                                        |
|------|-----------------------------------------------------------------|
| 200  | Successful GET / PUT / DELETE                                  |
| 201  | Successful POST (resource created)                              |
| 400  | Validation error, malformed request body, or invalid ID format  |
| 404  | Todo not found / unmatched route                                 |
| 500  | Unexpected server error                                          |

---

## 🔍 Example Requests

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
**Response — `201 Created`**
```json
{
  "success": true,
  "data": {
    "_id": "64f1c2e5a1b2c3d4e5f6a7b8",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "createdAt": "2026-08-02T10:15:30.000Z",
    "updatedAt": "2026-08-02T10:15:30.000Z"
  }
}
```

### Get all todos
```bash
curl http://localhost:5000/todos
```
**Response — `200 OK`**
```json
{
  "success": true,
  "count": 1,
  "data": [ { "_id": "64f1c2e5a1b2c3d4e5f6a7b8", "title": "Buy groceries", "...": "..." } ]
}
```

### Get a single todo
```bash
curl http://localhost:5000/todos/64f1c2e5a1b2c3d4e5f6a7b8
```
**Not found — `404 Not Found`**
```json
{ "success": false, "message": "Todo not found with id: 64f1c2e5a1b2c3d4e5f6a7b8" }
```

### Update a todo
```bash
curl -X PUT http://localhost:5000/todos/64f1c2e5a1b2c3d4e5f6a7b8 \
  -H "Content-Type: application/json" \
  -d '{ "completed": true }'
```
**Response — `200 OK`**
```json
{
  "success": true,
  "data": { "_id": "64f1c2e5a1b2c3d4e5f6a7b8", "title": "Buy groceries", "completed": true, "...": "..." }
}
```

### Delete a todo
```bash
curl -X DELETE http://localhost:5000/todos/64f1c2e5a1b2c3d4e5f6a7b8
```
**Response — `200 OK`**
```json
{
  "success": true,
  "message": "Todo 64f1c2e5a1b2c3d4e5f6a7b8 deleted successfully",
  "data": { "_id": "64f1c2e5a1b2c3d4e5f6a7b8", "title": "Buy groceries", "...": "..." }
}
```

### Validation error example
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{ "description": "Missing the title field" }'
```
**Response — `400 Bad Request`**
```json
{ "success": false, "message": "Title is required and must be a non-empty string" }
```

---

## 🧪 Testing with Postman

1. Open Postman → **Import** → select `postman/Todo-List-API.postman_collection.json`.
2. The collection uses a `{{baseUrl}}` variable (defaults to `http://localhost:5000`) and a `{{todoId}}` variable you can set after creating a todo (copy the `_id` from the Create Todo response).
3. Run requests top to bottom: Create → Get All → Get By ID → Update → Delete, plus the included error-case requests (missing title, invalid ID, not-found ID) to demonstrate validation and status codes.
4. Take screenshots of at least two successful requests (e.g. a 201 Create and a 200 Get All) for submission.

---

## ✅ Requirements Checklist

- [x] `GET /todos`, `GET /todos/:id`, `POST /todos`, `PUT /todos/:id`, `DELETE /todos/:id`
- [x] Todo includes `title`, `description`, `completed`, `createdAt`
- [x] Input validation with proper status codes (200, 201, 400, 404)
- [x] Real database (MongoDB) — no in-memory storage
- [x] Project structured into `routes/`, `models/`, `controllers/`
- [x] Centralized error-handling middleware
- [x] README with setup instructions and example requests
- [x] Postman collection included

---

## 📬 Author

**Saad Abdullah** — Embedded Systems & IoT Engineer
📧 saadiabdullah133@gmail.com · 🔗 [linkedin.com/in/saad-abdullah-iot](https://linkedin.com/in/saad-abdullah-iot)
