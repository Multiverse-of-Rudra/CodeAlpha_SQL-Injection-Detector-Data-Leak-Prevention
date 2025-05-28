from flask import Flask, render_template, request, redirect
from config import Config
from utils.db import Database
from utils.encrypt import AESEncryptor
from utils.sanitizer import sanitize_input
import base64, os

app = Flask(__name__)
db = Database()
aes = AESEncryptor(base64.b64decode(Config.AES_KEY))

@app.route('/', methods=['GET', 'POST'])
def index():
    success = False
    if request.method == 'POST':
        token = request.headers.get('X-CAPABILITY-TOKEN')
        if token != Config.CAPABILITY_TOKEN:
            return "Unauthorized", 403

        name = sanitize_input(request.form['name'])
        email = sanitize_input(request.form['email'])
        info = aes.encrypt(request.form['info'])

        db.insert_user(name, email, info)
        success = True

    users = db.fetch_users()
    return render_template("index.html", success=success, users=users)


if __name__ == '__main__':
    app.run(debug=True)
