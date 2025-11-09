import httpx
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP
from chess_urls import CHESSAPIURLS


mcp = FastMCP("chess-mcp")

chess_urls = CHESSAPIURLS()

# Global headers used for all outgoing requests
HEADERS = {"User-Agent": "Me"}


@mcp.tool()
async def get_chess_pgns(username: str, year: str, month: str) -> str:
    url = chess_urls.player_games_pgn(username, year, month)

    async with httpx.AsyncClient() as ac:
        response = await ac.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.text
    return ""


@mcp.tool()
async def get_player_profile(username: str) -> Any:
    url = chess_urls.player_profile(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_titled_players(title_abbrev: str) -> Any:
    url = chess_urls.titled_players(title_abbrev)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_player_stats(username: str) -> Any:
    url = chess_urls.player_stats(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_player_is_online(username: str) -> Any:
    url = chess_urls.player_is_online(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"online": False}


@mcp.tool()
async def get_player_games_current(username: str) -> Any:
    url = chess_urls.player_games_current(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"games": []}


@mcp.tool()
async def get_player_games_to_move(username: str) -> Any:
    url = chess_urls.player_games_to_move(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"games": []}


@mcp.tool()
async def get_player_games_archives(username: str) -> Any:
    url = chess_urls.player_games_archives(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"archives": []}


@mcp.tool()
async def get_player_games_archive(username: str, year: str, month: str) -> Any:
    url = chess_urls.player_games_archive(username, year, month)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"games": []}


@mcp.tool()
async def get_player_games_live_by_time(username: str, basetime: int, increment: Optional[int] = None) -> Any:
    url = chess_urls.player_games_live_by_time(username, basetime, increment)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"games": []}


@mcp.tool()
async def get_player_clubs(username: str) -> Any:
    url = chess_urls.player_clubs(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"clubs": []}


@mcp.tool()
async def get_player_matches(username: str) -> Any:
    url = chess_urls.player_matches(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"finished": [], "in_progress": [], "registered": []}


@mcp.tool()
async def get_player_tournaments(username: str) -> Any:
    url = chess_urls.player_tournaments(username)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"finished": [], "in_progress": [], "registered": []}


@mcp.tool()
async def get_club_profile(url_id: str) -> Any:
    url = chess_urls.club_profile(url_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_club_members(url_id: str) -> Any:
    url = chess_urls.club_members(url_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"weekly": [], "monthly": [], "all_time": []}


@mcp.tool()
async def get_club_matches(url_id: str) -> Any:
    url = chess_urls.club_matches(url_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"finished": [], "in_progress": [], "registered": []}


@mcp.tool()
async def get_tournament(url_id: str) -> Any:
    url = chess_urls.tournament(url_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_tournament_round(url_id: str, round_no: int) -> Any:
    url = chess_urls.tournament_round(url_id, round_no)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_tournament_round_group(url_id: str, round_no: int, group: int) -> Any:
    url = chess_urls.tournament_round_group(url_id, round_no, group)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_match(match_id: int) -> Any:
    url = chess_urls.match(match_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_match_board(match_id: int, board: int) -> Any:
    url = chess_urls.match_board(match_id, board)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_live_match(match_id: int) -> Any:
    url = chess_urls.live_match(match_id)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_live_match_board(match_id: int, board: int) -> Any:
    url = chess_urls.live_match_board(match_id, board)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_country_profile(iso: str) -> Any:
    url = chess_urls.country_profile(iso)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_country_players(iso: str) -> Any:
    url = chess_urls.country_players(iso)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"players": []}


@mcp.tool()
async def get_country_clubs(iso: str) -> Any:
    url = chess_urls.country_clubs(iso)
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"clubs": []}


@mcp.tool()
async def get_daily_puzzle() -> Any:
    url = chess_urls.daily_puzzle()
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_random_daily_puzzle() -> Any:
    url = chess_urls.random_daily_puzzle()
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}


@mcp.tool()
async def get_streamers() -> Any:
    url = chess_urls.streamers()
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {"streamers": []}


@mcp.tool()
async def get_leaderboards() -> Any:
    url = chess_urls.leaderboards()
    async with httpx.AsyncClient() as ac:
        r = await ac.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    return {}

