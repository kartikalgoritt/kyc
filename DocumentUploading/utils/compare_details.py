import google.generativeai as genai
import json
import re
from config import GEMINI_API_KEY, COMPARE_PROMPT, GEMINI_MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

def compare_details_utils(json_data1, json_data2):
    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    json_data1_str = json.dumps(json_data1)
    json_data2_str = json.dumps(json_data2)
    response = model.generate_content([COMPARE_PROMPT, json_data1_str, json_data2_str])
    response_dict = response.to_dict()
    raw_text = response_dict["candidates"][0]["content"]["parts"][0]["text"]
    cleaned_text = re.sub(r"```json|```", "", raw_text).strip()
    try:
        json_data = json.loads(cleaned_text)
        return json_data
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        return None


