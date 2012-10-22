import os
from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello Cybertron!'

@app.route('/stunticons.json')
def stunticons():
  data = ["Motormaster", "Dead End", "Breakdown", "Wildrider", "Drag Strip"]
  resp = Response(json.dumps(data), status=200, mimetype='application/json')
  return resp

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)
