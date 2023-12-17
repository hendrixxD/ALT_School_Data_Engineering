from datetime import datetime, timezone

def _timestamp():
    """returns the timestamp when called

    Returns:
        timestamp: returns as a timezone-aware timestamp
    """
    return datetime.utcnow().astimezone()

print(_timestamp())
