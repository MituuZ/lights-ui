from flask import Flask, render_template
import os

app = Flask(__name__)

if os.path.exists('config.py'):
    app.config.from_object('config.Config')
else:
    app.config.from_object('config_example.Config')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
