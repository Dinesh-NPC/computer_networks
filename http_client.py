import requests
url = "http://localhost:8000" # Replace with any server URL
response = requests.get(url)
print(f"Status Code: {response.status_code}")
print(f"Response:\n{response.text}")
