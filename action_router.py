import httpx

def route_action(intent, tone=None, urgency=None, anomalies=None):
    if intent == "Complaint" and tone == "angry" and urgency == "high":
        httpx.post("http://localhost:8000/crm/escalate", json={"issue": "urgent complaint"})
        return "CRM Escalated"
    elif anomalies:
        httpx.post("http://localhost:8000/alert", json=anomalies)
        return "Alert Sent"
    else:
        return "Logged"
