from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def home():
    return "SRH AI Assitance API"

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        query = data['query']
        answer = "I don't know the answer to that query"
        return jsonify({"answer": answer,"query":query}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)
