# KavachAI PQC Prediction ML Service

> **Machine Learning Service for Post-Quantum Cryptography Scoring**
> Built for PNB Hackathon 2026 by **InfiniTech**

This microservice provides an AI-driven scoring mechanism to evaluate the Post-Quantum Cryptography (PQC) readiness of network assets. It takes extracted cryptographic features from TLS scans and predicts a quantum-safety score using a pre-trained machine learning model.

---

## 📌 Table of Contents

- [Features](#-features)
- [Architecture & Flow](#-architecture--flow)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Local Setup (First Time)](#-local-setup-first-time)
- [Running the Server](#-running-the-server)
- [API Endpoints](#-api-endpoints)
- [Team](#-team)

---

## 🚀 Features

| Feature | Description |
|---|---|
| **Predictive Scoring** | Evaluates a target's TLS configuration to output a PQC readiness score. |
| **Pre-trained Model** | Utilizes a scikit-learn model (`pqc-scoremodel.pkl`) trained on cryptographic datasets. |
| **Categorical Mapping** | Automatically encodes raw strings (like TLS versions, cipher suites, signature algorithms) into ML-ready numerical features. |
| **High Performance** | Built on FastAPI and Uvicorn for incredibly fast, stateless inference. |
| **Model Training Notebook** | Includes the Jupyter Notebook (`pqc-tls.ipynb`) and dataset (`pqc_tls_dataset.csv`) used to train the model. |

---

## 🔄 Architecture & Flow

### Execution Flow / How it Works

1. **Feature Extraction**: The main backend extracts cryptographic properties (TLS version, ciphers, key size, hybrid support) from a raw scan result.
2. **Inference Request**: The backend sends a POST request to this ML service containing the raw features.
3. **Data Preprocessing**: The FastAPI service maps categorical string variables (e.g., `TLS_AES_256_GCM_SHA384`, `KYBER768`) to their corresponding integer values required by the model.
4. **Prediction**: The mapped feature vector is fed into the loaded `scikit-learn` `.pkl` model.
5. **Response**: The predicted PQC readiness score is returned as a JSON response back to the main backend.

---

## 🛠️ Tech Stack

### Backend & Machine Learning
| Technology | Purpose |
|---|---|
| **Python 3** | Core language |
| **FastAPI** | High-performance async web framework |
| **scikit-learn** | Machine learning library used for the predictive model |
| **pandas** & **numpy** | Data manipulation and numerical feature formatting |
| **Uvicorn** | ASGI server to run the FastAPI application |
| **Jupyter** | Notebook environment for model training and analysis |

---

## 📂 Project Structure

```text
pqc-prediction-ml/
│
├── main.py                 # FastAPI Server entry point & prediction logic
├── pqc-scoremodel.pkl      # Pre-trained scikit-learn model binary
├── pqc-tls.ipynb           # Jupyter notebook used for data exploration & training
├── pqc_tls_dataset.csv     # Training dataset containing TLS cryptographic records
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Local Setup (First Time)

### Prerequisites
- Python 3.8+ 

### Setup

1. **Clone & Navigate**
   ```bash
   git clone <repository-url>
   cd pqc-prediction-ml
   ```

2. **Create and activate a Python Virtual Environment**
   ```bash
   python3 -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

*(Note: There are no `.env` files required for this ML microservice.)*

---

## 🏃 Running the Server

### Start the FastAPI Service
```bash
uvicorn main:app --reload --port 8001
```

- The inference server runs at `http://localhost:8001`
- Interactive Swagger API docs are automatically generated at `http://localhost:8001/docs`

---

## 📊 API Endpoints

### ML Inference
- `POST /pqc-score`: Accepts a JSON payload of cryptographic features (like TLS version, cipher suite, key exchange type) and returns a machine-learning predicted PQC readiness score.

---

## 👤 Team

- **Author:** InfiniTech
- **Event:** PNB Hackathon 2026