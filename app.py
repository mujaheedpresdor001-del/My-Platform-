
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Platform</h1>
    <p>This platform was created by Muhammad Mujahid 🚀</p>
    """

if __name__ == "__main__":
    app.run()
