# Lights UI
A simple one-page Flask application for controlling a single cronjob.

Provides a week view with three options per day to run the cronjob at timer 1, timer 2 or not at all.

# Article
I wrote an article about why and how I created this project, you can read it [here](https://mituuz.com/content/crontab_python_ui.html).

# Running the project
Requires python3.

## Using venv
If you've already created a venv, you can jump to [activating the virtual environment](#activating-the-virtual-environment).

Or if you don't want to use env, you can jump to [installing requirements.txt](#installing-requirementstxt).

### Creating a virtual environment
To use a venv for the project, we first need to create it, if it doesn't exist. This creates a venv folder
to the project root.
```bash
python3 -m venv ./venv
```

### Activating the virtual environment
Assuming you're using bash, you can activate the virtual environment with the following command.
```bash
source ./venv/bin/activate
```

## Installing requirements.txt
To install the required dependencies, you'll need to install them using pip.

```bash
pip install -r requirements.txt
```

## Starting the ui
Mostly for testing, blocks the current shell.
```bash
python3 app.py
```

Start the ui in the background and keep it running even after the shell session is closed.
```bash
nohup python3 app.py &
```

# Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

Website: https://palletsprojects.com/p/flask/
License: BSD-3-Clause
Copyright: 2010 by Pallets

BSD-3-Clause License:  
Copyright 2010 Pallets

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
