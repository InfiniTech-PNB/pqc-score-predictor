# 🧠 KavachAI ML-Engine – PQC Risk Prediction Model

This service provides a specialized machine learning engine designed to predict **Post-Quantum Cryptography (PQC) Readiness** and risk scores. By analyzing TLS configurations and cryptographic parameters, the model evaluates how vulnerable an asset is to future quantum computing threats.

It integrates seamlessly with the KavachAI ecosystem to provide deterministic risk scoring used in CBOM generation and security auditing.

---

## 🚀 Features

- **ML-Based Risk Scoring**: Predictive analysis of cryptographic configurations using a trained Random Forest model.
- **TLS Attribute Mapping**: Comprehensive internal mapping for TLS versions, ciphers, and key exchange algorithms.
- **Hybrid PQC Evaluation**: Specific logic to detect and weight hybrid post-quantum cryptographic support.
- **Feature Engineering**: Automated transformation of raw TLS scan data into model-optimized feature vectors.
- **High-Performance Inference**: FastAPI-powered endpoint optimized for rapid batch processing and real-time scoring.

---

## 🔄 Execution Flow / How it Works

1. **Feature Intake**: Receives cryptographic metadata (TLS version, cipher suites, key exchange, etc.) via a JSON request.
2. **Preprocessing**: Converts categorical strings (e.g., `TLS_AES_128_GCM_SHA256`) and boolean flags into numerical values based on curated `MAPPING` dictionaries.
3. **Model Inference**: Feeds the feature vector into the pre-trained `pqc-scoremodel.pkl` engine.
4. **Scoring & Normalization**: Produces a raw prediction score which is then used by the backend to calculate the final "Quantum Readiness Grade".

---

## 🛠️ Technology Stack

### Machine Learning
- **Language**: Python 3.12+
- **ML Framework**: Scikit-Learn
- **Data Handling**: Pandas, NumPy
- **Model Storage**: Pickle

### API & Server
- **Web Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Validation**: Pydantic

---

## 📂 Project Structure

```text
pqc-prediction-ml/
├── main.py                 # FastAPI Inference Server & Feature Mapper
├── pqc-scoremodel.pkl      # Trained ML Model (Random Forest / Gradient Boosted)
├── pqc-tls.ipynb          # Jupyter Notebook for Model Training, EDA & Validation
├── pqc_tls_dataset.csv     # Synthetic and Real-world dataset used for training
├── requirements.txt        # Python dependencies
└── venv/                   # Local Virtual Environment
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.12 or higher
- `pip` (Python package manager)

### Setup
1. **Navigate to the ML folder**:
   ```bash
   cd pqc-prediction-ml
   ```

2. **Create and activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Running the Application

### Start the Prediction Service
```bash
uvicorn main:app --reload --port 9000
```
- The server will start at `http://localhost:9000`
- Interactive API documentation (Swagger) is available at `http://localhost:9000/docs`

---

## 📊 API Endpoints

### PQC Scoring
- `POST /pqc-score`: 
  - **Description**: Accepts a dictionary of TLS features and returns a predicted readiness score.
  - **Payload**: `{"features": { "tls_version": "TLSv1.3", "cipher": "...", "hybrid_pqc": true, ... }}`
  - **Response**: `{"scores": [0.892]}`

---

## 👤 Team Information
- **Author**: InfiniTech 🚀
