# import requests

# url = "http://localhost:8000/brief/token_feedback"
# data = {"input": {"topic": "Green house gas emission and its impact on climate change"}}

# try:
#     response = requests.post(url, json=data)
#     response.raise_for_status()  # Raise an exception for HTTP errors
#     content = response.json()["output"]["content"]
#     print(content)
# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP error occurred: {http_err}")
# except requests.exceptions.RequestException as req_err:
#     print(f"Request error occurred: {req_err}")
# except ValueError as val_err:
#     print(f"Error decoding JSON: {val_err}")
# except KeyError as key_err:
#     print(f"KeyError: {key_err}")
import requests

response = requests.post(
    "http://localhost:8000/joke/invoke",
    json={'input': {'topic': 'cats'}}
)
print(response.json())