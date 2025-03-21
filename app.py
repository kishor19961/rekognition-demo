import streamlit as st
import boto3

# AWS Credentials (hardcoded - not recommended for production)
AWS_ACCESS_KEY = "AKIAWVZBUMHODNLLXI2K"
AWS_SECRET_KEY = "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"
REGION_NAME = "ap-south-1"
BUCKET_NAME = "newawignbucket"

# Initialize AWS Rekognition client
rekognition_client = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

st.title("Face Recognition with AWS Rekognition")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Read file bytes
    file_bytes = uploaded_file.read()
    
    # Call AWS Rekognition for face detection
    response = rekognition_client.detect_faces(
        Image={'Bytes': file_bytes},
        Attributes=['ALL']
    )
    
    st.write("Detected Faces:")
    st.json(response)
