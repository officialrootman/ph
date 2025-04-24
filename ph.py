from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form action="/login" method="post">
        Kullanıcı Adı: <input type="text" name="username"><br>
        Şifre: <input type="password" name="password"><br>
        <input type="submit" value="Giriş Yap">
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(f"Kullanıcı Adı: {username}, Şifre: {password}")
    return "Bilgiler kaydedildi. Teşekkürler!"

if __name__ == "__main__":
    app.run(port=8080)