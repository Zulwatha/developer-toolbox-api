from datetime import datetime

def current_unix_timestamp() -> int:
    # Returns current Unix timestamp (seconds since epoch)
    return int(datetime.utcnow().timestamp())

def convert_unix_to_datetime(timestamp: int) -> str:
    # Converts Unix timestamp to human-readable UTC time
    try:
        dt = datetime.utcfromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    except (ValueError, OSError):
        raise ValueError("Invalid timestamp value.")
