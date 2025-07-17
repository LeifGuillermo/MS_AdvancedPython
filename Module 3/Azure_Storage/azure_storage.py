from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()
account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
account_key = os.getenv("AZURE_STORAGE_ACCOUNT_ACCESS_KEY")

blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net", 
    credential=account_key
)

#Create a new container called my-container. If it already exists, get the existing container client.
container_name = "my-container"
try:
    container_client = blob_service_client.create_container(container_name)
except Exception as e:
    if hasattr(e, 'error_code') and e.error_code == 'ContainerAlreadyExists':
        container_client = blob_service_client.get_container_client(container_name)
    else:
        raise

blob_client = container_client.get_blob_client("my_blob")

# Upload a file to the container
with open("my_file.txt", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

# Download a blob from the container
with open("downloaded_file.txt", "wb") as data:
    blob_client.download_blob().readinto(data)