import json
import re

def extract_list_from_llm_response(response):
    try:
        # Step 1: Get the actual text content inside the protos response
        raw_text = response.candidates[0].content.parts[0].text

        # Step 2: Remove ```python and ``` safely
        code_block_pattern = r"```(?:python)?\n?(.*?)```"
        match = re.search(code_block_pattern, raw_text, re.DOTALL)

        if not match:
            raise ValueError("No code block found in LLM response.")

        code_content = match.group(1).strip()

        # Step 3: Clean up common LLM artifacts if needed
        # Example: Normalize newlines, remove unnecessary spaces
        code_content = code_content.replace('\r\n', '\n').strip()

        # Step 4: Parse the cleaned list
        # Since it's a list of strings, JSON parsing is much safer
        code_content = code_content.replace("'", '"')  # In case LLM used single quotes
        parsed_list = json.loads(code_content)

        # Step 5: Validate
        if not isinstance(parsed_list, list):
            raise ValueError("Parsed content is not a list.")

        return parsed_list

    except Exception as e:
        raise RuntimeError(f"Failed to extract list from LLM response: {e}")