from flask import Flask, render_template, request
import anthropic
import markdown
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["user_message"]
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a construction technology advisor specialising in the UK construction industry. Provide clear, practical, and accurate guidance on construction technology, digital workflows, BIM, UK contract forms, CDM Regulations, site management, project delivery, and industry best practices. Tailor responses to UK standards and terminology, explain technical concepts in a concise and professional manner, highlight compliance or safety considerations where relevant, and acknowledge uncertainty rather than making unsupported assumptions.",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    response = markdown.markdown(message.content[0].text)
    return render_template("index.html", response=response, user_message=user_message)

if __name__ == "__main__":
    app.run(debug=True)