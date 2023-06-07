"""Pagina"""
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    """def index"""
    return "<marquee>Pagina de Emmanuel</marquee>"
if __name__=='__main__':
    app.run(host='0.0.0.0',port='6021')

