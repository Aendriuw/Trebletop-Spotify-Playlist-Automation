import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Connects to the spotify client.
def get_spotify_client():
	scope = "user-top-read playlist-modify-public playlist-modify-private"
	auth_manager = SpotifyOAuth(
		client_id=os.getenv('SPOTIPY_CLIENT_ID'),
		client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
		redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
		scope=scope,
		open_browser=True,
		show_dialog=True,
		cache_path=".spotify_cache"
	)
	sp = spotipy.Spotify(auth_manager=auth_manager)

	def patched_playlist_replace_items(playlist_id, items):
		sp._put(f"playlists/{playlist_id}/items", payload={"uris": items[:100]})
		for i in range(100, len(items), 100):
			sp._post(f"playlists/{playlist_id}/items", payload={"uris": items[i:i+100]})

	sp.playlist_replace_items = patched_playlist_replace_items

	return sp

# Fetches the current user's top tracks.
# API max per call is 50 songs uris, so we fetch by chunks of 50.
def fetch_top_tracks(sp, time_range='short_term', limit=100):
	track_uris = []

	for offset_val in range(0, limit, 50):
		try:
			results = sp.current_user_top_tracks(
				time_range=time_range,
				limit=50,
				offset=offset_val
			)
			batch = [track['uri'] for track in results['items']]
			track_uris.extend(batch)

			if len(results['items']) < 50:
				break

		except spotipy.exceptions.SpotifyException as e:
			print(f"Error fetching top tracks.")
			raise

	print(f"Fetched {len(track_uris)} top tracks.")
	return track_uris

# Replaces all items in the playlist with the given track URIs.
# Playlist_replace_items replaces in chunks of max 100.
def update_playlist(sp, playlist_id, track_uris):
	if not track_uris:
		print("No tracks found. Not updating.")
		return

	try:
		sp.playlist_replace_items(playlist_id, track_uris)
		print(f"Updated playlist {playlist_id} with {len(track_uris)} tracks.")
	except spotipy.exceptions.SpotifyException as e:
		print(f"Error updating playlist.")
		raise

def main():
	sp = get_spotify_client()

	playlist_id = os.getenv('SPOTIPY_PLAYLIST_ID')
	if not playlist_id:
		raise ValueError("SPOTIPY_PLAYLIST_ID is not set in your .env file.")

	top_uris = fetch_top_tracks(sp, time_range='short_term', limit=100)
	update_playlist(sp, playlist_id, top_uris)


if __name__ == "__main__":
	main()