from flask import Flask, render_template

app = Flask(__name__)

@app.route('/next')
def hello_world():
    return 'next page'

if__name__=="__main__":
app.run()debug =True)
