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

@app.route('/cn')
def home_cn():
    now = datetime.datetime.now()
    x = ""
    if now.month == 1 and now.day == 1:
        x = "新年快乐!"
    elif now.month == 12 and now.day == 25:
        x = "圣诞快乐!"
    elif now.month == 10 and now.day == 31:
        x = "万圣节!"
    else:
        x = ""
    return render_template('chinese/home_cn.html', sp_event=x)
      
@app.route('/about/cn')
def about_cn():
    return render_template('chinese/about_cn.html')

@app.route('/firstever/cn')
def firstever_cn():
    return render_template('chinese/firstever_cn.html')

@app.route('/chatgpt/cn')
def chatgpt_cn():
    return render_template('chinese/chatgpt_cn.html')

@app.route('/ai_img/cn')
def ai_img_cn():
    return render_template('chinese/ai_img_cn.html')

    
if __name__ == '__main__':
    app.run(debug=True)