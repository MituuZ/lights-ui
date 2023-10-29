from flask import Flask, render_template, jsonify, request
from crontab import CronTab
import os

def calculate_selected_option(job):
    if not job.is_enabled:
        return app.config['DISABLED']
    hour = str(job.hour)
    if hour.isdigit() and int(hour) < 5:
        return app.config['SCHEDULE_1']
    if hour.isdigit() and int(hour) < 7:
        return app.config['SCHEDULE_2']
    return 'No match'

app = Flask(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.py')

if os.path.exists(config_path):
    app.config.from_object('config.Config')
else:
    app.config.from_object('config_example.Config')

cron = CronTab(user=app.config['USER'])
cron_data = {}
for job in cron:
    if 'morning-light.sh' in job.command and job.is_enabled:
        cron_data[job.comment] = {
            'job': job,
            'selected_option': calculate_selected_option(job)
        }

@app.route('/')
def home():
    return render_template('index.html', cron_data=cron_data)

@app.route('/update_cron', methods=['POST'])
def update_cron():
    data = request.json
    job_comment = data.get('job_comment')
    scheduler = data.get('scheduler')
    print('Updating job: ' + job_comment)

    cron = CronTab(user=app.config['USER'])
    for job in cron:
        if 'morning-light.sh' in job.command and job.comment == job_comment:
            job.enable()
            if scheduler == app.config['SCHEDULE_1']:
                job.hour.on = app.config['SCHEDULE_1_HOUR']
                job.minute.on = app.config['SCHEDULE_1_MINUTE']
            else:
                job.hour.on = app.config['SCHEDULE_2_HOUR']
                job.minute.on = app.config['SCHEDULE_2_MINUTE']
            print('Updated job: ' + job_comment)
            cron.write()
            return jsonify({'status': 'success', 'message': 'Cron job updated.'})
    return jsonify({'status': 'error', 'message': 'Cron job not found.'})

@app.route('/disable_cron', methods=['POST'])
def disable_cron():
    data = request.json
    job_comment = data.get('job_comment')
    print('Disabling job: ' + job_comment)

    cron = CronTab(user=app.config['USER'])
    for job in cron:
        if 'morning-light.sh' in job.command and job.comment == job_comment:
            job.enable(False)
            cron.write()
            print('Disabled job: ' + job_comment)
            return jsonify({'status': 'success', 'message': 'Cron job disabled.'})
    return jsonify({'status': 'error', 'message': 'Cron job not found.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
