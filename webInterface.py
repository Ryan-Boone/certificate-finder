from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from darsPars import darsProcessor

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the DARS report
            courses = darsProcessor(filepath)
            # Convert courses to dictionary for JSON response
            courses_data = [
                {
                    'term': c.term,
                    'department': c.department,
                    'number': c.number,
                    'credits': c.credits,
                    'grade': c.grade,
                    'name': c.name
                } for c in courses
            ]
            
            # Clean up
            os.remove(filepath)
            
            return jsonify({
                'success': True,
                'courses': courses_data
            })
        except Exception as e:
            return jsonify({'error': str(e)})
        
    return jsonify({'error': 'Invalid file type'})

if __name__ == '__main__':
    app.run(debug=True)