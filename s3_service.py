import boto3, os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("aws_access_key_id"),
    aws_secret_access_key=os.getenv("aws_secret_access_key"),
    aws_session_token=os.getenv("aws_session_token"),
    region_name=os.getenv("aws_region", "us-east-1")
)

S3_BUCKET = os.getenv("s3_bucket_name", "s3-bucket-pokeneas")

def get_image_url(filename):
    """Retorna la URL pública de una imagen almacenada en S3"""
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{filename}"
