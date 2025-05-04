from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the recommendation route
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    # Get the job description or query from the request body
    data = request.get_json()  # This will parse the incoming JSON data
    job_description = data.get("job_description", "")
    
    print(f"Received job description: {job_description}")

    # Check if job description is provided
    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    # Call the function that handles SHL recommendations (replace this with real logic)
    recommendations = get_shl_recommendations(job_description)

    # Return the recommendations as a JSON response
    return jsonify({"recommendations": recommendations})

# Dummy function to simulate SHL recommendations
def get_shl_recommendations(job_description):
    recommendations = []
    jd = job_description.lower()
    if "python" in jd or "software" in jd:
        recommendations.append({
            "assessment": "Python Coding Test",
            "category": "Technical",
            "level": "Intermediate"
        })
    if "communication" in jd or "management" in jd:
        recommendations.append({
            "assessment": "Leadership & Communication",
            "category": "Behavioral",
            "level": "Advanced"
        })
    if not recommendations:
        recommendations.append({
            "assessment": "General Aptitude",
            "category": "Cognitive",
            "level": "Basic"
        })
    return recommendations

