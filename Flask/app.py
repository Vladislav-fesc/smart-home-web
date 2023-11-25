from flask import Flask, render_template, jsonify
from datetime import datetime
import random
import plotly
import plotly.graph_objs as go

app = Flask(__name__)

# Имитация данных с датчиков
sensor_data = {
    'temperature1': 25.0,
    'temperature2': 22.5,
    'temperature3': 24.0,
    'temperature4': 23.5
}
temperature_history = []
time_history = []

@app.route('/')
def index():
    return render_template('index.html', sensor_data=sensor_data)

@app.route('/update_data', methods=['POST'])
def update_data():
    global temperature_history, time_history

    # Обновление данных с датчиков
    for sensor in sensor_data:
        sensor_data[sensor] = round(sensor_data[sensor] + (0.5 - 1.0 * random.random()), 2)

    # Добавление новых данных в историю
    current_time = datetime.now().strftime('%H:%M')
    temperature_history.append({
        'time': current_time,
        'temperature1': sensor_data['temperature1'],
        'temperature2': sensor_data['temperature2'],
        'temperature3': sensor_data['temperature3'],
        'temperature4': sensor_data['temperature4']
    })

    # Ограничение истории в 20 точках
    if len(temperature_history) > 20:
        temperature_history = temperature_history[-20:]

    # Возвращение данных в формате JSON для обновления веб-страницы
    return jsonify({'sensor_data': sensor_data, 'temperature_history': temperature_history})

if __name__ == '__main__':
    app.run(debug=True)


                