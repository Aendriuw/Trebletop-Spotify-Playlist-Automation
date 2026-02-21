### 1. Clone the repository

bash:
'git clone https://github.com/your-username/trebletop.git
cd trebletop'
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

Rename the `.env_example` in the root to `.env` and complete the appropriate content.
Don't share this .env file.