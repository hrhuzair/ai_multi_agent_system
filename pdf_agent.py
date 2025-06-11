from pdfminer.high_level import extract_text
import re

def extract_pdf_fields(file_path):
    text = extract_text(file_path)
    flags = {}

    if "invoice" in text.lower():
        if "total" in text.lower():
            match = re.search(r'Total\s*[:\-]?\s*(\d+)', text)
            if match and int(match.group(1)) > 10000:
                flags["invoice_flag"] = "High Value Invoice"

    if any(term in text for term in ["GDPR", "FDA"]):
        flags["compliance_flag"] = "Regulatory Keyword Found"

    return flags
