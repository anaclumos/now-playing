import os
from dotenv import load_dotenv

load_dotenv()

url: str = 'https://api.music.apple.com/v1/me/recent/played/tracks'

headers: dict = {
    'Authorization': f'Bearer {os.environ.get("APPLE_MUSIC_DEV_TOKEN")}',
    'Music-User-Token': os.environ.get('APPLE_MUSIC_USER_TOKEN'),
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_now_playing():
    import requests
    result = requests.get(url, headers=headers)
    print(result.json())
    return result


if __name__ == '__main__':
    import json
    with open('now-playing.json', 'w') as f:
        json.dump(get_now_playing().json(), f, indent=2)
