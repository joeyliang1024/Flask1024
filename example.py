from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    while True:
        return (str(datetime.datetime.now()))

def about():
    return 'About this website'
app.add_url_rule('/about', 'about', about)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False)

