import vk
import asyncio
from credentials import LOGIN, PASSWORD

APP_ID = '5615994'
PERMISSIONS = 'audio,groups,status,offline'

# Settings

# Album to stream music from
ALBUM_ID = '78066191'
# Ids of targets (users or groups). If stream to group, use negated id.
TARGETS = '-74043360'


async def update_status():
    current_track_index = 0
    while True:
        tracks = api.audio.get(album_id=ALBUM_ID)
        if current_track_index >= len(tracks):
            current_track_index = 0
        track = tracks[current_track_index]
        current_track_index += 1
        
        track_id = '{}_{}'.format(track['owner_id'], track['aid'])
        api.audio.setBroadcast(audio=track_id, target_ids=TARGETS)
        track_duration = track['duration']
        await asyncio.sleep(track_duration)


def main():
    session = vk.AuthSession(app_id=APP_ID, user_login=LOGIN, user_password=PASSWORD, scope=PERMISSIONS)
    api = vk.API(session)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_status())
    loop.close()


if __name__ == '__main__':
    main()
