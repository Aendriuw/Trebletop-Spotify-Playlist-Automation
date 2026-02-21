# TrebleTop - Spotify playlist automation app

TrebleTop is a small Linux desktop app that automatically updates one of your Spotify playlists with your most listened songs. The number of songs in the playlist and the time range are chosen by the user.
Here is a screenshot of the user interface:

<img width="973" height="555" alt="GUI_demo" src="https://github.com/user-attachments/assets/8cb6215b-acc0-4085-8a7b-d188ad311da3" />

## Setup

### 1. Clone the repository

bash:
`git clone https://github.com/Aendriuw/Trebletop-Spotify-Playlist-Automation
cd trebletop`

### 2. Install dependecies

bash:
`pip install spotipy python-dotenv`

### 3. Create a Spotify for Developers app

1. Go to the Spotify for Developers website (https://developer.spotify.com/) and log in with your Spotify account
2. Go to the dashboard and click **create app**
3. For website use: http://localhost:8888
4. For redirect URIs use: http://127.0.0.1:8888/callback (Most Linux machines have the 127.0.0.1 ip address configured, if you have another ip address configured change the one in the URI with yours)
5. Save the app and note down your **Client ID** and **Client Secret**.

### 4. Copy your playlist's ID

Open your playlist and copy the link to the playlist. The playlist ID  is between the "playlist/" and the "?" character:
https://open.spotify.com/playlist/**<playlist_id>**? ...

### 5. Configure the **.env** file

Rename the `.env_example` in the root to `.env` and complete the appropriate content. The client id and secret key are found on the Spotify for developers website. The **redirect link** should be the **exact same** as the redirect URI used on the Spotify for developers website. The playlist id is the one copied from the link.
Don't share this .env file.

## Run

bash:
`python3 trebletop.py`

On the first run, a browser window will open asking to authorise the app with your Spotify account. After authorising, a `.spotify_cache` file will be created locally to store your session so you won't need to log in again.

## Resources used

### Spotipy & the Spotify Web API

**Spotipy** is a Python wrapper around the **Spotify Web API**. The program uses it to:
- Authenticate with your Spotify account using `SpotifyOAuth`
- Read your **top tracks** using the `current_user_top_tracks` endpoint
- Modify a playlist using the `playlist_replace_items` endpoint

### Azure ttk Theme

The UI uses the **Azure ttk theme** (https://github.com/rdbende/Azure-ttk-theme) by **rdbende**. It is included in this repository with its original MIT license.
