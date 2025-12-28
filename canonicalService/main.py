from fastapi import FastAPI
import boto3
import os
from dotenv import load_dotenv
from schema import InputSchema
from PIL import Image
import io
import pytesseract 
from utils.normalizer import normalize
from utils.edges import infer_edges
from utils.canonicalizer import canonicalize
load_dotenv()
s3 = boto3.client(
     's3', 
     aws_access_key_id= os.getenv("AWS_ACCESS_KEY_ID"), 
     aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
     region_name = os.getenv("COGNITO_REGION")
        )

can_app = FastAPI()

@can_app.post("/canonic")
def canonic_img(payload: InputSchema):
    file_key = payload.file_key
    bucket = os.getenv("BUCKET_NAME")
    obj = s3.get_object(Bucket=bucket, Key=file_key)
    image_bytes = obj["Body"].read()
    image = Image.open(io.BytesIO(image_bytes).convert("RGB")) #convert to pixels
    text = pytesseract.image_to_string(image)
    components = normalize(text)
    edges = infer_edges(components)
    canonical = canonicalize(components, edges)
    return canonical


    
