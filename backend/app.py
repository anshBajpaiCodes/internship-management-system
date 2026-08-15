from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Internship Management System! We welcome you to our project and this is added by lucky using another branch"

if __name__ == "__main__":
    app.run(debug=True)