document.addEventListener('DOMContentLoaded', function () {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevents the form from submitting and refreshing the page

        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            // Create a new task item
            const taskItem = createTaskItem(taskText);

            // Append the new task to the task list
            taskList.appendChild(taskItem);

            // Clear the input field
            taskInput.value = '';
        }
    });

    function createTaskItem(text) {
        // Create a new list item
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${text}</span>
            <button onclick="deleteTask(this)">Delete</button>
        `;

        return listItem;
    }

    window.deleteTask = function (button) {
        const listItem = button.parentElement;
        taskList.removeChild(listItem);
    };
});

