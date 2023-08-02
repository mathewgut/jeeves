import spotipy
from spotipy.oauth2 import SpotifyOAuth
from passwords import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL

scope = "user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL, username='itszraven'))

#class man:
    #def __init__(self):


def liked():
    track_list = []
    results = sp.current_user_saved_tracks()
    count = 0
    for idx, item in enumerate(results['items']):
        count +=1
        track = item['track']
                #print(track)
        val1 = (idx, track['artists'][0]['name'], " – ", track[0]['name'])
        track_list.append(val1)
        #print(track_list)
    return val1 

def add_to_queue(song):
    sp.add_to_queue(device_id=None)

def song_current():
    # Set up authentication

    # Get the current playback information
    current_playback = sp.current_playback()

    # Check if there is a currently playing track
    if current_playback is not None and current_playback["is_playing"]:
        # Get the current track
        current_track = current_playback["item"]
        # Get the track name and artist(s)
        track_name = current_track["name"]
        artists = [artist["name"] for artist in current_track["artists"]]
        return f"Currently playing: {track_name} by {', '.join(artists)}"
    else:
        return "No track currently playing"

