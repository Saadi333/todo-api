const express = require('express');
require('dotenv').config();
console.log("Check loaded Mongo URI -->", process.env.MONGO_URI);
const connectDB = require('./config/db');
const todoRoutes = require('./routes/todoRoutes');
const { errorHandler, notFound } = require('./middleware/errorHandler');

const app = express();

// Connect to MongoDB
connectDB();

// Body parser
app.use(express.json());

// Health check / root route
app.get('/', (req, res) => {
  res.status(200).json({
    success: true,
    message: 'Todo List REST API is running',
    endpoints: {
      getAllTodos: 'GET /todos',
      getTodoById: 'GET /todos/:id',
      createTodo: 'POST /todos',
      updateTodo: 'PUT /todos/:id',
      deleteTodo: 'DELETE /todos/:id',
    },
  });
});

// API routes
app.use('/todos', todoRoutes);

// 404 handler (unmatched routes)
app.use(notFound);

// Centralized error handler (must be registered last)
app.use(errorHandler);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server running in ${process.env.NODE_ENV || 'development'} mode on port ${PORT}`);
});

module.exports = app;
