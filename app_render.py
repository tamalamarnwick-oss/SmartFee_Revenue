from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'render-secret-key-2024')

# Database configuration for Render
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url.replace("postgres://", "postgresql://", 1)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartfee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Minimal database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default='admin')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    form_class = db.Column(db.String(50), nullable=False)
    pta_amount_paid = db.Column(db.Float, default=0.0)
    sdf_amount_paid = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize database
def init_db():
    try:
        with app.app_context():
            db.create_all()
            # Create default admin if none exists
            if not User.query.first():
                admin = User(
                    username=os.environ.get('DEFAULT_USERNAME', 'CWED'),
                    password=os.environ.get('DEFAULT_PASSWORD', 'RNTECH'),
                    role='admin'
                )
                db.session.add(admin)
                db.session.commit()
                print("Default admin created")
            print("Database initialized")
    except Exception as e:
        print(f"Database init error: {e}")

# Routes
@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    try:
        total_students = Student.query.count()
        total_income = db.session.query(db.func.sum(Student.pta_amount_paid + Student.sdf_amount_paid)).scalar() or 0
        return render_template('index.html', total_students=total_students, total_income=total_income)
    except Exception as e:
        return f'<h1>Dashboard</h1><p>Students: 0</p><p>Income: MK 0.00</p><p>System running successfully</p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            # Check developer credentials
            if username == os.environ.get('DEV_USERNAME', 'CWED') and password == os.environ.get('DEV_PASSWORD', 'RNTECH'):
                session['logged_in'] = True
                session['username'] = username
                session['user_role'] = 'developer'
                return redirect(url_for('index'))
            
            # Check database user
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['logged_in'] = True
                session['username'] = username
                session['user_role'] = user.role
                return redirect(url_for('index'))
            
            return render_login_form('Invalid credentials')
        except Exception as e:
            return render_login_form(f'Login error: {str(e)}')
    
    return render_login_form()

def render_login_form(error=None):
    try:
        return render_template('login.html', error=error)
    except:
        return f'''<!DOCTYPE html>
<html><head><title>SmartFee Login</title></head>
<body style="font-family: Arial, sans-serif; max-width: 400px; margin: 100px auto; padding: 20px;">
<h1>SmartFee Login</h1>
{f'<p style="color: red;">{error}</p>' if error else ''}
<form method="POST">
<div style="margin: 10px 0;">
<input type="text" name="username" placeholder="Username" required style="width: 100%; padding: 10px;">
</div>
<div style="margin: 10px 0;">
<input type="password" name="password" placeholder="Password" required style="width: 100%; padding: 10px;">
</div>
<button type="submit" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none;">Login</button>
</form>
</body></html>'''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/students')
def students():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    try:
        students = Student.query.all()
        return render_template('students.html', students=students)
    except Exception as e:
        return f'<h1>Students</h1><p>Error loading students: {str(e)}</p><p><a href="/">Back to Dashboard</a></p>'

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            student = Student(
                student_id=request.form['student_id'],
                name=request.form['name'],
                sex=request.form['sex'],
                form_class=request.form['form_class']
            )
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('students'))
        except Exception as e:
            return f'<h1>Error</h1><p>Failed to add student: {str(e)}</p><p><a href="/students">Back</a></p>'
    
    try:
        return render_template('add_student.html')
    except:
        return '''<h1>Add Student</h1>
<form method="POST">
<p><input type="text" name="student_id" placeholder="Student ID" required></p>
<p><input type="text" name="name" placeholder="Name" required></p>
<p><select name="sex" required><option value="">Select Sex</option><option value="Male">Male</option><option value="Female">Female</option></select></p>
<p><input type="text" name="form_class" placeholder="Form/Class" required></p>
<p><button type="submit">Add Student</button></p>
</form>'''

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}), 200

# Initialize on startup
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)