from flask import Flask, render_template_string
import boto3

app = Flask(__name__)

# AWS credentials - hardcoded as per your request
AWS_ACCESS_KEY = 'AKIAWVZBUMHODNLLXI2K'
AWS_SECRET_KEY = 'tOjA7M6ZnXQ0X7cLGvKJkuCwdba5FGlidYRwGaqk'
AWS_REGION = 'ap-south-1'
BUCKET_NAME = 'newawignbucket'

# Boto3 client setup
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

@app.route('/')
def show_image():
    # The S3 object key (folder path + filename)
    object_key = 'index/Darshan.jpg.jpg'

    # Generate presigned URL
    image_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': object_key},
        ExpiresIn=3600  # URL valid for 1 hour
    )

    # Render the image
    return render_template_string('''
        <h1>Image from S3</h1>
        <img src="{{ image_url }}" alt="Image from S3" />
    ''', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
