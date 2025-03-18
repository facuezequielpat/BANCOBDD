# Bank Management System (CRUD)

A Python-based system for managing bank users, deposits, withdrawals, and transaction history. This project includes a MySQL database for storing user data and a command-line interface for interacting with the system.

## 📁 Project Structure
- **`Banco.sql`**: SQL script to create the database, tables, and triggers for managing users, deposits, withdrawals, and transaction history.
- **`Banco1.py`**: Python class (`Conectar`) to handle database connections and CRUD operations (Create, Read, Update, Delete).
- **`Banco2.py`**: Python class (`Metodos`) to handle user input and logic for managing users, deposits, withdrawals, and history.
- **`menu.py`**: Main menu-driven interface for interacting with the system.


## 📄 Estructura de la Base de Datos

Tabla persona: Almacena los detalles del usuario (DNI, nombre, apellido).

Tabla dep_ret: Almacena depósitos, retiros, saldo y fecha de transacción para cada usuario.

Tabla bitacoraTrigger: Registra todas las acciones (inserciones, actualizaciones, eliminaciones) con fines de auditoría.

### Triggers

after_insert_dep_ret: Registra nuevos usuarios.

after_update_dep_ret: Registra actualizaciones de datos de usuarios.

after_delete_dep_ret: Registra eliminaciones de usuarios.

## 🧭 Menu Features

1	Register User: Collects DNI, name, surname, deposit, and withdrawal (validates withdrawal ≤ deposit).

2	Show Users: Lists all registered users with their details (DNI, name, surname, deposit, withdrawal, balance, and date).

3	Search User: Finds a user by DNI and displays their details.

4	Edit Balance: Updates deposits and withdrawals for an existing user.

5	Edit All: Modifies all user data (name, surname, deposit, withdrawal, and balance).

6	Delete User: Removes a user by DNI.

7	View History: Displays the transaction history (registrations, edits, and deletions).

8	Exit: Closes the program.


## 🛠 Requirements
- **Python 3.6 or higher**
- **MySQL Server**
- **`mysql-connector-python`**: Install using `pip install mysql-connector-python`.

## 🚀 Installation & Execution
1. **Clone the repository**:
   ```bash
   git clone https://github.com/facuezequielpat/BANCOBDD
