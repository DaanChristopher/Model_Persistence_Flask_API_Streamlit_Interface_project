import joblib
import matplotlib.pyplot as plt
import streamlit as st

MODEL_PATH = "student_pass_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("Student Pass/Fail Prediction")
st.write("Enter a student's name and study hours to get a model prediction.")

student_name = st.text_input("Student name")
study_hours = st.number_input(
    "Study hours",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5,
)

if st.button("Predict"):
    if not student_name.strip():
        st.warning("Please enter the student's name.")
    else:
        prediction = str(model.predict([[study_hours]])[0])
        st.success(f"Prediction for {student_name.strip()}: {prediction}")
        st.write(f"Study hours entered: {study_hours}")
        st.info(
            "How this prediction was generated: the app loaded the saved model "
            "from student_pass_model.joblib and passed the study-hours value "
            "to model.predict(). This version uses study hours only."
        )

        # Bonus: show how the saved model classifies different study-hour values.
        test_hours = list(range(0, 11))
        test_inputs = [[hours] for hours in test_hours]
        predicted_classes = [str(value) for value in model.predict(test_inputs)]
        classes = sorted(set(predicted_classes))
        y_values = [classes.index(label) for label in predicted_classes]

        fig, ax = plt.subplots()
        ax.plot(test_hours, y_values, marker="o")
        ax.set_xlabel("Study hours")
        ax.set_ylabel("Predicted class")
        ax.set_title("Predicted class by study hours")
        ax.set_yticks(range(len(classes)))
        ax.set_yticklabels(classes)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close(fig)
