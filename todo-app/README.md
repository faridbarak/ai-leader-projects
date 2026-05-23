# 📋 To-Do List Application

A modern, feature-rich to-do list application with local storage functionality. Manage your tasks efficiently with a beautiful and intuitive interface.

## Features

✅ **Add Tasks** - Quickly add new tasks to your to-do list

✅ **Mark Complete** - Check off tasks as you complete them

✅ **Edit Tasks** - Modify task descriptions

✅ **Delete Tasks** - Remove individual tasks

✅ **Filter Tasks** - View all tasks, only active, or only completed

✅ **Task Statistics** - See total, active, and completed task counts

✅ **Local Storage** - All tasks are automatically saved to browser storage

✅ **Timestamps** - Each task includes a creation timestamp

✅ **Responsive Design** - Works perfectly on desktop and mobile devices

✅ **Beautiful UI** - Modern gradient design with smooth animations

✅ **XSS Protection** - Safe HTML escaping for task content

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- No additional installations needed!

### Installation

1. Download or clone the repository
2. Open `index.html` in your web browser
3. Start adding tasks!

### Files

- `index.html` - Application structure
- `styles.css` - Styling and layout
- `script.js` - Core functionality and local storage management
- `README.md` - This file

## Usage

### Adding a Task
1. Type your task in the input field
2. Press Enter or click "Add Task" button
3. Task will appear at the top of the list

### Completing a Task
- Click the checkbox next to a task to mark it as complete
- Completed tasks will show a strikethrough and appear faded

### Editing a Task
1. Click the edit icon (pencil) on the task
2. Update the task text in the prompt
3. Click OK to save

### Deleting a Task
- Click the delete icon (trash) on the task to remove it

### Filtering Tasks
Use the filter buttons to view:
- **All** - Display all tasks
- **Active** - Show only incomplete tasks
- **Completed** - Show only finished tasks

### Clearing Tasks
- **Clear Completed** - Remove all finished tasks
- **Clear All** - Delete all tasks (shows confirmation)

### Statistics
At the top, you can see:
- **Total** - Total number of tasks
- **Active** - Number of incomplete tasks
- **Completed** - Number of finished tasks

## Local Storage

Your tasks are automatically saved to your browser's local storage:
- Data persists even after closing the browser
- All data is stored locally on your device (no server needed)
- Storage key: `todos`
- To clear all data: Clear browser cache/storage

## Data Structure

Each task is stored as:
```javascript
{
    id: timestamp (unique identifier),
    text: "task description",
    completed: boolean,
    createdAt: "date/time string"
}
```

## Browser Support

- ✅ Chrome/Chromium (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Responsive design with gradients and animations
- **JavaScript (ES6+)** - Core functionality
- **Local Storage API** - Data persistence
- **Font Awesome** - Beautiful icons

## Tips & Tricks

1. **Keyboard Shortcut** - Press Enter while typing to quickly add a task
2. **Quick Overview** - Use filters to focus on specific types of tasks
3. **Cleanup** - Regularly use "Clear Completed" to keep your list organized
4. **Mobile Friendly** - Works great on smartphones and tablets

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Add Task | Enter |
| Focus Input | Click on input field |

## Known Limitations

- Tasks are stored per browser/device (not synced across devices)
- Maximum storage depends on browser (usually 5-10MB)
- Clearing browser cache will delete all tasks

## Future Enhancements

- [ ] Task priorities (High, Medium, Low)
- [ ] Due dates and reminders
- [ ] Categories/tags for tasks
- [ ] Recurring tasks
- [ ] Task search functionality
- [ ] Dark mode theme
- [ ] Export/Import tasks
- [ ] Cloud sync across devices
- [ ] Subtasks support
- [ ] Time tracking

## Troubleshooting

### Tasks not saving?
- Check if your browser allows local storage
- Try clearing cache and refreshing the page
- Check browser console for errors (F12)

### Data lost after refresh?
- Ensure cookies and storage are enabled in your browser
- Check if you're using private/incognito mode (storage is cleared on exit)

### Tasks not appearing?
- Refresh the page
- Check browser console for JavaScript errors
- Clear browser cache and reload

## License

Free to use and modify for personal and commercial projects.

## Contributing

Feel free to fork and submit improvements!

## Support

For issues or questions, check the browser console (F12) for error messages.
