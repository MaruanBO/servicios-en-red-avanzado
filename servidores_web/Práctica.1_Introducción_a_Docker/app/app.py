
from flask import Flask

app = Flask(__name__)
@app.route("/")

def main():
    return "Welcome to the first Flask App by Maruan Boukhriss!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
