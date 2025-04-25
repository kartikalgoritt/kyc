def compare_details(manual, ocr):
    result = {}
    for key in manual:
        m_val = manual.__getitem__(key).strip().lower()
        o_val = ocr.__getitem__(key).strip().lower()
        result[key] = {
            "manual": m_val,
            "ocr": o_val,
            "match": m_val == o_val
        }
    return result
