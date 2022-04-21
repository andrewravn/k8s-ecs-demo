from dotenv import load_dotenv
from flask import Flask, render_template
import os 

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

@app.route("/")
def home():
    load_dotenv(override=True)
    return render_template('index.html', color=os.getenv('COLOR', 'light-blue'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')