from flask import Flask

app = Flask('app')

@app.route('/')
def index():
    return 'hello'

app.run(host='localhost', port=5000)