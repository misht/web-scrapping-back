from flask import Flask

from src.routes import user_bp

app = Flask(__name__)


app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    return 'Web Scrapping'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
