import jinja2
from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    x = ""
    if now.month == 1 and now.day == 1:
        x = "Happy New Year!"
    elif now.month == 12 and now.day == 25:
        x = "Merry Christmas!"
    elif now.month == 10 and now.day == 31:
        x = "Boo!"
    else:
        x = ""
    return render_template('home.html', sp_event=x)
      
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