# KavachAI PQC Score Predictor

Machine Learning based Post-Quantum Cryptography (PQC) readiness scoring engine that evaluates the cryptographic strength of assets using TLS configuration parameters.

---

## 🚀 Features

- ML-Based PQC Risk Scoring: Predicts quantum readiness score using trained model
- Cryptographic Feature Analysis: Uses TLS version, cipher suites, key exchange, key size, and security flags
- Environment-Agnostic Model: Works independently or as part of scanning pipeline
- Fast Inference: Lightweight model for real-time scoring
- Integration Ready: Designed to be used with backend APIs (FastAPI / Express)

---

## 📊 Input Features

The model uses the following features to predict PQC readiness score:

### Categorical Features
- tls_version  
- cipher  
- key_exchange  
- signature_algorithm  
- pqc_key_exchange  
- pqc_signature  

### Numerical Features
- supported_tls_versions_count  
- cipher_suites_count  
- weak_cipher_count  
- key_size  

### Boolean Features
- hybrid_pqc  
- pfs_supported  
- rsa_used  

---

## 🎯 Output

- pqc_ready_score (0 – 100)
  - 80–100 → Quantum Safe  
  - 50–79 → Partially Safe  
  - <50 → Vulnerable  

---

## 🧠 Model Details

- Model Type: Regression Model (Scikit-learn)
- Training Data: Synthetic dataset generated based on real-world TLS configurations and NIST PQC guidelines
- Feature Encoding: Label Encoding for categorical features
- Evaluation Metrics: RMSE, R² Score

---

## 📂 Project Structure
pqc-score-predictor/
├── main.py # API logic
├── pqc_tls.ipynb # Training notebook
├── pqc_tls_dataset.csv # Synthetic dataset
├── pqc-scoremodel.pkl # Trained ML model
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Setup & Installation

### Prerequisites
- Python >= 3.10

### Setup

```bash
git clone <your-repo-url>
cd pqc-score-predictor

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

🏃 Running the Model
Run Prediction Script
python main.py

🔗 Integration

This model is used as part of the KavachAI pipeline:

TLS Scanner extracts cryptographic parameters
Features are passed to ML model
Model predicts PQC readiness score
Score is combined with environment-based scoring
Final risk classification is generated

⚠️ Note on Dataset
The dataset is synthetic due to unavailability of real-world labeled cryptographic datasets
Generated using TLS configurations, cryptographic standards, and PQC guidelines
Model is used alongside rule-based checks and environment scoring for reliable results
👤 Team Information

Team: InfiniTech
