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
cd shl-recommendation-system

### 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

### 3. Install dependencies
pip install flask

### 4. Run the Flask app
python app.py

### 5. Test the API with Postman
Method: POST
URL: http://127.0.0.1:5000/recommendations

Headers:
Key: Content-Type, Value: application/json

Body (raw JSON):
json
Copy
Edit
{
  "job_description": "Software engineer with expertise in Python and JavaScript"
}

✅ Example Response:

json
{
  "recommendations": [
    {
      "assessment": "Python Coding Test",
      "category": "Technical",
      "level": "Intermediate"
    },
    {
      "assessment": "Leadership & Communication",
      "category": "Behavioral",
      "level": "Advanced"
    }
  ]
}

### 📁 Project Structure
plaintext
shl-recommendation-system/
│
├── app.py
├── README.md
├── venv/
pgsql
This version includes all the necessary steps to clone the repository, set up the virtual environment, install dependencies, run the app, and test the API with Postman.






