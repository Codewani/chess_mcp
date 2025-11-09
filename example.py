
import requests
import json

def get_chess_games(username, year, month):
    # Construct the API URL
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}/pgn"
    
    # Make the API request with headers to bypass Cloudflare
    headers = {
        'User-Agent': 'Me'
    }
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Print the PGN response (it's text, not JSON)
        print(response.text)
    else:
        print(f"Error {response.status_code}: {response.text}")

# Example usage - use a past date
username = "kondwani2"
year = "2025"
month = "09"

get_chess_games(username, year, month)