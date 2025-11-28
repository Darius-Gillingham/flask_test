
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask server is running on Railway!"

if __name__ == "__main__":
    # Railway assigns PORT automatically; default to 5000 if not present.
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
