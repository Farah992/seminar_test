from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "7516911026:AAEaQ4L2Jyu8B9apFRK0Q1XOgGFH9mmc9IE"

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(debug=True)

