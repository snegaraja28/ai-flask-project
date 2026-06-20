from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- CHATBOT ----------------
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    response = ""
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()

        if "hello" in user_input:
            response = "Hi! How can I help you?"
        elif "internship" in user_input:
            response = "Start with Python, ML, and projects."
        else:
            response = "I don't understand."

    return render_template('chatbot.html', response=response)

# ---------------- RESUME ----------------
@app.route('/resume', methods=['GET', 'POST'])
def resume():
    feedback = ""
    if request.method == 'POST':
        text = request.form['resume_text']

        suggestions = []
        if "python" not in text.lower():
            suggestions.append("Add Python skills")
        if "project" not in text.lower():
            suggestions.append("Mention projects")
        if len(text.split()) < 100:
            suggestions.append("Resume too short")

        feedback = "\n".join(suggestions) if suggestions else "Good resume!"

    return render_template('resume.html', feedback=feedback)

# ---------------- IMAGE ----------------
@app.route('/image', methods=['GET', 'POST'])
def image():
    result = ""
    if request.method == 'POST':
        file = request.files['image']
        img = Image.open(file)

        width, height = img.size
        result = "Landscape Image" if width > height else "Portrait Image"

    return render_template('image.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)