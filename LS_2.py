from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']

    response = make_response(render_template('welcome.html', name=name))
    response.set_cookie('name', name)
    response.set_cookie('email', email)
    return response

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

if __name__ == '__main__':
    app.run()