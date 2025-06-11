from utils import retry

def extract_email_fields(text):
    fields = {}
    if "urgent" in text.lower():
        fields["urgency"] = "high"
    if "angry" in text.lower():
        fields["tone"] = "angry"
    if "please" in text.lower():
        fields["tone"] = "polite"
    if "threat" in text.lower():
        fields["tone"] = "threatening"
    return fields

@retry(max_attempts=3, delay=2)
def your_agent_function(intent, **kwargs):
    print(f"Processing intent: {intent} with args: {kwargs}")
    import random
    if random.choice([True, False]):
        print("Yay, success!")
        return "Success"
    else:
        raise Exception("Oops, fail!")
