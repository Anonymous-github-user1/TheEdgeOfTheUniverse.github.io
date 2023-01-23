import jinja2
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/firstever')
def firstever():
    return render_template('firstever.html')

@app.route('/chatgpt')
def chatgpt():
    return render_template('chatgpt.html')

@app.route('/ai_img')
def ai_img():
    return render_template('ai_img.html')
    
if __name__ == '__main__':
    app.run(debug=True)