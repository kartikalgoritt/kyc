def validate_form_data(uploaded_file, fields):
    errors = []
    if uploaded_file is None:
        errors.append("⛔ Document photo upload is required.")
    
    for label, value in fields.items():
        if not value or not str(value).strip():
            errors.append(f"⛔ {label} is required.")
    
    return errors
