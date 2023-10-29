from flask import Flask, render_template
from crontab import CronTab
import os

app = Flask(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.py')

if os.path.exists(config_path):
    print('Found')
    app.config.from_object('config.Config')
else:
    print('Not found')
    app.config.from_object('config_example.Config')

cron = CronTab(user=app.config['USER'])
cron_data = {}
for job in cron:
    if 'morning-light.sh' in job.command:
        cron_data[job.comment] = job

items = list(cron_data.items())

for item in items:
    print(item)
    print(item[0])

@app.route('/')
def home():
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
