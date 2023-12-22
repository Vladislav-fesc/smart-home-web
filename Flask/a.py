from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    # Здесь вы можете подставить ваш код для получения температурных данных
    # Например, если у вас есть датчик температуры, используйте его для получения текущей температуры.
    temperature = 25.5  # Пример температуры

    # Возвращаем температуру в формате JSON
    return jsonify({'temperature': temperature})

if __name__ == '__main__':
    app.run(host='::', port=5000, debug=True)


