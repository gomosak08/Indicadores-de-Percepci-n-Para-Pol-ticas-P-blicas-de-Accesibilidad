# Flask File Processor App

### Overview
This is a Flask-based web application that allows users to upload Excel files (.xlsx), processes them using a machine learning model, and returns the processed file as a downloadable Excel file.

---

## Features
- Upload an Excel file (`.xlsx`) through a user-friendly web interface.
- Processes the file with a pre-trained machine learning model.
- Returns a processed Excel file for download.
- Organized storage of uploaded and processed files.

---

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - Flask
  - Pandas
  - FastAI
  - OpenPyXL (for handling Excel files)

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Directory Structure
Ensure the following directories and files exist:
```bash
project/
├── app.py                     # Main Flask app
├── predict.py                 # Prediction function
├── templates/
│   └── index.html             # Frontend HTML
├── uploads/                   # Stores uploaded files
├── processed/                 # Stores processed files
├── model/
│   └── model.pkl              # Pre-trained machine learning model
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Running the Application
### 1. Start the Flask Server
```bash
python app.py
```
The app will be available at: http://127.0.0.1:5000

### 2. Access the Web Interface
- Open the above link in your browser.
- Upload an Excel file (.xlsx) for processing.
- Download the processed file once available.

## How It Works
- Upload File: User uploads an .xlsx file through the interface.
- Process File: The app processes the file using the pre-trained machine learning model (model.pkl).
- Download Processed File: The processed file is made available for download.
## Configuration
### Default Upload and Processed Directories
The app stores files in the following locations:

- Uploaded Files: uploads/
- Processed Files: processed/
### Change Directories
If needed, you can update the default directories in app.py:
```
app.config['UPLOAD_FOLDER'] = 'your_upload_folder'
app.config['PROCESSED_FOLDER'] = 'your_processed_folder'
```
## Dependencies
Install all dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```
Key dependencies include:
- Flask: For creating the web interface.
- Pandas: For data manipulation.
- FastAI: For running the machine learning model.
- OpenPyXL: For reading and writing Excel files.
## Notes
- Ensure your model.pkl is compatible with the structure of the input data.
- Input Excel files must include the following columns:
    - Entre_sem
    - Fin_sem
    - Tpú_capaz
    - VePar_pref
## Example Workflow
1. User uploads an Excel file named `example.xlsx` with the required columns.
2. The app processes the file and appends predictions to it.
3. The user downloads the modified file as `processed_prediction.xlsx`.

## Future Improvements
- Add support for additional file formats (e.g., .csv).
- Enhance error handling and user feedback.
- Deploy the app using a cloud platform like Heroku or AWS.
## License
This project is licensed under the MIT License. Feel free to modify and distribute it.