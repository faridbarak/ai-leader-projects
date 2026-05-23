const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");
const clearAllBtn = document.getElementById("clearAllBtn");

const STORAGE_KEY = "todoTasks";

// Load tasks from localStorage on page load
function loadTasks() {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
  return saved.map((task) => ({
    id: task.id,
    text: task.text,
    completed: !!task.completed,
  }));
}

// Save tasks array to localStorage
function saveTasks(tasks) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

// Render all tasks
function renderTasks() {
  const tasks = loadTasks();
  taskList.innerHTML = "";

  if (tasks.length === 0) return;

  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.className = "task-item";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.addEventListener("change", () => toggleTask(task.id));

    const span = document.createElement("span");
    span.className = "task-text";
    if (task.completed) span.classList.add("completed");
    span.textContent = task.text;

    const delBtn = document.createElement("button");
    delBtn.className = "delete-btn";
    delBtn.textContent = "✕";
    delBtn.addEventListener("click", () => deleteTask(task.id));

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);
    taskList.appendChild(li);
  });
}

// Add a new task
function addTask() {
  const text = taskInput.value.trim();
  if (!text) return;

  const tasks = loadTasks();
  const id = Date.now();

  tasks.unshift({
    id,
    text,
    completed: false,
  });

  saveTasks(tasks);
  renderTasks();
  taskInput.value = "";
}

// Toggle task done/undone
function toggleTask(id) {
  const tasks = loadTasks();
  const task = tasks.find((t) => t.id === id);
  if (task) {
    task.completed = !task.completed;
    saveTasks(tasks);
    renderTasks();
  }
}

// Delete a task
function deleteTask(id) {
  const tasks = loadTasks().filter((t) => t.id !== id);
  saveTasks(tasks);
  renderTasks();
}

// Clear all tasks
function clearAllTasks() {
  saveTasks([]);
  renderTasks();
}

// Event listeners
addBtn.addEventListener("click", addTask);
taskInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") addTask();
});
clearAllBtn.addEventListener("click", clearAllTasks);

// Initial render
window.addEventListener("load", renderTasks);