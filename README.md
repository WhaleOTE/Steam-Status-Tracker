# Steam-Status-Tracker
Steam Status Tracker is a Python script that monitors one or more Steam accounts' activity status and logs the data in a file. 

# Steam Status Checker

Steam Status Tracker is a Python script that monitors one or more Steam accounts' activity status and logs the data in a file. It utilizes the Steam API to fetch the current status of the Steam IDs at regular intervals. The script logs the data in two separate log files, `steam_data_log.txt` and `status_changes_log.txt`.

## Requirements

- Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

## Installation

1. Clone the repository or download the script directly.

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Install the necessary dependencies using pip.

    ```bash
    pip install requests
    ```

## Configuration

Before running the script, you need to set up your API key and Steam IDs in the script. Follow the steps below:

1. Open the script file `steam_status_checker.py` in a text editor.

2. Locate the following lines and replace the placeholder values with your actual API key and Steam IDs:

    ```python
    API_KEY = 'YOUR_API_KEY'
    STEAM_ID_1 = 'STEAM_ID_1'
    STEAM_ID_2 = None  # Replace with an actual Steam ID if needed, or keep it as None for an optional ID
    ```

## How to Run

Open a terminal or command prompt and navigate to the directory where the script is located. Then, execute the following command:

    ```bash
    python steam_status_checker.py
    ```

The script will start monitoring the online status of the provided Steam IDs and will log the data in the specified log files. You can stop the script at any time by pressing `Ctrl + C` in the terminal.

## Output

The script logs the data in two files:

1. `steam_data_log.txt` - Contains a log of the Steam IDs' status at each check.
2. `status_changes_log.txt` - Contains a log of any status changes detected since the script started running.

## Notes

- Make sure to keep your API key secure and not share it with anyone.
- The script checks the status every minute by default, but you can modify the `time.sleep(60)` line in the script to adjust the frequency of checks according to your preference.
