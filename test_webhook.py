import requests


user_message =  "Can you tell me about black holes in 3-4 line?"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/c164777d-0a85-4d20-851c-096a24791b46"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.json())

