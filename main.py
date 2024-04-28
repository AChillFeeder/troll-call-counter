from flask import Flask, render_template, redirect
import json
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def index():
    data = get_data()
    date_of_last_call = datetime.strptime(data["day_of_last_call"], "%d-%m-%y").date()
    difference = date.today() - date_of_last_call
    return render_template('index.html', data=data, difference=difference.days)

@app.route('/reset_counter')
def reset_counter():
    data = get_data()
    data["days_after_last_call"] = 0
    data["day_of_last_call"] = datetime.today().strftime("%d-%m-%y")
    write_data(data)
    return redirect('/')

def get_data():
    with open('stats.json', 'r') as file:
        data = json.loads(file.read())
        print(f"data logged: {data}")
        return data
    
def write_data(data):
    with open('stats.json', 'w') as file:
        file.write(json.dumps(data))
    return True

if __name__ == '__main__':
    app.run('0.0.0.0',5500,debug=True)
