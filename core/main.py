# Main loop with multi-pair scanning + signal broadcastimport requests
import datetime

def send_signal_to_backend(symbol, direction, confidence):
    url = "https://msio-backend.onrender.com/signals/push"
    payload = {
        "symbol": symbol,
        "direction": direction,
        "confidence": confidence,
        "source": "msio_bot"
    }
    try:
        res = requests.post(url, json=payload)
        print("Signal sent:", res.status_code, res.json())
    except Exception as e:
        print("Failed to send signal:", e)
