# Telegram Group Manager

A Python script to manage Telegram group members using the Telethon library.

# Table of Contents

- [Features](#features)
- [Installation](#installation)
  1. [Clone the Repository](#1-clone-the-repository)
  2. [Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
  3. [Install Dependencies](#3-install-dependencies)
  4. [Configure the Application](#4-configure-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)


## Features

- **Load Configuration**: Load Telegram credentials from a YAML configuration file.
- **Connect to Telegram**: Authenticate and connect to Telegram using Telethon.
- **Fetch Participants**: Retrieve participants from a specified source group.
- **Filter Users**: Exclude specific users from being added to the target group.
- **Add Users to Group**: Add filtered users to a target Telegram group with proper error handling.
- **Logging**: Provides informative console output for monitoring the script’s progress.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-group-manager.git
cd telegram-group-manager
```
*Replace yourusername with your actual GitHub username.*

### 2. Create and Activate a Virtual Environment

It’s recommended to use a virtual environment to manage your project’s dependencies.

```
python -m venv venv
```

**Activate the Virtual Environment:**
- **For Linux/Mac:**

```bash
source venv/bin/activate
```

- **For Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Application

**Rename Configuration File:**

Copy the example configuration file to create your own config.yaml:

```bash
cp config.example.yaml config.yaml
```

**Edit config.yaml:**

Open config.yaml in your preferred text editor and fill in your Telegram credentials:

```yaml
credentials:
  telegram:
    api_id: YOUR_API_ID
    api_hash: YOUR_API_HASH
    phone_number: YOUR_PHONE_NUMBER
```

- `api_id` and `api_hash`: Obtain these from Telegram’s API development tools at [my.telegram.org](https://my.telegram.org/auth). 
- `phone_number`: The phone number associated with your Telegram account.

## Usage

Run the main script to execute the Telegram group management tasks:

```bash
python main.py
```

**Script Workflow:**

1.	**Authentication**: The script authenticates with Telegram using the provided credentials.
2.	**Source Group**: It fetches participants from the source group specified in the script (current_group by default).
3.	**Filter Users**: Excludes users listed in the excluded_users list.
4.	**Target Group**: Adds the filtered users to the target group (target_group by default).
5.	**Logging**: Outputs the progress and any encountered errors to the console.

## Project Structure

```
telegram_group_manager/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── config.example.yaml
├── main.py
└── utils/
    ├── __init__.py
    ├── config_loader.py
    └── telegram_manager.py
```

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: Contains the project’s license information.
- `README.md`: Provides an overview and instructions for the project.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `config.example.yaml`: Example configuration file to guide users in setting up their own config.yaml.
- `main.py`: The main script that orchestrates the group’s management tasks.
- `utils/`: Directory containing utility modules.
- `__init__.py`: Indicates that utils is a Python package.
- `config_loader.py`: Handles loading configuration from the YAML file.
- `telegram_manager.py`: Manages interactions with Telegram using Telethon.


## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software under the terms of the license.
