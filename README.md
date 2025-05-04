# SHL Assessment Recommendation System

This is a Flask-based API that recommends SHL assessments based on a given job description.

## 📌 Features

- Accepts job description input via POST request.
- Returns mock SHL assessment recommendations (customizable).
- Built with Python and Flask.
- API endpoint: `/recommendations`

## 🚀 How to Run the App

### 1. Clone or download the repository

Navigate to your desired folder and run:

bash
cd shl-recommendation-system

### 2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate

### 3. Install dependencies
bash
Copy
Edit
pip install flask

### 4. Run the Flask app
bash
Copy
Edit
python app.py

### 5. Test the API with Postman
Method: POST

URL: http://127.0.0.1:5000/recommendations

Headers:

Content-Type: application/json

Body (raw JSON):

json
Copy
Edit
{
  "job_description": "Software engineer with expertise in Python and JavaScript"
}
✅ Example Response:
json
Copy
Edit
{
  "recommendations": [
    {
      "assessment": "Assessment 1",
      "category": "Technical",
      "level": "Intermediate"
    },
    {
      "assessment": "Assessment 2",
      "category": "Behavioral",
      "level": "Advanced"
    }
  ]
}

### 📁 Project Structure
perl
Copy
Edit
shl-recommendation-system/
│
├── app.py
├── README.md
├── venv/
