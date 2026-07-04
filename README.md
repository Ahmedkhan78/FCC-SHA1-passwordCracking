````md
# SHA-1 Password Cracker 🔐

This project is part of the freeCodeCamp Information Security Certification.

It is a Python-based password cracking tool that uses a dictionary attack to find plaintext passwords from SHA-1 hashes, with optional support for salted hashes.

---

## 🚀 Project Description

The goal of this project is to build a function that can:

- Take a SHA-1 hash as input
- Compare it against a large password list
- Optionally try salted variations of passwords
- Return the matching plaintext password

This simulates how basic brute-force password cracking works in cybersecurity.

---

## 📌 Function Requirements

You must implement:

```python
crack_sha1_hash(hash, use_salts=False)
```
````

### Parameters:

- `hash` → SHA-1 hash string to crack
- `use_salts` → optional boolean to enable salted password checking

---

## 📤 Return Values

### If password is found:

Return the plaintext password:

```
superman
```

---

### If password is NOT found:

Return:

```
PASSWORD NOT IN DATABASE
```

---

## 🧠 How It Works

1. Load a dictionary of common passwords (`top-10000-passwords.txt`)
2. Hash each password using SHA-1
3. Compare with the target hash
4. If no match:
   - If `use_salts=True`, try salted combinations:
     - salt + password
     - password + salt

5. Return result

---

## 🔐 Technologies Used

- Python
- hashlib (SHA-1 hashing)
- File handling
- Brute-force search algorithm

---

## 📁 Project Structure

```
sha1-password-cracker/
│
├── password_cracker.py     # Main logic
├── main.py                 # Entry point for testing
├── test_module.py         # Unit tests
├── top-10000-passwords.txt # Password dictionary
├── known-salts.txt        # Salt values
└── README.md              # Documentation
```

---

## ▶️ How to Run

Run the program:

```bash
python main.py
```

Run tests:

```bash
python test_module.py
```

---

## 🎯 Objective

Understand how password hashing works and how brute-force attacks can be used to crack weak passwords.

This project demonstrates why:

- Strong passwords matter
- Salting is important for security
- Hashing alone is not enough protection

---

## 📚 Reference

Project instructions:
[https://www.freecodecamp.org/learn/information-security/information-security-projects/sha-1-password-cracker](https://www.freecodecamp.org/learn/information-security/information-security-projects/sha-1-password-cracker)

```

```
