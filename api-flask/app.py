import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def welcome():
  return jsonify({'status': 'api working'})

if __name__ == '__main__':
  #define the localhost ip and the port that is going to be used
  # in some future article, we are going to use an env variable instead a hardcoded port 
  app.run(host='0.0.0.0', port=os.getenv('PORT'))