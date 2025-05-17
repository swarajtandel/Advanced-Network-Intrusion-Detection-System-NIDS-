import torch
import numpy as np
from sklearn.preprocessing import StandardScaler

class AnomalyDetector:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
        self.model.eval()
        self.scaler = StandardScaler()
        # Pre-fit scaler on training data or load parameters

    def extract_features(self, pkt):
        # Example: packet length, flags, IP TTL
        length = len(pkt)
        ttl = pkt[TTL] if pkt.haslayer(TTL) else 0
        return np.array([length, ttl]).reshape(1, -1)

    def is_anomaly(self, features):
        ft = self.scaler.transform(features)
        with torch.no_grad():
            output = self.model(torch.tensor(ft, dtype=torch.float))
        loss = torch.nn.functional.mse_loss(output, torch.tensor(ft, dtype=torch.float))
        return loss.item() > 0.01  # anomaly threshold