import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("chess-mcp")

@mcp.tool()
async def get_chess_games(username: str, year: str, month: str) -> str:
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}/pgn"
    
    headers = {
        'User-Agent': 'Me'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    return ""
