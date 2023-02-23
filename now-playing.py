import os
from dotenv import load_dotenv

load_dotenv()

url: str = 'https://api.music.apple.com/v1/me/recent/played/tracks'

headers: dict = {
    'Authorization': f'Bearer {os.environ["APPLE_MUSIC_DEV_TOKEN"]}',
    'Music-User-Token': os.environ['APPLE_MUSIC_USER_TOKEN'],
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def get_now_playing():
    import requests
    try:
        result = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    print(result.status_code)
    print(result.headers)
    print(result.content)
    return result


if __name__ == '__main__':
    import json
    with open('now-playing.json', 'w') as f:
        result = get_now_playing().json()
        if result is not None:
            json.dump(result, f, indent=2)
