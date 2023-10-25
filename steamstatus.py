import requests
import time
from datetime import datetime

# Set your API key and Steam IDs here
API_KEY = 'YOUR_API_KEY'
STEAM_ID_1 = 'STEAM_ID_1'
STEAM_ID_2 = None  # Replace with an actual Steam ID if needed, or keep it as None for an optional ID

status_names = {
    0: 'Offline',
    1: 'Online',
    2: 'Busy',
    3: 'Away',
    4: 'Snooze',
    5: 'Looking to Trade',
    6: 'Looking to Play'
}

url_template = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={}&format=json&steamids={}'

steam_ids = [STEAM_ID_1]
if STEAM_ID_2:
    steam_ids.append(STEAM_ID_2)

previous_states = {steam_id: None for steam_id in steam_ids}

while True:
    for steam_id in steam_ids:
        url = url_template.format(API_KEY, steam_id)
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                personastate_data = data['response']['players'][0]['personastate']
                personaname = data['response']['players'][0]['personaname']
                current_time = datetime.now().strftime('%Y/%m/%d %H:%M')
                status = status_names.get(personastate_data, 'Unknown Status')
                with open('steam_data_log.txt', 'a') as file:
                    file.write(f'[{current_time}] {personaname} - {status}\n')
                if personastate_data != previous_states[steam_id]:
                    with open('status_changes_log.txt', 'a') as changes_file:
                        changes_file.write(f'[{current_time}] {personaname} - {status}\n')
                    print(f'[{current_time}] {personaname} - {status}')
                    previous_states[steam_id] = personastate_data
                else:
                    print(f'[{current_time}] {personaname} - {status}')
            else:
                print(f'Failed to retrieve data for {steam_id}. Status Code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error occurred for {steam_id}: {e}')

    time.sleep(60)  # Sleep for 1 minute before the next check
