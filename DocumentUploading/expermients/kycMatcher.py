import streamlit as st
import datetime
import time # To simulate processing delay

st.set_page_config(layout="wide") # Use wider layout for better form display

st.title("Identity Document Verification")



# --- Form Creation ---
with st.form(key="verification_form"):
    st.header("1. Upload Document Photo")
    st.info("Please upload a clear photo of the identity document.")
    uploaded_file = st.file_uploader(
    "Choose document image *",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
    label_visibility="collapsed",
    )


    st.divider() # Visual separator

    st.header("2. Enter Details Manually")
    st.caption("Enter the details *exactly* as they appear on the document. All fields are required.")

    # Use columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name *", placeholder="e.g., LIM KOK WING")
        id_no = st.text_input("Identity Card No. *", placeholder="e.g., S1234567D")
        # Use selectbox for Sex to force a selection
        sex_options = ["--Select--", "M", "F", "Other"]
        sex = st.selectbox("Sex *", options=sex_options, index=0) # Default to placeholder
        country = st.text_input("Country (as on document) *", placeholder="e.g., SINGAPORE")
        required_text_fields = True


    with col2:
        # Date input - default to a reasonable past date or force selection UX
        # Using today's date requires users to actively change it. Add help text.
        dob = st.date_input(
            "Date of Birth *",
            value=None, # Allow None initially
            min_value=datetime.date(1900, 1, 1),
            max_value=datetime.date.today(),
            help="Please select the date of birth from the document."
        )
        race = st.text_input("Race *", placeholder="e.g., CHINESE")
        doc_type = st.text_input("Document Type *", placeholder="e.g., IDENTITY CARD")
        country_of_birth = st.text_input("Country of Birth *", placeholder="e.g., SINGAPORE")


    st.divider()

    # --- Submit Button ---
    submitted = st.form_submit_button("Submit for Verification", use_container_width=True)

# --- Post-Submission Logic ---
if submitted:
    # --- Input Validation ---
    error_messages = ["Error"]

    # Check file upload
    if uploaded_file is None:
        error_messages.append("⛔ Document photo upload is required.")

    # Check text fields
    required_text_fields = {
        "Full Name": name,
        "Identity Card No.": id_no,
        "Race": race,
        "Document Type": doc_type,
        "Country (as on document)": country,
        "Country of Birth": country_of_birth
    }
    for label, value in required_text_fields.items():
        if not value or not value.strip():
            error_messages.append(f"⛔ {label} is required.") 
