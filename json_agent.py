def validate_json(data):
    required_fields = ["id", "type", "payload"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return {"anomaly": True, "missing_fields": missing}
    return {"anomaly": False}
