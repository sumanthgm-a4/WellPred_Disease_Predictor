# WellPred Disease Predictor

WellPred is a web application built with Flask for predicting health conditions including cervical cancer, heart disease, and kidney disease.

![Screenshot from 2024-07-29 23-12-45](https://github.com/user-attachments/assets/79a5776d-cdee-49e7-8f15-f9807e7a7bd0)
![Screenshot from 2024-07-29 23-13-06](https://github.com/user-attachments/assets/837ca332-68bb-4883-90b6-5d7ce983954f)
![Screenshot from 2024-07-29 23-13-24](https://github.com/user-attachments/assets/55f28677-5420-4963-8ca1-fd923b9f7295)

## Models Used

### 1. Cervical Cancer Prediction:
- Model: XGBoost
- File: cerv_canc_models.pkl
- Description: XGBoost model trained on preprocessed cervical cancer dataset.

### 2. Heart Disease Prediction:
- Model: Random Forest
- File: heart_model.pkl
- Description: Random Forest model trained on preprocessed heart disease dataset.

### 3. Kidney Disease Prediction:
-  Model: Logistic Regression
- File: kidney_models.pkl
- Description: Logistic Regression model trained on preprocessed kidney disease dataset.

## Directory Structure

Following is the project's directory structure:

```bash
WellPred_Disease_Predictor
│
├── apps/
│   ├── cerv_app.py           # Flask application for cervical cancer prediction
│   ├── heart_app.py          # Flask application for heart disease prediction
│   └── kidney_app.py         # Flask application for kidney disease prediction
│
├── codes/
│   ├── Cervical_Cancer.ipynb # Jupyter Notebook for cervical cancer data analysis
│   ├── Heart.ipynb           # Jupyter Notebook for heart disease data analysis
│   └── Kidney.ipynb          # Jupyter Notebook for kidney disease data analysis
│
├── datasets/
│   ├── Cervical_Cancer.csv           # Raw dataset for cervical cancer
│   ├── Prepro_Cervical_Cancer.csv    # Preprocessed dataset for cervical cancer
│   ├── Prepro_Heart.csv              # Preprocessed dataset for heart disease
│   └── Prepro_Kidney.csv             # Preprocessed dataset for kidney disease
│
├── models/
│   ├── cerv_canc_models.pkl  # Pickled models for cervical cancer prediction
│   ├── heart_model.pkl       # Pickled model for heart disease prediction
│   └── kidney_models.pkl     # Pickled models for kidney disease prediction
│
├── templates/
│   ├── base.html             # Base HTML template for Flask application
│   ├── cerv_main.html        # Main template for cervical cancer prediction
│   ├── cerv_res.html         # Result template for cervical cancer prediction
│   ├── heart_main.html       # Main template for heart disease prediction
│   ├── heart_res.html        # Result template for heart disease prediction
│   ├── index.html            # Index page template
│   ├── kidney_main.html      # Main template for kidney disease prediction
│   └── kidney_res.html       # Result template for kidney disease prediction
│
├── __pycache__/              # Python bytecode cache (automatically generated)
│
├── app.py               # Main Flask application file
│
└── README.md                 # This README file

```


## Installation

### 1. Clone the Repository:

```bash
  git clone https://github.com/sumanthgm-a4/WellPred.git
  cd WellPred
```

### 2. Setup the Python Environment:

- Make sure python3.10 or above is installed on your system.
- Install dependencies using 'pip':
```bash
  pip install -r requirements.txt
```

## Usage

### 1. Run the Application:
- Start the Flask app:
```bash
  python app.py
```
- Access the application in your web browser at http://localhost:5000 .

### 2. Using WellPred:
- Choose from the available prediction modules (cervical cancer, heart disease, kidney disease).
- Fill out the required information in the input fields.
- Submit the form to get predictions based on the selected health condition.
## Authors

- [S. Sarfaraaz](https://www.github.com/sarfaraaz97)
- [A. Pavan Kumar](https://www.github.com/pavan07071)
- [C. Pavan Sai](https://www.github.com/)
- [G. M. Sumanth](https://www.github.com/sumanthgm-a4)


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/sumanthgm-a4/WellPred_Disease_Predictor/blob/main/LICENSE) file for details.

## DISCLAIMER 
### The predictions made by these models are accurate, though relying on them ENTIRELY is not advised.
