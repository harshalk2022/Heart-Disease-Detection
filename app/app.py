import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Section headings */
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }

    .section-description {
        color: #666666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    /* Result cards */
    .result-card {
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 1rem;
        border: 1px solid #dddddd;
    }

    .result-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .result-description {
        font-size: 1rem;
        color: #555555;
    }

    /* Disclaimer */
    .disclaimer {
        background-color: #f7f7f7;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #888888;
        font-size: 0.85rem;
        color: #555555;
        margin-top: 2rem;
    }

    /* Prediction button */
    div.stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.05rem;
        font-weight: 600;
        border-radius: 8px;
    }

    /* Small info text */
    .info-text {
        font-size: 0.85rem;
        color: #777777;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOAD MODEL
# ============================================================


@st.cache_resource
def load_model_files():
    model = joblib.load("models/KNN_Heart_Model.pkl")
    scaler = joblib.load("models/Heart_Scaler.pkl")
    expected_columns = joblib.load("models/Heart_Columns.pkl")

    return model, scaler, expected_columns


model, scaler, expected_columns = load_model_files()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">Heart Disease Risk Predictor</div>', unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Enter the required health information below to get a model-based
        heart disease risk prediction.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INFORMATION BOX
# ============================================================

st.info(
    "Please enter the information as accurately as possible. "
    "Fields marked with an explanation contain measurements commonly "
    "used by the prediction model."
)


# ============================================================
# INPUT FORM
# ============================================================

with st.form("heart_prediction_form"):

    # --------------------------------------------------------
    # SECTION 1: PERSONAL INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">1. Personal Information</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        "Basic information about the person."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider(
            "Age",
            min_value=18,
            max_value=100,
            value=40,
            help="Age of the person in years.",
        )

    with col2:
        sex = st.selectbox(
            "Sex",
            ["M", "F"],
            format_func=lambda x: "Male" if x == "M" else "Female",
            help="Biological sex used by the prediction model.",
        )

    st.divider()

    # --------------------------------------------------------
    # SECTION 2: HEART MEASUREMENTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">2. Heart & Blood Measurements</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        "Enter the measurements obtained from the patient or medical report."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        resting_bp = st.number_input(
            "Resting Blood Pressure",
            min_value=80,
            max_value=200,
            value=120,
            step=1,
            help="Resting blood pressure in mm Hg.",
        )

        cholesterol = st.number_input(
            "Cholesterol",
            min_value=100,
            max_value=600,
            value=200,
            step=1,
            help="Serum cholesterol level in mg/dL.",
        )

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            [0, 1],
            format_func=lambda x: "No (0)" if x == 0 else "Yes (1)",
            help="Whether fasting blood sugar is greater than 120 mg/dL.",
        )

    with col2:

        max_hr = st.slider(
            "Maximum Heart Rate",
            min_value=60,
            max_value=220,
            value=150,
            help="Maximum heart rate achieved during exercise/testing.",
        )

        oldpeak = st.slider(
            "Oldpeak (ST Depression)",
            min_value=0.0,
            max_value=6.0,
            value=1.0,
            step=0.1,
            help="ST depression measured during exercise relative to rest.",
        )

    st.divider()

    # --------------------------------------------------------
    # SECTION 3: ECG & EXERCISE INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">3. ECG & Exercise Information</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        "Select the values from the available medical/test report."
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"],
            format_func=lambda x: {
                "ATA": "ATA - Atypical Angina",
                "NAP": "NAP - Non-Anginal Pain",
                "TA": "TA - Typical Angina",
                "ASY": "ASY - Asymptomatic",
            }[x],
            help="Type of chest pain recorded during examination.",
        )

        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"],
            format_func=lambda x: {
                "Normal": "Normal",
                "ST": "ST-T Wave Abnormality",
                "LVH": "Left Ventricular Hypertrophy",
            }[x],
            help="Result of the resting electrocardiogram.",
        )

    with col2:

        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            ["Y", "N"],
            format_func=lambda x: "Yes" if x == "Y" else "No",
            help="Whether exercise causes angina/chest discomfort.",
        )

        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"],
            format_func=lambda x: {"Up": "Up", "Flat": "Flat", "Down": "Down"}[x],
            help="Slope of the peak exercise ST segment.",
        )

    st.divider()

    # --------------------------------------------------------
    # PREDICT BUTTON
    # --------------------------------------------------------

    predict_button = st.form_submit_button("Predict Heart Disease Risk")


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # CREATE RAW INPUT
    # --------------------------------------------------------

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingECG_" + resting_ecg: 1,
        "ExerciseAngina_" + exercise_angina: 1,
        "ST_Slope_" + st_slope: 1,
    }

    # --------------------------------------------------------
    # CREATE DATAFRAME
    # --------------------------------------------------------

    input_df = pd.DataFrame([raw_input])

    # --------------------------------------------------------
    # ADD MISSING COLUMNS
    # --------------------------------------------------------

    for col in expected_columns:

        if col not in input_df.columns:
            input_df[col] = 0

    # --------------------------------------------------------
    # REORDER COLUMNS
    # --------------------------------------------------------

    input_df = input_df[expected_columns]

    # --------------------------------------------------------
    # SCALE INPUT
    # --------------------------------------------------------

    with st.spinner("Analyzing the entered information..."):

        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        # ----------------------------------------------------
        # PREDICTION PROBABILITY
        # ----------------------------------------------------

        probability = None

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(scaled_input)

            probability = probabilities[0][1] * 100

    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">Prediction Result</div>', unsafe_allow_html=True
    )

    if prediction == 1:

        st.error("High Risk of Heart Disease")

        if probability is not None:

            st.metric("Model Risk Probability", f"{probability:.1f}%")

        st.warning(
            "The model predicts a higher risk based on the entered "
            "information. This result is not a medical diagnosis."
        )

    else:

        st.success("Low Risk of Heart Disease")

        if probability is not None:

            st.metric("Model Risk Probability", f"{probability:.1f}%")

        st.info(
            "The model predicts a lower risk based on the entered "
            "information. This result is not a medical diagnosis."
        )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        <strong>Important:</strong> This application is a machine learning
        demonstration and should not be used as a substitute for professional
        medical advice, diagnosis, or treatment. The prediction is based only
        on the information provided to the model.
    </div>
    """,
    unsafe_allow_html=True,
)
