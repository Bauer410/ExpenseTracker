CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount FLOAT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

CREATE VIEW IF NOT EXISTS user_expenses AS
SELECT users.username, categories.category_name, expenses.amount, expenses.date, expenses.description
FROM expenses
JOIN users ON expenses.user_id = users.user_id
JOIN categories ON expenses.category_id = categories.category_id;

-- to check the total expenses by each user
SELECT user_id, SUM(amount) AS total_spent
FROM expenses
GROUP BY user_id;

-- To Check expenses by category
SELECT category_id, SUM(amount) AS total_spent
FROM expenses
GROUP BY category_id;

-- Display
SELECT * FROM users;
SELECT * FROM categories;
SELECT * FROM expenses;



