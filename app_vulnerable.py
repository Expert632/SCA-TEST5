from flask import Flask, request

app = Flask(__name__)

# Exemple très simple d'appli Flask (le but est pédagogique)
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "world")
    return f"Hello, {name}!"

if __name__ == "__main__":
    # En prod, ce serait déjà discutable, mais ici c'est juste pour le lab
    app.run(host="0.0.0.0", port=5000, debug=True)
