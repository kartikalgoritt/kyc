import google.generativeai as genai
import json
import re
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME, OCR_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

def call_gemini_ocr(file1_obj_front, file1_obj_back, file2_obj_front, file2_obj_back):
    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    response = model.generate_content([OCR_PROMPT, file1_obj_front, file1_obj_back, file2_obj_front, file2_obj_back]) 

    response_dict = response.to_dict()
    raw_text = response_dict["candidates"][0]["content"]["parts"][0]["text"]
    cleaned_text = re.sub(r"```json|```", "", raw_text).strip()
    
    try:
        json_data = json.loads(cleaned_text)
        return json_data
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)