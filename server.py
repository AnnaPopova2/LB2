from flask import Flask, request  # Імпортуємо Flask

app = Flask(__name__)  # Створюємо додаток Flask

@app.route("/", methods=['GET'])  # Обробляємо GET-запит на головному маршруті
def hello_world():
    return "Hello World!"  # Повертаємо текст

if __name__ == '__main__':
    app.run(port=5000)  # Запускаємо сервер на порту 5000