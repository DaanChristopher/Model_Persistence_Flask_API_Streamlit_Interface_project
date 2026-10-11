"""Train a small demonstration model and save it for the exercise apps.

This is a teaching example with made-up sample labels, not a real student
assessment tool. Replace the sample data with your course/project data when
available.
"""

import joblib
from sklearn.linear_model import LogisticRegression

# Input feature: study hours. Output label: Pass or Fail.
# This small, illustrative dataset is only for demonstrating model persistence.
X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [
    "Fail", "Fail", "Fail", "Fail", "Pass", "Pass",
    "Pass", "Pass", "Pass", "Pass", "Pass",
]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "student_pass_model.joblib")
print("Model trained and saved as student_pass_model.joblib")
print("This is sample teaching data, not a validated real-world prediction model.")
