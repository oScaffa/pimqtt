from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hi</h1>"

@app.route("/about")
def about():
    return "<h1>Bye</h1>"

###---------Run the webpage
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
