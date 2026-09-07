# 📝 To-Do List — Python

A simple **To-Do List application written in Python**.

This project was created to practice Python fundamentals, JSON file handling, task management, and the first steps toward integrating cryptography with a Python application.

---

## 📌 Project Overview

The project contains two Python implementations:

* `To_Do_list.py` — basic To-Do List implementation.
* `to-do-list-crypto.py` — To-Do List version with initial work toward integrating **Fernet cryptography**.

The current version focuses mainly on **task management and JSON data storage**. Cryptography is currently being explored and is **not fully implemented yet**.

---

## 📂 Project Structure

```text
To_Do_List-Crypto/
│
├── To_Do_List/
│   ├── To_Do_list.py
│   └── to-do-list-crypto.py
│
└── README.md
```

---

## ⚙️ Features

The To-Do List allows you to:

* ➕ Add a task
* 📋 Display tasks
* 🗑️ Delete a task
* 🆔 Assign an ID to each task
* 📝 Store a task title
* 📄 Store a task body
* 🔄 Manage the task status
* 💾 Store data using JSON

A task follows a structure similar to:

```json
{
    "id": 1,
    "title": "Learn Python",
    "body": "Practice Python functions",
    "status": "pending"
}
```

---

## 🐍 `To_Do_list.py`

This is the basic version of the application.

It uses Python's built-in `json` module to work with task data.

The program provides operations for:

```text
Afficher → Display tasks
Add      → Add a task
Delete   → Delete a task
```

The data is designed to be stored in a JSON file.

---

## 🔐 `to-do-list-crypto.py`

This version is an experiment toward adding cryptography to the application.

It imports:

```python
from cryptography.fernet import Fernet
```

Fernet is a symmetric encryption system provided by the Python `cryptography` library.

The project is currently at the **learning/implementation stage** for this part. The encryption functionality is not yet fully integrated into the task storage workflow.

---

## 🔄 How the Application Works

The basic workflow is:

```text
            To-Do List
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
      Add    Afficher   Delete
       │        │        │
       └────────┼────────┘
                ▼
             JSON
```

The application manages tasks and stores their information in JSON format.

---

## 🛠️ Technologies

* **Python 3**
* **JSON**
* **Cryptography / Fernet** *(experimental)*

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hatimhansal/To_Do_List-Crypto.git
```

Enter the project:

```bash
cd To_Do_List-Crypto
```

Go to the Python files:

```bash
cd To_Do_List
```

### Basic version

Run:

```bash
python To_Do_list.py
```

### Crypto version

First install the `cryptography` package:

```bash
pip install cryptography
```

Then run:

```bash
python to-do-list-crypto.py
```

---

## 📚 What I Learned

This project helped me practice:

* Python functions
* Variables and data types
* Lists and dictionaries
* Conditions
* Loops
* User input
* JSON
* Reading and writing data
* Basic CRUD operations
* Python modules
* Using external libraries
* Introduction to symmetric encryption
* Git and GitHub

---

## 🔮 Future Improvements

The project can be improved by adding:

* [ ] Fully implement Fernet encryption
* [ ] Encrypt the stored task data
* [ ] Secure encryption-key management
* [ ] Add task editing
* [ ] Add task completion functionality
* [ ] Add task priorities
* [ ] Add task deadlines
* [ ] Improve input validation
* [ ] Improve error handling
* [ ] Add a graphical interface
* [ ] Add automated tests

---

## ⚠️ Current Status

This is a **learning project**.

The To-Do List functionality is implemented, while the cryptography part is currently being developed and explored.

The project is **not intended to be a production-ready secure application**.

---

## 👨‍💻 Author

**Hatim Hansal**

GitHub:
https://github.com/hatimhansal

---

## ⭐ Support

If you find this project useful for learning Python, feel free to ⭐ the repository.
