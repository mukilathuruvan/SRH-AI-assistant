from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from database.connection import DatabaseManager
from AI.open_router import OpenRouter
from dotenv import load_dotenv

app=Flask(__name__)
CORS(app)

load_dotenv()

@app.route('/api', methods=['GET'])
def home():
    return "SRH AI Assitance API"

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        query = data.get('query')

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400
        
        agent=OpenRouter()
        agent_response = agent.ask(query)

        if agent_response:
            return jsonify({"answer": agent_response,"query":query}), 200
        
        return jsonify({"error": "No answer found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = DatabaseManager.get_courses()  # Get all courses from the database
        if courses:
            return jsonify([{
                "id": course.id,
                "name": course.coursename,
                "duration": course.duration,
                "semester_fee": course.semester_fee,
            } for course in courses]), 200  # Return courses as JSON
            
        

        return jsonify({"error": "No courses found"}), 404  # If no courses are found
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors
 
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)
