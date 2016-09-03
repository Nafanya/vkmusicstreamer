import vk
import asyncio
import sys

from credentials import LOGIN, PASSWORD
from settings import APP_ID, PERMISSIONS, ALBUM_ID, TARGETS


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
        
        track_title = '{} - {}'.format(track['artist'], track['title'])
        track_title = (track_title[:75] + '..') if len(track_title) > 77 else track_title
        
        sys.stdout.write('{}\r'.format(track_title))
        sys.stdout.flush()
        
        track_duration = track['duration']
        await asyncio.sleep(track_duration)



session = vk.AuthSession(app_id=APP_ID, user_login=LOGIN, user_password=PASSWORD, scope=PERMISSIONS)
api = vk.API(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(update_status())
loop.close()
