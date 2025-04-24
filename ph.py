from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba, Dünya! Bu benim ilk web sitem!"

if __name__ == '__main__':
    app.run(debug=True)