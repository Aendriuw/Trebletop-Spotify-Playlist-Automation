# TrebleTop - Spotify playlist automation app

TrebleTop is a small Linux desktop app that automatically updates one of your Spotify playlists with your most listened songs. The number of songs in the playlist and the time range are chosen by the user.
Here is a screenshot of the user interface:

<img width="973" height="555" alt="GUI_demo" src="https://github.com/user-attachments/assets/8cb6215b-acc0-4085-8a7b-d188ad311da3" />

## Requirements
- Operating system: **Linux**
- **Python**: 3.8+
- Installed Python libraries (installed using pip install)
  - **spotipy**
  - **python-dotenv**
- A Spotify account with a **Premium Subscription** (because of the last spotify API update)
- A registered **Spotify for Developers app** (to obtain API credentials, more details in the Setup section)

## Setup

### 1. Clone the repository

bash:
'git clone https://github.com/your-username/trebletop.git
cd trebletop'

