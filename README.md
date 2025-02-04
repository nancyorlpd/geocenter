# GeoCenter

GeoCenter is a Python-based utility designed to enhance the longevity of Windows-operated devices by applying critical updates and power management tweaks. This script automates the process of keeping your Windows system up-to-date and optimizes power settings for better energy efficiency.

## Features

- Automatically installs critical Windows updates.
- Configures power management settings to extend device lifespan:
  - Sets AC monitor timeout to 10 minutes.
  - Sets DC (battery) monitor timeout to 5 minutes.
  - Enables hibernation for reduced power usage.

## Requirements

- Python 3.x
- Windows Operating System
- Administrative privileges to execute system commands

## Usage

1. Ensure that Python is installed on your Windows machine.
2. Download or clone the repository to your local system.
3. Open a command prompt with administrative privileges.
4. Navigate to the directory containing `geocenter.py`.
5. Run the script using the command: `python geocenter.py`

## Important Notes

- GeoCenter is designed to work exclusively on Windows platforms.
- Make sure you have the necessary permissions to perform system updates and modify power settings.
- The script uses PowerShell commands and may trigger User Account Control (UAC) prompts.

## Troubleshooting

- If you encounter any errors related to permissions, ensure that you are running the command prompt as an administrator.
- For any issues with updates, verify your internet connection and Windows Update settings.

## License

GeoCenter is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.