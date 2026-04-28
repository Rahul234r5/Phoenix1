from google import genai
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

# --- THE NEW STABLE SETUP ---
# Replace with your actual key
API_KEY = "AIzaSyDBwBf8kMcCbn99LR7Ub2LjV1iRFIv5eZg" 

# Initialize the new client
client = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1'})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'money-key-123'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    user_exists = User.query.filter_by(email=email).first()
    if not user_exists:
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_review = data.get('review')
    prompt = f"Write a professional response to this customer review: '{user_review}'"
    
    try:
        # The new way to call the model
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"New Library Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)