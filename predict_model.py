import joblib

model = joblib.load("student_pass_model.joblib")
study_hours_values = [2, 5, 8]

for hours in study_hours_values:
    prediction = model.predict([[hours]])[0]
    print(f"Study hours: {hours} -> Prediction: {prediction}")
