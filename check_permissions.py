import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def check_my_token():
    scope = "user-top-read playlist-modify-public playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=scope,
        open_browser=False
    ))

    # 1. Who am I?
    me = sp.current_user()
    print(f"--- DIAGNOSTIC REPORT ---")
    print(f"Logged in as: {me['display_name']} (ID: {me['id']})")

    # 2. What can I do?
    # This checks the actual scopes tied to your current .cache file
    token_info = sp.auth_manager.get_cached_token()
    print(f"Active Scopes: {token_info.get('scope')}")

    # 3. Who owns the target playlist?
    playlist_id = os.getenv('SPOTIPY_PLAYLIST_ID')
    playlist = sp.playlist(playlist_id)
    print(f"Target Playlist: {playlist['name']}")
    print(f"Playlist Owner ID: {playlist['owner']['id']}")
    
    if me['id'] == playlist['owner']['id']:
        print("RESULT: You OWN this playlist. Ownership is not the issue.")
    else:
        print("RESULT: You DO NOT own this playlist. This is why you get a 403.")

if __name__ == "__main__":
    check_my_token()