from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Initialize Groq client (API key should be secured in production)
client = Groq(api_key="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")

# List of questions for the chatbot
QUESTIONS = [
    "What subjects do you enjoy the most?",
    "Do you prefer working with people, data, or things?",
    "Do you like solving problems or creating new things?",
    "Do you enjoy working indoors or outdoors?",
    "Do you prefer structured tasks or creative freedom?",
    "What motivates you the most: helping others, innovation, leadership, or stability?"
]

@app.route('/')
def index():
    return open('chatbot.html').read()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    answers = data.get('answers', [])
    # Compose prompt for Groq LLM
    prompt = f"""
You are a supportive and motivating career guidance assistant. Based on the following answers, recommend a suitable career field (Engineering, Medicine, Business, Arts, Military, etc.) and provide a motivational message.\n\nAnswers: {answers}\n\nRespond in 2-3 sentences.\n"""
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile"
    )
    reply = chat_completion.choices[0].message.content
    return jsonify({'reply': reply})

@app.route('/questions')
def get_questions():
    return jsonify({'questions': QUESTIONS})

if __name__ == '__main__':
    app.run(debug=True) 