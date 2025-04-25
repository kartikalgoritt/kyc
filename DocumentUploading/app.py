import streamlit as st
import datetime
from utils.gemini_ocr import call_gemini_ocr
from utils.comparator import compare_details
from utils.form_validation import validate_form_data
from utils.compare_details import compare_details_utils
from PIL import Image
import io
from pymongo import MongoClient
from config import password, username


st.set_page_config(layout="wide")
st.title("🛂 Identity Document Verification")
uri = f"mongodb+srv://{username}:{password}@cluster0.e9tile1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

with st.form(key="verification_form"):

    st.header("1.1) Upload Front Aadhar Photo")
    front_aadhar_file = st.file_uploader(
        "Choose document image *",
        key="front_aadhar",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )

    st.header("1.2) Upload Back Aadhar Photo")
    back_aadhar_file = st.file_uploader(
        "Choose document image *",
        key="back_aadhar",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )

    st.divider()

    st.header("2.1) Upload DL Front Photo")
    dl_front_file = st.file_uploader(
        "Choose DL Front *",
        key="dl_front",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )

    st.header("2.2) Upload DL Back Photo")
    dl_back_file = st.file_uploader(
        "Choose DL Back *",
        key="dl_back",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )

    st.divider()

    submitted = st.form_submit_button("Submit for Verification", use_container_width=True)

client = MongoClient(uri)

# --- Process after submit ---
if submitted:
    errors = []

    # Validate uploaded files
    if not front_aadhar_file:
        errors.append("⛔ Front Aadhar Photo is required.")
    if not back_aadhar_file:
        errors.append("⛔ Back Aadhar Photo is required.")
    if not dl_front_file:
        errors.append("⛔ DL Front Photo is required.")
    if not dl_back_file:
        errors.append("⛔ DL Back Photo is required.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        with st.spinner("🔍 Processing document with Gemini Flash 2.0..."):
            # Process front Aadhar photo
            front_aadhar_bytes = front_aadhar_file.read()
            back_aadhar_bytes = back_aadhar_file.read()
            front_aadhar_image = Image.open(io.BytesIO(front_aadhar_bytes))
            back_aadhar_image = Image.open(io.BytesIO(back_aadhar_bytes))

            # process DL front and back photos
            dl_front_bytes = dl_front_file.read()
            dl_back_bytes = dl_back_file.read()
            dl_front_image = Image.open(io.BytesIO(dl_front_bytes))
            dl_back_image = Image.open(io.BytesIO(dl_back_bytes))

            # Call Gemini OCR API for Aadhar
            ocr_result = call_gemini_ocr(front_aadhar_image, back_aadhar_image, dl_front_image, dl_back_image)
            # Call Gemini OCR API for DL
            ocr_result_adhar = ocr_result["adhar_details"]
            ocr_result_dl = ocr_result["dl_details"]
            match_results = compare_details_utils(ocr_result_adhar, ocr_result_dl)

            data ={
                "adhar_details": ocr_result_adhar,
                "dl_details": ocr_result_dl,
                "info_match_score": match_results["info_match_score"],
                "customer_valid": match_results["customer_valid"],
                "kyc_status": "not_verified"    
            }

            db = client["identity_documents"]
            collection = db["documents"]
            
            #check if the document already exists in the database
            existing_document = collection.find_one({"adhar_details.identity_card_no": ocr_result_adhar["identity_card_no"]})
            if existing_document:
                st.warning("⚠️ Document already exists in the database.")
            else:
                collection.insert_one(data)
                st.success("✅ Document processed successfully!")



           


        if ocr_result_adhar and ocr_result_dl and match_results:
            st.subheader("📄 Extracted OCR Details (Gemini Flash 2.0)")
            st.json(ocr_result_adhar, expanded=True)
            st.json(ocr_result_dl, expanded=True)
            st.subheader("🔍 Comparison Results")
            st.json(match_results, expanded=True)
            st.divider()
