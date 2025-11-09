import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("chess-mcp")

@mcp.tool()
async def get_chess_games(username: str, year: str, month: str) -> str:
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
        return response.text
    return ""
