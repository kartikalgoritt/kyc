from urllib.parse import quote_plus
GEMINI_API_KEY = "AIzaSyCkUIoAexHRCHWez6zxA4faUyj48g9n28A"
GEMINI_MODEL_NAME = "gemini-2.0-flash"

username = "kartik61003"
password = quote_plus("algoritt@123")

OCR_PROMPT = """
Analyze the provided image(s) of identity documents. Extract the following information and return the result strictly in the following nested JSON structure:

For Aadhaar card, return the data inside an adhar_details object.
For Driver's License, return the data inside a dl_details object.

- country: The issuing country of the document.
- document_type: The type of document (e.g., National ID, Driver's License, Passport).
- identity_card_no: The main identification number.
- name: The full name of the holder.
- address: address written on the id
- date_of_birth: The date of birth in YYYY-MM-DD format. strictly numbers.
- sex: The sex or gender (use "M" or "F").
- True_Documents: "Yes" or "No" whether the document uploaded by the user seems legit or not, if front and back doest match return "No".

Ensure the output is a valid JSON object with exactly two nested objects: adhar_details and dl_details. Return nothing else except this JSON.

Example Output Structure:
{
  "adhar_details": {
    "country": "",
    "document_type": "",
    "identity_card_no": "",
    "name": "",
    "address": "",
    "date_of_birth": "",
    "sex": "",
    "True_Documents": "No"
  },
  "dl_details": {
    "country": "",
    "document_type": "",
    "identity_card_no": "",
    "name": "",
    "address": "",
    "date_of_birth": "",
    "True_Documents": "No"
  }
}
"""

COMPARE_PROMPT = """
You are given two JSON documents representing identity information. Compare them field by field based on the rules below:

Rules for comparison:
- "country": must match exactly (case-sensitive)
- "name": must be an exact match ignoring case, order of first/last name, and suffixes like Jr., Sr., III, etc.
- "address": perform semantic matching, ignoring case and order of words
- "date_of_birth": must match exactly, ignoring format differences (e.g., "1990-01-01" = "01/01/1990")
- "sex": must match exactly

Your task is to output a **single JSON object only** (no explanation) with:
1. "info_match_score": an integer from 1 to 10 representing how well the documents match.
2. "customer_valid": "true" if all fields match according to the rules above, else "false".

Only return the valid JSON object, nothing else.
"""


CONFIDENT_AI = "wHbl4e+45rjS7QdUSiSnWmVYrSz6Pqo317TlhACTExU="