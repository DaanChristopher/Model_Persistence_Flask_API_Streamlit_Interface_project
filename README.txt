COMPLETED EXERCISE CODE — MODEL PERSISTENCE, FLASK API, AND STREAMLIT

FIRST: IMPORTANT NOTE
The original train_model.py was not in the uploaded files. To make these examples runnable, this folder now includes a small sample train_model.py that creates student_pass_model.joblib.
The sample data is illustrative only; it is not a validated model for assessing real students. If you already have your own train_model.py and trained model, use your own training data/model instead.

WINDOWS POWERSHELL — FIRST-TIME SETUP
1. Download and extract the ZIP.
2. Open the extracted exercise_solution_code folder in File Explorer.
3. Click the folder address bar, type powershell, and press Enter.
4. Run these commands one at a time:

    python --version
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

If PowerShell blocks activation, run this in the same PowerShell window, then activate again:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
    .\.venv\Scripts\Activate.ps1

If `python` is not recognized, try replacing `python` with `py` in the commands.

STEP 1 — CREATE THE SAVED MODEL (DO THIS FIRST)
Run:

    python train_model.py

It creates student_pass_model.joblib in this same folder. You only need to train again if you change the training data or training code.

EXERCISE 1 — MODEL PERSISTENCE
Run:

    python predict_model.py

It loads the saved model and predicts for 2, 5, and 8 study hours.

EXERCISE 2 — FLASK API
Start the API:

    python app.py

Leave that PowerShell window running. Open a SECOND PowerShell window in the same folder, activate the environment if needed, then test:

    curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"study_hours":5,"attendance_percentage":90}'

The response is JSON containing study hours, attendance percentage, and the prediction. Attendance is validated and returned, but does not influence the model because this example trains on study hours only.
To stop Flask, press Ctrl+C in its window.

EXERCISE 3 — STREAMLIT INTERFACE
In a PowerShell window in the same folder, run:

    python -m streamlit run streamlit_app.py

A browser should open to the Streamlit page (usually http://localhost:8501). Enter a student's name, choose study hours, and click Predict.
To stop Streamlit, press Ctrl+C in its PowerShell window.

TROUBLESHOOTING
- FileNotFoundError for student_pass_model.joblib: run `python train_model.py` first and ensure you are in this folder.
- ModuleNotFoundError: activate .venv and run `python -m pip install -r requirements.txt`.
- The Flask API is not a website home page. It responds to POST requests at /predict.
