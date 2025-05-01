from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Червено хабанеро", "description": "Супер люта чушка!", "price": 7.99},
    {"id": 2, "name": "Халапеньо", "description": "Средно люта чушка..", "price": 4.50},
    {"id": 3, "name": "Каролина рийпър", "description": "Супер люта чушка!", "price": 7.99},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
