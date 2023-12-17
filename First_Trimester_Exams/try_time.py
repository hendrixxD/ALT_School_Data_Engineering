from datetime import datetime, timezone

def get_timestamp():
    return datetime.utcnow().astimezone()


timestamp = get_timestamp()
print(timestamp)
