from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return ('Hello from zain and me  ')


app.run(host='0.0.0.0', debug=True)
