from prometheus_client import start_http_server
import config

if __name__ == '__main__':
    start_http_server(config.prometheus_port)
    print(f"Prometheus metrics on :{config.prometheus_port}/metrics")
    while True:
        pass  # metrics updated by AlertManager