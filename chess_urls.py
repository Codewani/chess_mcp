class CHESSAPIURLS:
    """
    Methods return full URLs as strings. They follow patterns documented at
    https://www.chess.com/news/view/published-data-api
    """

    def __init__(self):
        self.base_url = "https://api.chess.com/"

    # Player endpoints
    def player_profile(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}"

    def titled_players(self, title_abbrev: str) -> str:
        """title_abbrev: GM, WGM, IM, ..."""
        return self.base_url + f"pub/titled/{title_abbrev}"

    def player_stats(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/stats"

    def player_is_online(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/is-online"

    # Player games
    def player_games_current(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/games"

    def player_games_to_move(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/games/to-move"

    def player_games_archives(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/games/archives"

    def player_games_archive(self, username: str, year: str, month: str) -> str:
        return self.base_url + f"pub/player/{username}/games/{year}/{month}"

    def player_games_pgn(self, username: str, year: str, month: str) -> str:
        return self.base_url + f"pub/player/{username}/games/{year}/{month}/pgn"

    def player_games_live_by_time(self, username: str, basetime: int, increment: int | None = None) -> str:
        """Return live games archive by time control. increment is optional."""
        if increment is None:
            return self.base_url + f"pub/player/{username}/games/live/{basetime}"
        return self.base_url + f"pub/player/{username}/games/live/{basetime}/{increment}"

    # Player related lists
    def player_clubs(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/clubs"

    def player_matches(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/matches"

    def player_tournaments(self, username: str) -> str:
        return self.base_url + f"pub/player/{username}/tournaments"

    # Clubs
    def club_profile(self, url_id: str) -> str:
        return self.base_url + f"pub/club/{url_id}"

    def club_members(self, url_id: str) -> str:
        return self.base_url + f"pub/club/{url_id}/members"

    def club_matches(self, url_id: str) -> str:
        return self.base_url + f"pub/club/{url_id}/matches"

    # Tournaments
    def tournament(self, url_id: str) -> str:
        return self.base_url + f"pub/tournament/{url_id}"

    def tournament_round(self, url_id: str, round_no: int) -> str:
        return self.base_url + f"pub/tournament/{url_id}/{round_no}"

    def tournament_round_group(self, url_id: str, round_no: int, group: int) -> str:
        return self.base_url + f"pub/tournament/{url_id}/{round_no}/{group}"

    # Team matches
    def match(self, match_id: int) -> str:
        return self.base_url + f"pub/match/{match_id}"

    def match_board(self, match_id: int, board: int) -> str:
        return self.base_url + f"pub/match/{match_id}/{board}"

    def live_match(self, match_id: int) -> str:
        return self.base_url + f"pub/match/live/{match_id}"

    def live_match_board(self, match_id: int, board: int) -> str:
        return self.base_url + f"pub/match/live/{match_id}/{board}"

    # Countries
    def country_profile(self, iso: str) -> str:
        return self.base_url + f"pub/country/{iso}"

    def country_players(self, iso: str) -> str:
        return self.base_url + f"pub/country/{iso}/players"

    def country_clubs(self, iso: str) -> str:
        return self.base_url + f"pub/country/{iso}/clubs"

    # Puzzles, streamers, leaderboards
    def daily_puzzle(self) -> str:
        return self.base_url + "pub/puzzle"

    def random_daily_puzzle(self) -> str:
        return self.base_url + "pub/puzzle/random"

    def streamers(self) -> str:
        return self.base_url + "pub/streamers"

    def leaderboards(self) -> str:
        return self.base_url + "pub/leaderboards"

    # Misc / helpers
    def raw(self, path: str) -> str:
        """Return a raw path appended to the base URL. path should not start with a leading slash."""
        return self.base_url + path
