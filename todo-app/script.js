// To-Do List Application with Local Storage

const todoInput = document.getElementById('todoInput');
const addBtn = document.getElementById('addBtn');
const todoList = document.getElementById('todoList');
const emptyState = document.getElementById('emptyState');
const filterButtons = document.querySelectorAll('.filter-btn');
const clearCompletedBtn = document.getElementById('clearCompletedBtn');
const clearAllBtn = document.getElementById('clearAllBtn');
const totalCount = document.getElementById('totalCount');
const activeCount = document.getElementById('activeCount');
const completedCount = document.getElementById('completedCount');

let todos = [];
let currentFilter = 'all';
const STORAGE_KEY = 'todos';

// Initialize app
window.addEventListener('load', () => {
    loadTodos();
    renderTodos();
    updateStats();
});

// Event Listeners
addBtn.addEventListener('click', addTodo);
todoInput.addEventListener('keypress', (e) => e.key === 'Enter' && addTodo());
filterButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        currentFilter = e.target.dataset.filter;
        filterButtons.forEach((b) => b.classList.remove('active'));
        e.target.classList.add('active');
        renderTodos();
    });
});
clearCompletedBtn.addEventListener('click', clearCompleted);
clearAllBtn.addEventListener('click', clearAll);

// Add new todo
function addTodo() {
    const text = todoInput.value.trim();
    if (text === '') return;

    const todo = {
        id: Date.now(),
        text: text,
        completed: false,
        createdAt: new Date().toLocaleString(),
    };

    todos.unshift(todo);
    saveTodos();
    renderTodos();
    updateStats();
    todoInput.value = '';
    todoInput.focus();
}

// Toggle todo completion
function toggleTodo(id) {
    const todo = todos.find((t) => t.id === id);
    if (todo) {
        todo.completed = !todo.completed;
        saveTodos();
        renderTodos();
        updateStats();
    }
}

// Delete todo
function deleteTodo(id) {
    todos = todos.filter((t) => t.id !== id);
    saveTodos();
    renderTodos();
    updateStats();
}

// Edit todo
function editTodo(id) {
    const todo = todos.find((t) => t.id === id);
    if (todo) {
        const newText = prompt('Edit task:', todo.text);
        if (newText && newText.trim() !== '') {
            todo.text = newText.trim();
            saveTodos();
            renderTodos();
        }
    }
}

// Clear all completed todos
function clearCompleted() {
    if (confirm('Are you sure you want to delete all completed tasks?')) {
        todos = todos.filter((t) => !t.completed);
        saveTodos();
        renderTodos();
        updateStats();
    }
}

// Clear all todos
function clearAll() {
    if (confirm('Are you sure you want to delete ALL tasks? This cannot be undone.')) {
        todos = [];
        saveTodos();
        renderTodos();
        updateStats();
    }
}

// Filter todos based on current filter
function getFilteredTodos() {
    switch (currentFilter) {
        case 'active':
            return todos.filter((t) => !t.completed);
        case 'completed':
            return todos.filter((t) => t.completed);
        default:
            return todos;
    }
}

// Render todos to the DOM
function renderTodos() {
    const filteredTodos = getFilteredTodos();
    todoList.innerHTML = '';

    if (filteredTodos.length === 0) {
        emptyState.classList.add('show');
        return;
    }

    emptyState.classList.remove('show');

    filteredTodos.forEach((todo) => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.innerHTML = `
            <input 
                type="checkbox" 
                class="checkbox" 
                ${todo.completed ? 'checked' : ''}
                onchange="toggleTodo(${todo.id})"
            >
            <span class="todo-text">${escapeHtml(todo.text)}</span>
            <span class="todo-date">${todo.createdAt}</span>
            <div class="todo-actions">
                <button class="edit-btn" onclick="editTodo(${todo.id})" title="Edit">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="delete-btn" onclick="deleteTodo(${todo.id})" title="Delete">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;
        todoList.appendChild(li);
    });
}

// Update statistics
function updateStats() {
    const total = todos.length;
    const completed = todos.filter((t) => t.completed).length;
    const active = total - completed;

    totalCount.textContent = total;
    activeCount.textContent = active;
    completedCount.textContent = completed;
}

// Save todos to local storage
function saveTodos() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}

// Load todos from local storage
function loadTodos() {
    const stored = localStorage.getItem(STORAGE_KEY);
    todos = stored ? JSON.parse(stored) : [];
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
