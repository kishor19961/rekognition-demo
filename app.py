import streamlit as st
import boto3

# Set up AWS Rekognition client
rekognition = boto3.client('rekognition',
                           aws_access_key_id='YOUR_AWS_ACCESS_KEY',
                           aws_secret_access_key='YOUR_AWS_SECRET_KEY',
                           region_name='YOUR_REGION')

st.title("Guard Verification Demo")

# Create form
with st.form("guard_form"):
    guard_id = st.text_input("Enter Guard ID")
    workforce_id = st.text_input("Enter Workforce ID")
    uploaded_file = st.file_uploader("Capture or Upload Photo", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        
        # Call Rekognition (example: detect faces)
        response = rekognition.detect_faces(
            Image={'Bytes': bytes_data},
            Attributes=['ALL']
        )
        
        st.write(f"Guard ID: {guard_id}")
        st.write(f"Workforce ID: {workforce_id}")
        st.write("Rekognition Result:")
        st.json(response)
    else:
        st.warning("Please upload a photo!")
