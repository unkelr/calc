# CALC

## Overview

This is a Python-based Discord utility script that allows users to perform various operations using their Discord token, including:
- Retrieving server information
- Listing friends
- Viewing personal account details
- Mass messaging friends
- Changing user activity status

⚠️ **Disclaimer**: Use this tool responsibly and in compliance with Discord's Terms of Service.

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/unkelr/calc
cd calc
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```


### Running the Script

Windows batch file to install requirements and launch the script.
- On Windows: Double-click `start.bat`
- On macOS/Linux: 
  ```bash
  pip3 install -r requirements.txt
  python calc.py
  ```

### Main Menu Options

1. **Get Servers**: List and optionally save Discord servers you're a member of
2. **Get Friends**: List and optionally save your Discord friends
3. **Get Info**: View your Discord account details
4. **MassDM**: Send a mass direct message to all your friends
5. **Change Activity**: Update your Discord custom status
6. **Exit**: Close the application

## Important Notes

- You must provide a valid Discord token to use this tool
- Token is saved in `config.json` for future use
- The script uses Discord API v9, v10
- Outputs are saved in `outputs/` directories

## Security Warning

🚨 **Never share your Discord token publicly!** This token provides access to your account.

## Dependencies

- `requests`: HTTP library for API calls
- `colorama`: Terminal text coloring
- `json`: JSON configuration handling

## Contribution

Feel free to open issues or submit pull requests to improve the tool.

[Website!](https://unkelrunkel.se)
