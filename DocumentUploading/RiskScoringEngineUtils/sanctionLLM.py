import google.generativeai as genai
from RiskScoringEngineUtils.ResponseToList import extract_list_from_llm_response
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME, Sanction_PROMT

genai.configure(api_key=GEMINI_API_KEY)

def sanctionedCountryList(list):
    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    comma_separated_string = ','.join(list)
    response_from_LLM = model.generate_content([Sanction_PROMT, comma_separated_string])
    
    #extracted_list = extract_list_from_llm_response(response_from_LLM)
    return response_from_LLM.candidates[0].content.parts[0].text
    
    