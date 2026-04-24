# 📧 Gistify | AI Assistant

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-10b981?style=for-the-badge&logoColor=white)

## 🚀 Overview

**Gistify** is a sleek, modern AI-powered web application designed to help users process information faster. Featuring a highly interactive split-screen interface inspired by premium writing tools, Gistify currently offers advanced email summarization and a general-purpose AI assistant, powered by the lightning-fast Groq API and Llama 3.

## ✨ Features

- **📧 Email Summarizer:** Instantly condense lengthy emails into clear summaries, extracting main points, action items, and deadlines.
- **💬 Ask AI:** A highly intelligent research assistant ready to answer questions, brainstorm ideas, or draft content.
- **🖥️ Premium UI/UX:**
  - Seamless Split-Screen Editor
  - Real-time live word counters
  - One-click "Copy to Clipboard" functionality
  - Interactive toast notifications
  - Clean, modern Emerald Green & Soft Cream aesthetic
- **🔒 Future-Proof Dashboard:** UI prepared for upcoming V2 features including Paraphraser and Grammar Checker.

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python, Flask
- **AI Engine:** Groq API (Model: `llama-3.1-8b-instant`)
- **Deployment Ready:** Configured for seamless deployment on Vercel (`vercel.json` included)

## 🚀 Local Setup & Installation

To run Gistify locally on your machine, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/Priyanshu-pandey1/Gistify.git
cd Gistify
```

### 2. Set up environment variables
Create a `.env` file in the root directory and add your Groq API Key:
```env
API_KEY_GROQ=your_groq_api_key_here
```
(Note: Ensure `.env` is included in your `.gitignore` file to keep your API key secure.)

### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
```bash
python main.py
```

### 5. Open in Browser
Navigate to http://127.0.0.1:5000 to start using Gistify!

## ☁️ Deployment

This project is configured for easy deployment on Vercel:

- Import the repository into your Vercel dashboard.
- Add your `API_KEY_GROQ` to the Environment Variables settings.
- Deploy! Vercel will automatically use the provided `vercel.json` and `requirements.txt` to build the Flask backend.

## 👨‍💻 Author

**Priyanshu Pandey**

- GitHub: @Priyanshu-pandey1
- Focus: AI/ML & Frontend Development