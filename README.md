# Dynamic Top 10 Playlist

A Python project that dynamically updates a Spotify playlist to include top tracks from specific artists. Using the Spotify API, this script checks and refreshes the playlist content, ensuring that only the top songs from selected artists are included. It also tracks changes to prevent duplicate entries and optimize playlist maintenance.

## Features

- **Dynamic Playlist Updating**: Continuously refreshes a Spotify playlist with the top tracks from selected artists.
- **Caching Mechanism**: Keeps track of previously added songs to avoid re-adding or duplicating tracks.
- **Efficient Item Management**: Limits API calls to add or remove songs up to 100 tracks at a time.
- **User Notifications**: Displays song addition and removal notifications in the console for easy tracking.

## Setup

1. **Spotify Developer Account**: Set up a Spotify Developer account to obtain `Client ID`, `Client Secret`, and register a redirect URI.
2. **Clone Repository**
3. **Install Dependencies**:
    ```bash
    pip install spotipy
    ```
4. **Configure Environment**: Set your Spotify API credentials in the script:
- `clientID`
- `clientSecret`
- `redirectURI`

5. Run Script:
    ```bash
    python dynamicTop10.py
    ```

## Usage
- **Authenticate**: On first run, the script will prompt you to authenticate with Spotify.
- **Automatic Playlist Update**: The script fetches top tracks for selected artists and updates the designated playlist.
- **Customizing Artists**: Modify the artistIDs list to select artists whose top tracks should be featured.

## Dependencies
- **Spotipy**: A Python client for the Spotify Web API.
    ```bash
    pip install spotipy
    ```
## Notes
- **Rate Limiting**: This script limits the number of added or removed tracks to 100 per operation to comply with Spotify’s API constraints.
- **Error Handling**: The script outputs relevant messages in the console for troubleshooting.