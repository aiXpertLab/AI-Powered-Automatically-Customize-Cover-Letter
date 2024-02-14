from openai import OpenAI
import os

def check_openai_api_key(api_key):
    windows_key = os.environ.get("OPENAI_API_KEY")
    if windows_key is None:
        windows_key = "sk_input"
    client = OpenAI(api_key = windows_key)

    try:
        client.models.list()
        print('good')
    except Exception as e:
        print(client.api_key)
        print("An error occurred:", e)

    # if client.api_key[:2] != 'sk':
    #     client = OpenAI(api_key = api_key)

check_openai_api_key("key")