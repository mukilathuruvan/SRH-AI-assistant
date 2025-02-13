from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from AI.open_router import AI

app = Flask(__name__)
CORS(app)

load_dotenv()


@app.route("/api", methods=["GET"])
def home():
    return "SRH AI Assitance API"


@app.route("/api/ask", methods=["POST"])
def ask_ai():
    try:
        data = request.json
        query = data.get("query")

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        agent = AI()
        gemini_response = agent.ask_gemini(query)
        gpt_response = agent.ask_gpt(query)

        # formatted_text = agent_response.replace("\n", "\n\n")  # Adds extra line breaks

        response = {
            "gemini_response": gemini_response,
            "gpt_response": gpt_response,
        }

        if gemini_response and gpt_response:
            return jsonify(response), 200

        return jsonify({"error": "No answer found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
