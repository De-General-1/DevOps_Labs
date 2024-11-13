import requests

# Make a GET request to a URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful with a status code of 200
if response.status_code == 200:
    # We just want to print the response of the request
    print(response.json())
else:
    # printing an error message if something went wrong    
    print(f'Error: {response.status_code}')