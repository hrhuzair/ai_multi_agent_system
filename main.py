from fastapi import FastAPI, UploadFile
from classifier_agent import detect_format, detect_intent
from email_agent import extract_email_fields
from json_agent import validate_json
from pdf_agent import extract_pdf_fields
from memory_store import log_trace
from action_router import route_action
import json

app = FastAPI()

@app.post("/process")
async def process_input(file: UploadFile):
    content = await file.read()

    try:
        decoded = content.decode('utf-8')
    except:
        decoded = None

    format = detect_format(content if decoded is None else decoded)
    intent = detect_intent(decoded if decoded else "")

    fields = {}
    action = None

    if format == "Email":
        fields = extract_email_fields(decoded)
        action = route_action(intent, **fields)

    elif format == "JSON":
        try:
            json_data = json.loads(decoded)
            fields = validate_json(json_data)
            action = route_action(intent, anomalies=fields if fields.get("anomaly") else None)
        except Exception as e:
            fields = {"error": "Invalid JSON format", "details": str(e)}
            action = "Alert Sent"

    elif format == "PDF":
        with open("temp.pdf", "wb") as f:
            f.write(content)
        fields = extract_pdf_fields("temp.pdf")
        action = route_action(intent)

    else:
        fields = {"note": "Unrecognized format"}
        action = "Logged"

    log_trace(format, intent, fields, action)

    return {
        "format": format,
        "intent": intent,
        "fields": fields,
        "action": action
    }
