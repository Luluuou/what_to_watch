from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_view():
    print(app.config)
    return 'Совсем скоро тут будет случайное мнение о фильме!'

if __name__ == '__main__':
    app.run()
