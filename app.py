from flask import Flask, render_template
from crontab import CronTab
import os

def calculate_selected_option(job):
    hour = str(job.hour)
    if hour.isdigit() and int(hour) < 5:
        return app.config['SCHEDULE_1']
    if hour.isdigit() and int(hour) < 7:
        return app.config['SCHEDULE_2']
    if not job.is_enabled:
        return app.config['DISABLED']
    return 'No match'

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
        cron_data[job.comment] = {
            'job': job,
            'selected_option': calculate_selected_option(job)
        }

@app.route('/')
def home():
    return render_template('index.html', cron_data=cron_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
