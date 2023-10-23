import sqlite3
from datetime import datetime

# Connected to the Db
conn = sqlite3.connect('todo_database.db')
c = conn.cursor()

# table
c.execute('''
          CREATE TABLE IF NOT EXISTS todos
          (id INTEGER PRIMARY KEY,
           item TEXT,
           description TEXT,
           status INTEGER,
           due_date DATE,
           timestamp DATETIME)
          ''')

    
# to add an item to the database
def add_item_to_db(item, description, due_date):
    try:
       
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        while True:
            user_input = input("Do you want to continue? (yes/no): ")
            if user_input.lower() == 'yes':
                return
            elif user_input.lower() == 'no':
                print("Good Bye")
                exit()

    timestamp = datetime.now()
    c.execute("INSERT INTO todos (item, description, status, due_date, timestamp) VALUES (?, ?, ?, ?, ?)",
              (item, description, 0, due_date, timestamp))
    conn.commit()
    print("Item added:", item)


# Func to mark an item as done

def mark_item_as_done():
    c.execute("SELECT * FROM todos")
    rows = c.fetchall()
    for row in rows:
        item_id, item_text, description, status, due_date, timestamp = row
        status_message = "Done" if status else "Not Done"
        print(f"Item {item_id}: {item_text} ({status_message})")
        print(f"   Description: {description}")
        print(f"   Due Date: {due_date}")
        print(f"   Added at: {timestamp}")
    
    item_id = input("What item ID do you want to mark as done?")
    c.execute("UPDATE todos SET status = 1 WHERE id=?", (item_id,))
    conn.commit()

# Function to search item by ID
def search_item_by_id():
    item_id = input("Enter the item ID you want to search for: ")
    c.execute("SELECT * FROM todos WHERE id=?", (item_id,))
    row = c.fetchone()
    if row:
        item_id, item_text, description, status, due_date, timestamp = row
        status_message = "Done" if status else "Not Done"
        print(f"Item {item_id}: {item_text} ({status_message})")
        print(f"   Description: {description}")
        print(f"   Due Date: {due_date}")
        print(f"   Added at: {timestamp}")
    else:
        print(f"No item found with ID {item_id}.")



# Function to view items
def view_items():
    c.execute("SELECT * FROM todos")
    rows = c.fetchall()
    for row in rows:
        item_id, item_text, description, status, due_date, timestamp = row
        status_message = "Done" if status else "Not Done"
        print(f"Item {item_id}: {item_text} ({status_message})")
        print(f"   Description: {description}")
        print(f"   Due Date: {due_date}")
        print(f"   Added at: {timestamp}")



# fucn to date
def filter_by_date(date):
    c.execute("SELECT * FROM todos WHERE due_date = ?", (date,))
    rows = c.fetchall()
    if rows:
        print(f"Tasks for {date}:")
        for row in rows:
            item_id, item_text, description, status, due_date, timestamp = row
            status_message = "Done" if status else "Not Done"
            print(f"Item {item_id}: {item_text} ({status_message})")
            print(f"   Description: {description}")
            print(f"   Due Date: {due_date}")
            print(f"   Added at: {timestamp}")
    else:
        print(f"No tasks found for {date}.")





# Fun to filter  status

def filter_by_status(status):
    status_value = 1 if status.lower() == 'done' else 0
    c.execute("SELECT * FROM todos WHERE status = ?", (status_value,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            item_id, item_text, description, status, due_date, timestamp = row
            status_message = "Done" if status else "Not Done"
            print(f"Item {item_id}: {item_text} ({status_message})")
            print(f"   Description: {description}")
            print(f"   Due Date: {due_date}")
            print(f"   Added at: {timestamp}")
    else:
        status_message = "Done" if status_value else "Not Done"
        print(f"No tasks found marked as {status_message}.")







# Function to show the menu
def showMenu():
    print("Menu::")
    print("1: Add an item")
    print("2: Mark as done")
    print("3: View items")
    print("4: Filter by date")
    print("5: Filter by status")
    print("6: Search item by ID")
    print("7: Exit")

# Functi show the filtr menu
def showFilterMenu():
    print("Filter Menu:")
    print("1: Show Done Tasks")
    print("2: Show Not Done Tasks")

user_input = 'random'
print("Plz enter command")


while user_input != '7':
    showMenu()
    user_input = input("Enter your choice:")

    if user_input == '1':
        item = input("Please enter your item:")
        description = input("Please enter a description:")
        due_date = input("Please enter a due date (YYYY-MM-DD):")
        add_item_to_db(item, description, due_date)
    elif user_input == '2':
        mark_item_as_done()

    elif user_input == '3':
        print("List of to-do items:")
        view_items()
    elif user_input == '4':
        date = input("Please enter a date to filter tasks (YYYY-MM-DD):")
        filter_by_date(date)
    elif user_input == '5':
        showFilterMenu()
        filter_input = input("Enter your choice:")
        if filter_input == '1':
            filter_by_status('done')
        elif filter_input == '2':
            filter_by_status('not done')
    elif user_input == '6':
        search_item_by_id()
    elif user_input != '7':
        print("Invalid command. Please enter a valid option (1-7).")

# connection ended 
conn.close()

print("Good Bye")
