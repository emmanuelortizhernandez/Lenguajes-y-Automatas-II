from app import app
from flask import render_template
import xlsdata

@app.route("/")
@app.route("/index")
def index():
    titlew = xlsdata.getTitle()
    print (titlew)
    aboutImg = xlsdata.getAboutImg()
    print (aboutImg)
    aboutText = xlsdata.getAboutText()
    print(aboutText)
    return render_template('index.html',title=titlew, aboutText = aboutText, aboutImg = aboutImg)
