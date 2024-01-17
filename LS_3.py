from flask import Flask, render_template, request
import bcrypt

app = Flask(__name__)

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        user = User(first_name, last_name, email, password)
        user.save_to_database()

        return "Регистрация успешна!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
