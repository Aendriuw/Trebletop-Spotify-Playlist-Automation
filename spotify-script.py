# Initial failed attempt
# Spotify restricted the exact endpoints which I needed for this project, making the prohect
# impossible to complete. :^)

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def get_spotify_client():
    scope = "user-top-read playlist-modify-public playlist-modify-private"
    
    auth_manager = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=scope,
        open_browser=True,
		show_dialog=True
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def fetch_top_tracks(sp, time_range='short_term', limit=100):
    track_uris = []
    
    # We loop in steps of 50 because that is the Spotify API limit per call
    for offset_val in range(0, limit, 50):
        results = sp.current_user_top_tracks(
            time_range=time_range, 
            limit=50, 
            offset=offset_val
        )
        batch = [track['uri'] for track in results['items']]
        track_uris.extend(batch)
        
    return track_uris

def update_playlist(sp, playlist_id, track_uris):
	if not track_uris:
		print("No tracks found. Skipping update.")
		return

	sp.playlist_replace_items(playlist_id, track_uris)
	print(f"Successfully updated playlist {playlist_id} with {len(track_uris)} tracks.")

def main():
	#limit = 100

	sp = get_spotify_client()

	playlist_id = os.getenv('SPOTIPY_PLAYLIST_ID')

	top_100_uris = fetch_top_tracks(sp, time_range='short_term', limit=100)

	update_playlist(sp, playlist_id, top_100_uris)

if __name__ == "__main__":
	main()