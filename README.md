<h1>WellPred Health Prediction Application</h1>

        <h2>Overview</h2>
        <p>WellPred is a web application built with Flask for predicting health conditions including cervical cancer, heart disease, and kidney disease.</p>

        <h2>Directory Structure</h2>
        <pre><code>
WellPred/
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
├── main_app.py               # Main Flask application file
│
└── README.md                 # This README file
        </code></pre>

        <h2>Installation</h2>
        <pre><code>
1. Clone the Repository:
   <code>git clone https://github.com/your-username/WellPred.git</code>
   <code>cd WellPred</code>

2. Setup Python Environment:
   - Make sure Python 3.x is installed on your system.
   - Install dependencies using pip:
     <code>pip install -r requirements.txt</code>
        </code></pre>

        <h2>Usage</h2>
        <pre><code>
1. Run the Application:
   - Navigate to the <code>apps/</code> directory.
   - Start the Flask application:
     <code>python main_app.py</code>
   - Access the application in your web browser at <a href="http://localhost:5000">http://localhost:5000</a>.

2. Using WellPred:
   - Choose from the available prediction modules (cervical cancer, heart disease, kidney disease).
   - Fill out the required information in the input fields.
   - Submit the form to get predictions based on the selected health condition.
        </code></pre>

        <h2>Contributors</h2>
        <ul>
            <li>Sarfaraaz</li>
            <li>Pavan Kumar</li>
            <li>Pavan Sai</li>
            <li>Sumanth</li>
        </ul>

        <h2>License</h2>
        <p>This project is licensed under the MIT License. See the <a href="./LICENSE">LICENSE</a> file for details.</p>
