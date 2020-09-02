import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        saved_highscore = 'highscore.json'
        try:
            with open(saved_highscore) as sh:
                numbers = json.load(sh)
                self.high_score = numbers
        except FileNotFoundError:
            msg = f"Can’t find file: {saved_highscore}."
            print(msg)
        else:
            self.high_score = 0
            print(numbers)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
