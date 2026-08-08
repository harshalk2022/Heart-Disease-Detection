# ❤️ Heart Disease Risk Prediction

A machine learning project that predicts the risk of heart disease based on patient health and clinical information.

The trained **K-Nearest Neighbors (KNN)** model is integrated with a simple and user-friendly **Streamlit web application**, allowing users to enter patient information and receive a model-based prediction.

> **Disclaimer:** This project is created for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.

---

## 🚀 Live Demo

🔗 **Streamlit Application:**
**[Open Heart Disease Risk Predictor](https://heart-disease-detection-vs8xuvx32vtaxps6h2rugw.streamlit.app/)**

> Try the live application to enter patient information and get a model-based heart disease risk prediction.

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. Machine learning can be used to analyze medical data and identify patterns associated with heart disease.

In this project, a **K-Nearest Neighbors (KNN)** classification model is trained on a heart disease dataset and then integrated into a Streamlit application.

The application allows the user to enter information such as:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

The entered information is processed using the same preprocessing steps used during model training and passed to the trained KNN model.

---

## 🚀 Features

* Machine learning-based heart disease risk prediction
* K-Nearest Neighbors (KNN) classification
* Input feature preprocessing and scaling
* Saved trained model using Joblib
* Saved scaler for consistent preprocessing
* Saved expected feature columns for correct model input
* Interactive Streamlit web interface
* Simple and user-friendly input form
* Model prediction probability when supported
* Clear prediction result display
* Medical-use disclaimer

---

## 🧠 Machine Learning Workflow

The overall workflow of the project is:

```text
Heart Disease Dataset
        │
        ▼
Data Loading
        │
        ▼
Data Preprocessing
        │
        ▼
Categorical Feature Encoding
        │
        ▼
Feature Selection
        │
        ▼
Train / Test Split
        │
        ▼
Feature Scaling
        │
        ▼
Model Training & Comparison
        │
        ▼
Model Evaluation
        │
        ▼
Save Selected KNN Model + Scaler + Columns
        │
        ▼
Streamlit Application
        │
        ▼
User Input
        │
        ▼
Preprocessing
        │
        ▼
KNN Prediction
        │
        ▼
Risk Prediction
```

---

## 🤖 Model

The project uses the:

**K-Nearest Neighbors (KNN)** classification algorithm.

The trained model is saved using Joblib:

```text
models/KNN_Heart_Model.pkl
```

The application also uses two additional saved artifacts:

```text
models/Heart_Scaler.pkl
models/Heart_Columns.pkl
```

### Why are these files required?

The model expects the input data to be processed in the same way as during training.

Therefore:

* `KNN_Heart_Model.pkl` → trained KNN model
* `Heart_Scaler.pkl` → feature scaling object
* `Heart_Columns.pkl` → expected feature/column order

This ensures that the input provided by the Streamlit application matches the format expected by the trained model.

---

## 📊 Model Comparison

Multiple classification algorithms were evaluated before selecting the model used in the application.

| Model               |   Accuracy |   F1 Score |
| ------------------- | ---------: | ---------: |
| Logistic Regression |     86.96% |     88.57% |
| **KNN**             | **86.41%** | **88.15%** |
| Naive Bayes         |     85.33% |     86.83% |
| Decision Tree       |     78.80% |     80.98% |
| SVM (RBF Kernel)    |     84.78% |     86.79% |

The **KNN model** was selected for the Streamlit application.

> The metrics above are based on the test-set evaluation performed in the project notebook.

---

## 🖥️ Streamlit Application

The Streamlit application is located at:

```text
app/app.py
```

The application provides a structured form divided into:

### 1. Personal Information

* Age
* Sex

### 2. Heart & Blood Measurements

* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Maximum Heart Rate
* Oldpeak

### 3. ECG & Exercise Information

* Chest Pain Type
* Resting ECG
* Exercise-Induced Angina
* ST Slope

After entering the required information, the user can click:

```text
Predict Heart Disease Risk
```

The application then processes the input and displays the model prediction.

---

## 📊 Prediction Flow

When the user clicks the prediction button:

```text
User Input
    ↓
Create Input DataFrame
    ↓
Add Missing Encoded Columns
    ↓
Arrange Columns
    ↓
Scale Features
    ↓
KNN Model
    ↓
Prediction
```

The application displays either:

```text
Higher Risk of Heart Disease
```

or

```text
Lower Risk of Heart Disease
```

The result is a **machine learning prediction**, not a medical diagnosis.

---

## 📁 Project Structure

```text
Heart-Disease-Detection/
│
├── app/
│   └── app.py
│
├── data/
│   └── heart.csv
│
├── models/
│   ├── Heart_Columns.pkl
│   ├── Heart_Scaler.pkl
│   └── KNN_Heart_Model.pkl
│
├── notebooks/
│   └── Heart.ipynb
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Directory Description

| Directory/File     | Description                                |
| ------------------ | ------------------------------------------ |
| `app/`             | Streamlit application                      |
| `data/`            | Dataset used for the project               |
| `models/`          | Saved ML model and preprocessing artifacts |
| `notebooks/`       | Model development and experimentation      |
| `.gitignore`       | Files excluded from Git                    |
| `LICENSE`          | MIT License                                |
| `requirements.txt` | Python dependencies                        |
| `README.md`        | Project documentation                      |

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* K-Nearest Neighbors (KNN)
* Feature Scaling
* Logistic Regression
* Naive Bayes
* Decision Tree
* Support Vector Machine (SVM)

### Data Processing

* Pandas
* NumPy

### Visualization / Analysis

* Matplotlib
* Seaborn

### Model Persistence

* Joblib

### Web Application

* Streamlit

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/harshalk2022/Heart-Disease-Detection.git
```

Navigate into the project:

```bash
cd Heart-Disease-Detection
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment using Git Bash:

```bash
source venv/Scripts/activate
```

For Command Prompt:

```cmd
venv\Scripts\activate
```

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

Make sure the virtual environment is activated.

Then run:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

From the project root directory, run:

```bash
streamlit run app/app.py
```

Streamlit will start the application locally.

You can then open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

# 🧪 Running the Notebook

The machine learning workflow is available in:

```text
notebooks/Heart.ipynb
```

To open the notebook:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

The notebook contains the data analysis, preprocessing, model development, model comparison, and model training workflow.

---

# 📦 Model Files

The repository contains the trained model and preprocessing artifacts:

```text
models/
├── KNN_Heart_Model.pkl
├── Heart_Scaler.pkl
└── Heart_Columns.pkl
```

These files allow the Streamlit application to make predictions without retraining the model every time the application starts.

---

# 🔮 Future Improvements

Possible improvements for this project include:

* Hyperparameter tuning for KNN
* Improve model interpretability
* Add feature importance / feature analysis
* Add prediction history
* Improve application visualizations
* Deploy the Streamlit application
* Add automated testing
* Add CI/CD workflow using GitHub Actions

---

# ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.

The predictions generated by this application should **not** be considered medical advice, diagnosis, or treatment recommendations.

Always consult a qualified healthcare professional for medical evaluation and decisions.

---

# 👨‍💻 Author

**Harshal Khandalkar**

GitHub:
https://github.com/harshalk2022

Project Repository:
https://github.com/harshalk2022/Heart-Disease-Detection

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.
