import requests
import os
import shutil
from datetime import datetime

download_folder = 'fafa_aboagye'
local_file_path = os.path.join(download_folder, "fafa_aboagye.txt")

# Remove existing directory
if os.path.exists(download_folder):
    try:
        shutil.rmtree(download_folder)
        print(f"Directory '{download_folder}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Create directory
os.makedirs(download_folder, exist_ok=True)
print(f"Directory: {download_folder} created.")

# Downloading file
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print("File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
    print('File saved successfully.')
else:
    print(f"Failed to download file. Status code: {response.status_code}")


user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


try:
    with open(local_file_path, "w") as file:
        file.write(user_input + "\n")
        file.write(f"Last modified on: {current_time}\n")
    print("File successfully modified.")
except Exception as e:
    print(f"Error writing to file: {e}")


try:
    with open(local_file_path, "r") as file:
        print("\nYou Entered: ", end=' ')
        print(file.read())
except Exception as e:
    print(f"Error reading from file: {e}")
 
