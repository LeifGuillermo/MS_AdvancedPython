# Azure_Storage Project

This project provides Python utilities for interacting with Azure Storage services, such as Blob Storage. It enables you to upload, download, and manage files in your Azure Storage account.

## Features

- Upload files to Azure Blob Storage
- Download files from Azure Blob Storage
- List blobs in a container
- Delete blobs

## Prerequisites

- Python 3.7 or higher
- Azure Storage Account
- Required Python packages (see `requirements.txt`)

## Setup

1. **Clone the repository**  
    Download or clone this project to your local machine.

2. **Install Dependencies**  
    This project requires several Python packages to interact with Azure Storage and manage environment variables:

    - `azure-storage-blob`: Azure Blob Storage SDK
    - `python-dotenv`: For loading environment variables from a `.env` file (optional, but recommended)
    To install all required packages, run:
    ```
    pip install -r requirements.txt
    ```

3. **Set Environment Variables**  
    The project requires the following environment variables:

    - `AZURE_STORAGE_CONNECTION_STRING`: Your Azure Storage account connection string.
    - `AZURE_STORAGE_CONTAINER_NAME`: The name of the container you want to use.

    **How to find these in Azure:**
    - Go to the [Azure Portal](https://portal.azure.com).
    - Navigate to your Storage Account.
    - Under "Security + networking", select "Access keys".
    - Copy the "Connection string" value.
    - Create a container in "Containers" and use its name.

    **Set environment variables (example for Windows):**
    ```
    set AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
    set AZURE_STORAGE_CONTAINER_NAME=your_container_name_here
    ```

    For Linux/macOS:
    ```
    export AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
    export AZURE_STORAGE_CONTAINER_NAME=your_container_name_here
    ```

## Usage

Run `python azure_storage.py`. This will upload my_file.txt to your Azure storage, and then download the text into a file called downloaded_file.txt.

## Important Notes

- Never commit your connection string or other secrets to source control.
- Make sure your Azure Storage account has the correct permissions for the operations you want to perform.
- For more information, see the [Azure Storage documentation](https://docs.microsoft.com/en-us/azure/storage/).