# career-chatbot
AI chatbot to help students in choosing their career
An AI-powered chatbot to help users discover suitable career paths based on their interests and personality traits.

## Features
- Friendly introduction and supportive tone
- 5–6 interactive questions about your interests and preferences
- Personalized career field recommendation (e.g., Engineering, Medicine, Business, Arts, Military, etc.)
- Motivational message
- Option to restart the conversation

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Flask
- **AI Model:** Groq API (Llama-3.3-70b-versatile)

## Project Screenshot
<!-- Uncomment and add a screenshot if desired -->
<!-- ![Chatbot Screenshot](screenshot.png) -->

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

5. **Open your browser and go to:**
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
- Answer the questions presented by the chatbot.
- After the last question, you'll receive a career recommendation and a motivational message.
- Click the **Restart** button to try again with different answers.

## File Structure
- `app.py` — Flask backend
- `chatbot.html` — Frontend (HTML, CSS, JS, Bootstrap)
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

## .gitignore Example
To avoid uploading unnecessary files, add a `.gitignore` file with:
```
# Python
__pycache__/
*.pyc

# Virtual environment
.venv/
venv/
env/

# OS files
.DS_Store
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Contact
For questions or suggestions, please open an issue or contact the project maintainer.

## Notes
- **API Key:** The Groq API key is currently hardcoded for demonstration. For production, use environment variables for security.
- **Do not upload your `.venv` folder or any sensitive files to GitHub.**

## License
This project is for educational purposes. 
