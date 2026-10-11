from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

# Create this file first by saving your trained model in train_model.py.
MODEL_PATH = "student_pass_model.joblib"
model = joblib.load(MODEL_PATH)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object in the request body."}), 400

    try:
        study_hours = float(data["study_hours"])
        attendance_percentage = float(data["attendance_percentage"])
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Provide numeric study_hours and attendance_percentage values."
        }), 400

    if study_hours < 0:
        return jsonify({"error": "study_hours must be 0 or greater."}), 400

    if not 0 <= attendance_percentage <= 100:
        return jsonify({"error": "attendance_percentage must be between 0 and 100."}), 400

    # This model was trained using study_hours only. Attendance is validated
    # and returned, but it does not influence this prediction yet.
    prediction = str(model.predict([[study_hours]])[0])

    return jsonify({
        "study_hours": study_hours,
        "attendance_percentage": attendance_percentage,
        "prediction": prediction,
    })


if __name__ == "__main__":
    app.run(debug=True)
