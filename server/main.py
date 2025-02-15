from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from models.gemini import AppGemini
from models.chatgpt import AppChatGPT

app = Flask(__name__)
CORS(app)

load_dotenv()


@app.route("/api", methods=["GET"])
def home():
    return "SRH AI Assitance API"


@app.route("/api/chat", methods=["POST"])
def ask_ai():
    try:
        data = request.json
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt parameter is required"}), 400

        app_gemini = AppGemini()
        gemini_response = app_gemini.generate_response(prompt)

        app_chatgpt = AppChatGPT()
        gpt_response = app_chatgpt.generate_response(prompt)

        if gpt_response and gemini_response:
            return (
                jsonify(
                    {
                        "gemini": gemini_response,
                        "openai": gpt_response,
                    }
                ),
                200,
            )

        return jsonify({"response": "I couldn't understand you query"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)
