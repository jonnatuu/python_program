from flask import Flask
import html_generator as h

app = Flask(__name__) 

@app.route('/') 
def hello():
    return h.html_body("sisältö")