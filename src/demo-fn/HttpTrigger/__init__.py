import logging
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing HTTP request to fetch secret from Azure Key Vault.")

    # Get Key Vault URL and secret name from environment variables
    key_vault_url = os.getenv("KEY_VAULT_URL")
    secret_name = os.getenv("SECRET_NAME")

    if not key_vault_url or not secret_name:
        return func.HttpResponse(
            "Environment variables KEY_VAULT_URL or SECRET_NAME are not set.",
            status_code=500,
        )

    try:
        # Authenticate with Azure Key Vault
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        # Retrieve the secret value
        secret = client.get_secret(secret_name)

        return func.HttpResponse(
            f"The value of the SECRET '{secret_name}' is:\n\n\n{secret.value}",
            status_code=200,
        )
    except Exception as e:
        logging.error(f"Error fetching secret: {e}")
        return func.HttpResponse(
            "An error occurred while fetching the secret.",
            status_code=500,
        )