Application Setup

# Create new Virtual env named venv
1.  Python -m venv venv

# Activate the envirnments 
2.   .\venv\Scripts\activate
 
# Installed if not installed sqlite3 via pip or conda
3.    pip3 install --upgrade sqlite3    OR    conda install -c conda-forge sqlite

#
4. if you want to have your own database from step 1 then follow following

  # Command
  sqlite3 app.db
  # Quries to create new tables
  CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    quantity INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
