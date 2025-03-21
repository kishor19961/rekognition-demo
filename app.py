import streamlit as st
import boto3

# Streamlit title
st.title("Amazon Rekognition Face Detection Demo")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

# AWS credentials (DO NOT hardcode in production - for demo purpose only)
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'  # Example: 'us-east-1'

if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    image_bytes = uploaded_file.read()

    # AWS Rekognition client
    client = boto3.client('rekognition',
                          aws_access_key_id=AKIAWVZBUMHODNLLXI2K,
                          aws_secret_access_key=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,
                          region_name=ap-south-1)

    # Call Rekognition
    response = client.detect_faces(Image={'Bytes': image_bytes}, Attributes=['ALL'])

    # Show response
    st.write("Detected Faces:")
    for face in response['FaceDetails']:
        st.json(face)
