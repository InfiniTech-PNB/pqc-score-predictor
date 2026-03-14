from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import os
from typing import Dict, Any

app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "pqc-scoremodel.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Hardcoded Label Mappings
MAPPING = {
    "tls_version": {
        "SSLv3": 0, "TLSv1.0": 1, "TLSv1.1": 2, "TLSv1.2": 3, "TLSv1.3": 4
    },
    "cipher": {
        "TLS_AES_128_GCM_SHA256": 0, "TLS_AES_256_GCM_SHA384": 1,
        "TLS_CHACHA20_POLY1305_SHA256": 2, "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384": 3,
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256": 4, "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384": 5,
        "TLS_KYBER768_AES256_GCM_SHA384": 6, "TLS_RSA_WITH_3DES_EDE_CBC_SHA": 7,
        "TLS_RSA_WITH_AES_256_CBC_SHA": 8, "TLS_X25519_KYBER768_AES256_GCM_SHA384": 9
    },
    "key_exchange": {
        "ECDHE": 0, "KYBER768": 1, "RSA": 2, "X25519": 3
    },
    "signature_algorithm": {
        "DILITHIUM3": 0, "ECDSA": 1, "Ed25519": 2, "RSA": 3
    },
    "pqc_key_exchange": {
        "KYBER768": 0, "nan": 1
    },
    "pqc_signature": {
        "DILITHIUM3": 0, "nan": 1
    }
}

cat_cols = [
    "tls_version",
    "cipher",
    "key_exchange",
    "signature_algorithm",
    "pqc_key_exchange",
    "pqc_signature",
]

bool_cols = [
    "hybrid_pqc",
    "pfs_supported",
    "rsa_used",
]

FEATURE_ORDER = [
    "tls_version",
    "cipher",
    "key_exchange",
    "signature_algorithm",
    "pqc_key_exchange",
    "pqc_signature",
    "hybrid_pqc",
    "supported_tls_versions_count",
    "cipher_suites_count",
    "weak_cipher_count",
    "key_size",
    "pfs_supported",
    "rsa_used"
]


class FeatureRequest(BaseModel):
    features: Dict[str, Any]


@app.post("/pqc-score")
def pqc_score(req: FeatureRequest):

    row = {}
    for f in FEATURE_ORDER:
        val = req.features.get(f)
        if f in bool_cols:
            row[f] = int(bool(val))
        elif f in cat_cols:
            if pd.isna(val) or val is None or val == "":
                val_str = "nan"
            else:
                val_str = str(val)
            
            if f in MAPPING and val_str in MAPPING[f]:
                row[f] = MAPPING[f][val_str]
            else:
                row[f] = 0
        else:
            row[f] = val if val is not None else 0

    df = pd.DataFrame([row])

    score = model.predict(df)

    print("Prediction:", score)

    return {
        "scores": score.tolist()
    }