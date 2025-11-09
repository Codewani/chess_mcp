# chess_mcp

A small project that exposes Chess.com Public API helpers as FastMCP tools and URL utilities.

This repository provides:

- `chess_urls.py` — a `CHESSAPIURLS` helper class for building Chess.com Public API endpoints.
- `main.py` — MCP tool implementations that call Chess.com endpoints asynchronously using `httpx` (and follow the project's `get_chess_pgns` pattern).

## Features

- Generate Chess.com API URLs for player profiles, stats, games, clubs, tournaments, matches, countries, puzzles, streamers, and leaderboards.
- FastMCP tools wrapping the public API endpoints for easy automation and composition.

## Requirements

- Python 3.8+
- Dependencies listed in `pyproject.toml` (e.g. `httpx`).

Install dependencies (recommended to use a venv):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt || python -m pip install httpx
```

Note: The repository uses `pyproject.toml`. If you prefer, install with `pip install -e .` after adding project metadata.

## Quick usage

1. Build a URL using `CHESSAPIURLS`:

```python
from chess_urls import CHESSAPIURLS

urls = CHESSAPIURLS()
print(urls.player_profile('magnuscarlsen'))
print(urls.player_games_archives('erik'))
```

2. Use the MCP tools in `main.py` (examples assume the MCP server / runner you use loads the tools):

- `get_chess_pgns(username, year, month)` — fetch PGNs for a given month.
- Other tools follow the same pattern and use a global `HEADERS` constant for requests.

Example snippet to fetch a player's profile using `httpx` directly:

```python
import asyncio
import httpx
from chess_urls import CHESSAPIURLS

HEADERS = {"User-Agent": "Me"}

async def fetch_profile(username):
	urls = CHESSAPIURLS()
	async with httpx.AsyncClient() as c:
		r = await c.get(urls.player_profile(username), headers=HEADERS)
		r.raise_for_status()
		return r.json()

async def main():
	profile = await fetch_profile('magnuscarlsen')
	print(profile)

asyncio.run(main())
```

## Configuration

- `HEADERS`: The code uses a global `HEADERS` constant (e.g. `{ "User-Agent": "Me" }`). You can externalize this to environment variables or a config file if needed.

## Development notes

- The project intentionally avoids threads and follows a pure-async pattern using `httpx.AsyncClient`.
- Consider creating a shared `AsyncClient` instance for connection pooling if many requests are made.

## Tests / Verification

There are no automated tests included yet. Quick checks you can run locally:

1. Verify that `CHESSAPIURLS` builds expected endpoints (run a quick REPL or tiny script):

```bash
python -c "from chess_urls import CHESSAPIURLS; u=CHESSAPIURLS(); print(u.player_profile('magnuscarlsen'))"
```

2. Run the small `httpx` snippet above to confirm requests work.

## Contributing

Contributions welcome. Suggested small steps:

1. Add unit tests for `CHESSAPIURLS` URL generation.
2. Add more MCP tools and consistent tests for each tool's behavior (mock external calls).
3. Add CI (GitHub Actions) to run linters and tests.

Please open issues or pull requests with clear descriptions and small, focused changes.

## License

This project does not include a license file. Add one (e.g. `MIT`) if you want to make the repo open-source.

---

If you'd like, I can also:

- Add a `requirements.txt` generated from `pyproject.toml`.
- Create a small test that verifies a few URL outputs from `CHESSAPIURLS` and run it.
- Make `HEADERS` configurable via environment variables and show an example `.env` file.

Tell me which extras you want and I'll add them next.
