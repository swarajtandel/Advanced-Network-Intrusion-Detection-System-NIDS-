# Entry point: runs packet_capture.py and prometheus_exporter.py
import threading
import packet_capture
import prometheus_exporter

if __name__ == '__main__':
    t1 = threading.Thread(target=prometheus_exporter.main)
    t1.daemon = True
    t1.start()

    packet_capture.main()