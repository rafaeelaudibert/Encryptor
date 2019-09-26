from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# ROUTING
@app.route('/api/', methods=['GET'])
def root():
    return jsonify({'content': 'Hello World!'})
