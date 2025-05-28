# 🔐 SQL Injection Detector & Data Leak Prevention

A secure, cloud-enabled web application designed to prevent SQL injection attacks and safely store sensitive user data using AES-256 encryption.

## 🚀 Features

- ✅ **SQL Injection Protection** via parameterized queries and input sanitization
- 🔐 **AES-256 Encryption** for storing sensitive information securely
- 🌐 **Cloud-Ready**: Works seamlessly over the Internet (deployable to Heroku, AWS, etc.)
- 🛡️ **Double-Layer Security**:
  - Layer 1: Prepared statements
  - Layer 2: Capability tokens to detect and deny unauthorized requests
- 📊 **Frontend UI**: Clean HTML/CSS form with JS-based validation

---

## 🛠️ Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Python Flask        |
| Database   | MySQL               |
| Security   | AES-256 (`cryptography` library) |
| Hosting    | Heroku / AWS        |

---

## 📁 Project Structure

/sql-injection-detector
├── app.py
├── config.py
├── requirements.txt
├── utils/
│ ├── db.py
│ ├── encrypt.py
│ └── sanitizer.py
├── templates/
│ └── index.html
└── static/
├── style.css
└── script.js


---

## 🧩 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Multiverse-of-Rudra/sql-injection-detector.git
cd sql-injection-detector

2. Create the MySQL Database
sql:
CREATE DATABASE securedb;
USE securedb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    info TEXT
);
3. Set Environment Variables
Set the following environment variables (via .env or shell):

export DB_HOST=localhost
export DB_USER=your_mysql_user
export DB_PASS=your_mysql_password
export DB_NAME=securedb
export SECRET_KEY=your_flask_secret_key
export AES_KEY=your_32byte_base64_key
export CAP_TOKEN=your_capability_token

✅ To generate a 32-byte base64 key for AES:

bash:
python -c "import os, base64; print(base64.b64encode(os.urandom(32)).decode())"
4. Install Python Dependencies
bash:
pip install -r requirements.txt
5. Run the Flask App
bash:
python app.py
Open your browser and go to: http://localhost:5000

📦 How It Works
Form Submission: Users submit their name, email, and sensitive information.

Validation & Token Check: Capability token is validated to authorize the request.

Sanitization & Encryption:

SQL injection is prevented using prepared statements.

Sensitive data is encrypted using AES-256.

Database Storage: The encrypted data is saved to a secure MySQL database.

📊 Viewing Stored Data
In MySQL CLI:
sql
Copy
Edit
USE securedb;
SELECT * FROM users;
Or Use a GUI Tool:
MySQL Workbench

phpMyAdmin

DBeaver

Note: The info field will appear encrypted.

🧪 Testing
Try submitting normal text, SQL payloads (e.g., ' OR '1'='1), or scripts. The system will:

Reject suspicious input

Encrypt valid data before storing


🧑‍💻 Author
Your Rudra Mohan Mishra
Made as part of the CodeAlpha Internship Program
GitHub: Multiverse-of-Rudra

📄 License
This project is licensed under the MIT License.

🔒 Future Enhancements
JWT-based user authentication

Admin panel to decrypt and manage data securely

Integration with cloud KMS for key management

Detailed logging and anomaly detection

🤝 Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

