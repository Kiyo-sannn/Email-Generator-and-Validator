# Email Generator and Validator (PyQt5)

A desktop application built with **Python** and **PyQt5** that generates and validates email addresses. The app supports user-based email generation, random email creation, regex-based validation, and a modern dark-themed graphical user interface.

---

## 📌 Features

* **User-Based Email Generation**
  Generate email addresses using a person's full name and birth year or full birthdate.

* **Random Email Generation**
  Create randomized email usernames using different patterns and character combinations.

* **Email Validation**
  Validate email usernames using regular expressions to ensure correct formatting.

* **Duplicate Validation Detection**
  Prevents re-validating previously validated email addresses.

* **Modern Dark UI**
  Clean and minimal dark-mode interface using PyQt5 stylesheets.

* **Menu-Based Navigation**
  Uses `QStackedWidget` for smooth navigation between screens.

---

## 🛠 Technologies Used

* **Python 3**
* **PyQt5** – GUI Framework
* **Regex (`re`)** – Email validation
* **Datetime & Calendar** – Birthdate processing
* **Random** – Randomized email generation

---

## 📂 Project Structure

```
email-generator-validator/
│
├── main.py          # Main application file
├── README.md        # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/email-generator-validator.git
cd email-generator-validator
```

2. **Install dependencies**

```bash
pip install PyQt5
```

3. **Run the application**

```bash
python main.py
```

---

## 🚀 Usage

### Generate Email (Using Info)

1. Enter your **Full Name** (Format: `Last First [Middle]`).
2. Enter **Birth Year** (`YYYY`) or **Birthdate** (`YYYY-MM-DD`).
3. Click **Generate Using Info**.

### Generate Email (Random)

* Click **Generate Randomly** to create random email addresses.

### Validate Email

1. Enter an email address.
2. Click **Validate**.
3. The app will confirm whether the email format is valid.

---

## 🧪 Validation Rules

* Must contain `@`
* Username allows only:

  * Letters (`a–z`, `A–Z`)
  * Numbers (`0–9`)
  * Dots (`.`) and underscores (`_`)

---

## 📸 Screenshots (Optional)

*Add screenshots of the UI here for better presentation.*

---

## 🎓 Educational Purpose

This project was developed as a **learning and portfolio project**, focusing on:

* GUI development with PyQt5
* Input validation
* Regex usage
* Desktop application design

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project.

---

## 👤 Author

**Gereuel Brillantes**
BSIT Student – Guagua National Colleges, Inc.

---

## ⭐ Acknowledgments

* PyQt5 Documentation
* Python Official Documentation

If you find this project helpful, consider giving it a ⭐ on GitHub.
