import json

def detect_format(content):
    if isinstance(content, dict):
        return "JSON"
    if isinstance(content, bytes) and content.strip().startswith(b"%PDF"):
        return "PDF"
    if isinstance(content, str) and ("From:" in content or "Subject:" in content):
        return "Email"
    try:
        content_str = content.decode('utf-8') if isinstance(content, bytes) else content
        json.loads(content_str)
        return "JSON"
    except:
        pass
    return "Unknown"

def detect_intent(text):
    keywords = {
        "Invoice": ["invoice", "payment due", "bill"],
        "Complaint": ["not working", "complaint", "angry", "issue", "problem", "unsatisfied"],
        "RFQ": ["request for quote", "quotation", "rfq"],
        "Fraud Risk": ["unauthorized", "fraud", "suspicious", "scam"],
        "Regulation": ["GDPR", "FDA", "compliance", "regulatory"],
        "Meeting Reminder": ["meeting", "schedule", "calendar", "appointment"],
        "Follow-up": ["follow up", "checking in", "just checking", "gentle reminder"],
        "Feedback": ["feedback", "suggestion", "review"],
        "Query": ["question", "doubt", "inquiry", "query"]
    }
    try:
        lower_text = text.lower()
    except:
        return "Unknown"
    for intent, cues in keywords.items():
        if any(cue in lower_text for cue in cues):
            return intent
    return "Unknown"
