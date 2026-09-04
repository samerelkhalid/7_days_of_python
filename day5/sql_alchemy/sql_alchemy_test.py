from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

app.run(host='127.0.0.1', port=5000)