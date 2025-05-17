import yaml
from scapy.all import sniff
from signature_detector import SignatureDetector
from anomaly_detector import AnomalyDetector
from alert_manager import AlertManager

# Load config
cfg = yaml.safe_load(open("config.yaml"))

sig = SignatureDetector(cfg['rules_file'], cfg['thresholds'])
anom = AnomalyDetector(cfg['model_path'])
alert = AlertManager(cfg['db_path'])


def process_packet(pkt):
    # Signature check
    sig_alert = sig.check(pkt)
    if sig_alert:
        alert.raise_alert('signature', sig_alert, pkt)

    # Feature extraction + anomaly check
    features = anom.extract_features(pkt)
    if anom.is_anomaly(features):
        alert.raise_alert('anomaly', 'Deviation detected', pkt)


if __name__ == "__main__":
    sniff(iface=cfg['interface'], prn=process_packet, store=False)