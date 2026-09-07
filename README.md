# 🔐 To-Do List Crypto

A simple **To-Do List application with data encryption**, written in Python.

This project combines basic task management with **cryptography** to protect stored data.

It was created as a practical project to learn Python, file handling, JSON, encryption, and basic data security.

> ⚠️ **Disclaimer:** This project is intended for educational purposes. It should not be considered a production-ready security application.

---

## 📌 Features

* ✅ Create tasks
* 📋 View tasks
* ✏️ Manage tasks
* 🗑️ Delete tasks
* 💾 Store task data locally
* 🔐 Encrypt sensitive stored data
* 🔓 Decrypt data when the application needs to read it
* 🐍 Built with Python

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

## 🐍 To_Do_list.py

`To_Do_list.py` contains the basic To-Do List functionality.

It focuses on managing tasks and practicing Python fundamentals such as:

* Variables
* Lists
* Functions
* Loops
* Conditions
* User input
* File handling

Run it with:

```bash
python To_Do_list.py
```

---

## 🔐 to-do-list-crypto.py

`to-do-list-crypto.py` is the security-focused version of the project.

It adds encryption to protect the stored task data.

The general workflow is:

```text
User
 │
 ▼
Create / Modify Task
 │
 ▼
Task Data
 │
 ▼
Encryption 🔐
 │
 ▼
Encrypted Storage
 │
 ▼
Decryption 🔓
 │
 ▼
Application
```

This version was created to understand how encryption can be integrated into a Python application.

---

## 🛠️ Technologies

* **Python 3**
* JSON
* File handling
* `cryptography`
* Encryption / Decryption

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

Go to the project directory:

```bash
cd To_Do_List
```

Install the required dependency:

```bash
pip install cryptography
```

Then run:

```bash
python to-do-list-crypto.py
```

---

## 🔑 Encryption Concept

The project uses encryption to make stored data unreadable without the required key.

Instead of storing data like:

```text
Task: Learn Python
Task: Study Networking
Task: Build a project
```

the stored content is encrypted.

Conceptually:

```text
Plain Data
    │
    ▼
Encryption 🔐
    │
    ▼
Encrypted Data
    │
    ▼
Storage
```

When the application needs the data:

```text
Encrypted Data
    │
    ▼
Decryption 🔓
    │
    ▼
Original Data
```

---

## 📚 What I Learned

This project helped me practice:

* Python programming
* Functions
* Lists and dictionaries
* JSON
* Reading and writing files
* Exception handling
* Working with external Python libraries
* Encryption and decryption
* Basic data protection
* Git and GitHub

---

## 🔮 Future Improvements

Possible improvements:

* [ ] Add a graphical interface
* [ ] Add task priorities
* [ ] Add task deadlines
* [ ] Add task categories
* [ ] Add search functionality
* [ ] Improve encryption key management
* [ ] Add password-based authentication
* [ ] Add encrypted backup
* [ ] Improve error handling
* [ ] Add automated tests

---

## 🔐 Security Note

Encryption helps protect stored information, but **key management is extremely important**.

If the encryption key is lost, encrypted data may no longer be recoverable.

For real-world applications, additional security practices should be implemented before using the project to protect sensitive information.

---

## 👨‍💻 Author

**Hatim Hansal**

GitHub:

https://github.com/hatimhansal

---

## ⭐ Project

If you find this project useful for learning Python and basic cryptography, feel free to ⭐ the repository.
