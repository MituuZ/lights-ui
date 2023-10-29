from flask import Flask, render_template, jsonify, request
from crontab import CronTab
import os

def calculate_selected_option(job):
    if not job.is_enabled():
        return app.config['DISABLED']
    hour = str(job.hour)
    minute = str(job.minute)
    if hour.isdigit() and int(hour) == app.config['SCHEDULE_1_HOUR']:
        if minute.isdigit() and int(minute) == app.config['SCHEDULE_1_MINUTE']:
            return app.config['SCHEDULE_1']
    if hour.isdigit() and int(hour) == app.config['SCHEDULE_2_HOUR']:
        if minute.isdigit() and int(minute) == app.config['SCHEDULE_2_MINUTE']:
            return app.config['SCHEDULE_2']
    return 'No match'

app = Flask(__name__)

@app.route('/')
def home():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.py')

    if os.path.exists(config_path):
        print("Using config.py-file")
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config_example.Config')

    cron = CronTab(user=app.config['USER'])
    cron_data = {}
    for job in cron:
        if 'morning-light.sh' in job.command:
            cron_data[job.comment] = {
                'job': job,
                'selected_option': calculate_selected_option(job)
            }
    
    return render_template('index.html', cron_data=cron_data)

@app.route('/update_cron', methods=['POST'])
def update_cron():
    data = request.json
    job_comment = data.get('job_comment')
    schedule = data.get('schedule')

    cron = CronTab(user=app.config['USER'])
    for job in cron:
        if 'morning-light.sh' in job.command and job.comment == job_comment:
            day_of_week = job.dow
            job.enable()
            if schedule == app.config['SCHEDULE_1']:
                job.setall(f'{app.config["SCHEDULE_1_MINUTE"]} {app.config["SCHEDULE_1_HOUR"]} * * {day_of_week}')
            else:
                job.setall(f'{app.config["SCHEDULE_2_MINUTE"]} {app.config["SCHEDULE_2_HOUR"]} * * {day_of_week}')
            cron.write()
            return jsonify({'status': 'success', 'message': 'Cron job updated: ' + job_comment})
    return jsonify({'status': 'error', 'message': 'Cron job not found.'})

@app.route('/disable_cron', methods=['POST'])
def disable_cron():
    data = request.json
    job_comment = data.get('job_comment')

    cron = CronTab(user=app.config['USER'])
    for job in cron:
        if 'morning-light.sh' in job.command and job.comment == job_comment:
            job.enable(False)
            cron.write()
            return jsonify({'status': 'success', 'message': 'Cron job disabled: ' + job_comment})
    return jsonify({'status': 'error', 'message': 'Cron job not found.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
