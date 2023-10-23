# Python To-Do CLI App

This Python To-Do CLI (Command Line Interface) application allows users to manage their tasks efficiently. It is built using Python's built-in `sqlite3` module to provide seamless data storage and retrieval.

## Features

The application comes with the following features:

1. **Add an Item**: Add a new task to the to-do list.
2. **Mark as Done**: Mark a task as completed.
3. **View Items**: Display all tasks in the to-do list.
4. **Filter by Date**: View tasks based on their due dates.
5. **Filter by Status**: View tasks based on their completion status.
6. **Search Item by ID**: Find a specific task using its unique ID.
7. **Exit**: Close the application.

## Usage

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/itxTouseef74/To-Do-CLI.git

   ```

3. Navigate to the project directory:

   ```bash
   cd python-to_do.py
   ```

4. Run the application:

   ```bash
   python to_do.py
   ```

5. Follow the on-screen prompts to utilize the different features.

## Database

The application uses a SQLite database to store task information. The database file (`todo.db`) will be created automatically when you run the application.

## Example Usage

1. To add a new item, select option `1` and follow the prompts.

2. To mark a task as done, select option `2` and enter the task ID.

3. To view all items, select option `3`.

4. To filter tasks by date, select option `4` and follow the prompts.

5. To filter tasks by status, select option `5` and enter `1` for completed or `0` for pending tasks.

6. To search for an item by ID, select option `6` and enter the task ID.

7. To exit the application, select option `7`.

## Contributing

Contributions are welcome! If you want to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request explaining your changes.


## Acknowledgments

- This project was developed to provide a functional and efficient to-do list management solution using Python and SQLite.
