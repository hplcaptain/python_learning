from flask import  Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Home function
@app.route('/')
def home():
    return redirect(url_for('register'))

#Register Function
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        return redirect(url_for('success', username=name))
    return render_template('register.html')

#Success Function
@app.route('/success/<username>')
def success(username):
    return render_template('success.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)


