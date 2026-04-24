from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("API_KEY_GROQ")
client = Groq(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

# --- UNLOCKED TOOL 1: Ask AI ---
@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("text_input")
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are a highly intelligent, direct, and helpful AI assistant. Format your answers clearly."},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=1024
    )
    return jsonify({"response": response.choices[0].message.content}), 200

# --- UNLOCKED TOOL 2: Email Summarizer ---
@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form.get("text_input")
    prompt = f"Summarize the following email clearly and concisely. Extract the main points, action items, and deadlines if any exist:\n\n{text}"
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are an expert executive assistant. Summarize emails perfectly."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=512
    )
    return jsonify({"response": response.choices[0].message.content}), 200

if __name__ == "__main__":
    app.run(debug=True)