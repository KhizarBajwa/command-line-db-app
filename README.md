#Application Setup  # MyDatabaseApp

MyDatabaseApp is a command-line database application.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mydatabaseapp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mydatabaseapp
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install .
    ```

## Usage

1. Run the application:

    ```bash
    mydatabaseapp
    ```

    This will execute the main functionality of the application.

## Uninstallation

1. Deactivate the virtual environment (if used):

    ```bash
    deactivate
    ```

2. Optionally, remove the virtual environment and the cloned repository.

## Notes

- Make sure you have Python 3.x installed.

#Not Required but if you want to work on your own sqlite
--------------------------------------------------------------------------
# Installed if not installed sqlite3 via pip or conda
  pip3 install --upgrade sqlite3    OR    conda install -c conda-forge sqlite


if you want to have your own database from step 1 then follow following

  # Command
      sqlite3 app.db
     
     -- Create users table
     CREATE TABLE users (
         id INTEGER PRIMARY KEY,
         name TEXT,
         email TEXT
     );
     
     -- Insert sample users
     INSERT INTO users (name, email) VALUES
         ('John Doe', 'john.doe@example.com'),
         ('Jane Smith', 'jane.smith@example.com'),
         ('Bob Johnson', 'bob.johnson@example.com');
     
     -- Create orders table
     CREATE TABLE orders (
         id INTEGER PRIMARY KEY,
         user_id INTEGER,
         product TEXT,
         quantity INTEGER,
         FOREIGN KEY (user_id) REFERENCES users(id)
     );
     
     -- Insert sample orders
     INSERT INTO orders (user_id, product, quantity) VALUES
         (1, 'Product A', 2),
         (2, 'Product B', 1),
         (1, 'Product C', 3),
         (3, 'Product D', 5);


--------------------------------------------------------------------------



## Screen shots

![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/df0ec493-33ec-4d09-9280-7be3a9f1af16)

give command as 'mydatabaseapp' and press enter
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/760dbc43-74b9-4191-a340-5bbb9d4813ed)

Welcome Screen
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/f4670f32-0d34-45d1-8670-023eda89d042)

enter '-h' to view all commands
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/bbc02599-d6d4-4a26-a503-401b604ca2dc)

enter '1' to view all users from database table
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/6966fe58-e689-400e-b373-1bd6311188cb)

enter '5' to get all orders of the users
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/c158c541-47f0-4922-b3b4-fee2516a1cbc)
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/7e4ff15f-8dea-47ec-870c-44cc35fc2275)
![image](https://github.com/KhizarBajwa/command-line-db-app/assets/48625072/d140636f-df77-4f83-9d52-63e4ffdc8a65)

And reset you can explore on your own !!!

