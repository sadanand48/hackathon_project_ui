from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

import os

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def foo():
    c1 = request.form['release']
    cmd = 'sh /Users/sadanand.shenoy/run_build.sh ' + str(c1) + ' 2>&1 | tee /Users/sadanand.shenoy/results.txt'
    stream = os.popen(cmd)
    output = stream.read()
    return '<html><body><h1>Test Triggered</h1><br><h2>Command run:' + cmd + '</h2></body></html>'

if __name__ == '__main__':
    app.run()
