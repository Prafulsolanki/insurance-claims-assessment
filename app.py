import pdfplumber
import json

# 1. PDF se text nikalna
def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# 2. Fields extract karna
def extract_fields(text):
    fields = {}

    if "POLICY" in text:
        fields["policyNumber"] = "Found"
    else:
        fields["policyNumber"] = None

    if "injury" in text.lower():
        fields["claimType"] = "injury"
    else:
        fields["claimType"] = "vehicle"

    fields["estimatedDamage"] = 18000  # demo value
    fields["description"] = text[:200]

    return fields

# 3. Missing fields check
def check_missing(fields):
    missing = []
    for key, value in fields.items():
        if value is None:
            missing.append(key)
    return missing

# 4. Routing logic
def route_claim(fields, missing):
    if missing:
        return "Manual Review", "Mandatory fields missing"

    if fields["claimType"] == "injury":
        return "Specialist Queue", "Injury related claim"

    if fields["estimatedDamage"] < 25000:
        return "Fast-track", "Damage amount below 25,000"

    return "Standard", "Normal claim"

# 5. Main function
def main():
    text = read_pdf("fnol.pdf")
    fields = extract_fields(text)
    missing = check_missing(fields)
    route, reason = route_claim(fields, missing)

    output = {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    print(json.dumps(output, indent=2))

main()
