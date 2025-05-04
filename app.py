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

# Ensure the app runs on the appropriate host and port for deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env var if set
    app.run(host='0.0.0.0', port=port, debug=True)
