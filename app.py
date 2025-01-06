from flask import Flask, request, render_template, send_file
import os
from predict import predict_and_save

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure upload and processed directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the file
        processed_file_path = process_file(file_path)

        # Return the processed file
        return send_file(processed_file_path, as_attachment=True)

def process_file(file_path):
    # Define paths for processing
    output_file = os.path.join(app.config['PROCESSED_FOLDER'], 'prediction.xlsx')
    
    # Run the prediction function
    predict_and_save(
        learner_path='model/model.pkl',
        input_file=file_path,
        output_file=output_file,
        columns_to_use=['Entre_sem', 'Fin_sem', 'Tpú_capaz', 'VePar_pref']
    )
    
    # Return the processed file path
    return output_file

if __name__ == '__main__':
    app.run(debug=True)
