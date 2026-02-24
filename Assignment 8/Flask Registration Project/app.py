from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)

#------------------------------------------------------------------
# Secret key
#------------------------------------------------------------------
app.config['SECRET_KEY'] = 'mysecretkey123'

#------------------------------------------------------------------
# Database configuration
#------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#------------------------------------------------------------------ 
# Create Database Model
#------------------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)

#------------------------------------------------------------------
#Register Route
#------------------------------------------------------------------


@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Create new user
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("success"))

    return render_template("register.html", form=form)

#------------------------------------------------------------------
#Success Route
#------------------------------------------------------------------

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # Create database tables
    app.run(debug=True)