# Python Service Management and Temp Folder Cleanup

This Python script automates the process of restarting system services and cleaning up temporary folders. It provides two main functionalities:

1. **Restarting a system service** using `systemctl` (e.g., `cron`).
2. **Clearing a temporary folder** and recreating it.

## Features

- **Restart a system service**: The script allows restarting services like `cron`, `apache2`, etc., with `sudo` permissions.
- **Clear and recreate a temporary folder**: It deletes the contents of a specified folder and recreates it.

## Requirements

- Python 3.x
- `sudo` privileges to restart system services
- Access to the system's temporary folder (e.g., `/tmp`)

## How to Use

1. **Clone the repository**:
    ```bash
    https://github.com/De-General-1/DevOps_Labs/new/main/lab_2_cron_jobs
    ```

2. **Run the script**:
    ```bash
    python3 manage_service_and_temp.py
    ```

   This will:
   - Restart the `cron` service.
   - Clear and recreate the `/tmp/temp` folder.

## Code Example

```python
import os
import subprocess
import shutil

def restart_service(service_name):
    subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)

def clear_temp_folder(temp_folder):
    shutil.rmtree(temp_folder)
    os.makedirs(temp_folder)

if __name__ == "__main__":
    restart_service("cron")
    clear_temp_folder("/tmp/temp")
