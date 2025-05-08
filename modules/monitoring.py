import psutil
import time

def get_system_status():
    """
    Возвращает информацию о состоянии системы (CPU, RAM).
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent
    }

def monitor_openwebui():
    """
    Проверяет доступность OpenWebUI API.
    """
    start_time = time.time()
    try:
        response = requests.get("http://localhost:3000/health")
        latency = time.time() - start_time
        return {
            "status": "Online" if response.status_code == 200 else "Offline",
            "latency": latency
        }
    except:
        return {
            "status": "Offline",
            "latency": None
        }
